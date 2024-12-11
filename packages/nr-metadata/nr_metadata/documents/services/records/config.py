from invenio_records_resources.services import LinksTemplate, RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import has_permission
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.records import pagination_links_html

from nr_metadata.documents.records.api import DocumentsRecord
from nr_metadata.documents.services.records.permissions import DocumentsPermissionPolicy
from nr_metadata.documents.services.records.results import (
    DocumentsRecordItem,
    DocumentsRecordList,
)
from nr_metadata.documents.services.records.schema import NRDocumentRecordSchema
from nr_metadata.documents.services.records.search import DocumentsSearchOptions


class DocumentsServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """DocumentsRecord service config."""

    result_item_cls = DocumentsRecordItem

    result_list_cls = DocumentsRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-metadata-documents/"

    base_permission_policy_cls = DocumentsPermissionPolicy

    schema = NRDocumentRecordSchema

    search = DocumentsSearchOptions

    record_cls = DocumentsRecord

    service_id = "documents"

    search_item_links_template = LinksTemplate

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [CustomFieldsComponent]
        components_list.extend(additional_components)
        seen = set()
        unique_components = []
        for component in components_list:
            if component not in seen:
                unique_components.append(component)
                seen.add(component)

        return unique_components

    model = "nr_metadata.documents"

    @property
    def links_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-documents/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-documents/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-documents/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-documents/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-documents/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-documents/{?args*}"),
        }
