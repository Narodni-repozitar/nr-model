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

from nr_metadata.data.records.api import DataRecord
from nr_metadata.data.services.records.permissions import DataPermissionPolicy
from nr_metadata.data.services.records.results import DataRecordItem, DataRecordList
from nr_metadata.data.services.records.schema import NRDataRecordSchema
from nr_metadata.data.services.records.search import DataSearchOptions


class DataServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """DataRecord service config."""

    result_item_cls = DataRecordItem

    result_list_cls = DataRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-metadata-data/"

    base_permission_policy_cls = DataPermissionPolicy

    schema = NRDataRecordSchema

    search = DataSearchOptions

    record_cls = DataRecord

    service_id = "data"

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

    model = "nr_metadata.data"

    @property
    def links_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-data/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-data/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-data/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-data/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-data/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-data/{?args*}"),
        }
