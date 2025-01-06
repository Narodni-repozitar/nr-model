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

from nr_metadata.datacite.records.api import DataciteRecord
from nr_metadata.datacite.services.records.permissions import DatacitePermissionPolicy
from nr_metadata.datacite.services.records.results import (
    DataciteRecordItem,
    DataciteRecordList,
)
from nr_metadata.datacite.services.records.schema import DataCiteRecordSchema
from nr_metadata.datacite.services.records.search import DataciteSearchOptions


class DataciteServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """DataciteRecord service config."""

    result_item_cls = DataciteRecordItem

    result_list_cls = DataciteRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-metadata-datacite/"

    base_permission_policy_cls = DatacitePermissionPolicy

    schema = DataCiteRecordSchema

    search = DataciteSearchOptions

    record_cls = DataciteRecord

    service_id = "datacite"

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

    model = "nr_metadata.datacite"

    @property
    def links_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-datacite/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-datacite/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-datacite/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-datacite/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-datacite/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-datacite/{?args*}"),
        }
