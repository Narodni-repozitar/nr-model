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

from nr_metadata.common.records.api import CommonRecord
from nr_metadata.common.services.records.permissions import CommonPermissionPolicy
from nr_metadata.common.services.records.results import (
    CommonRecordItem,
    CommonRecordList,
)
from nr_metadata.common.services.records.schema_common import NRCommonRecordSchema
from nr_metadata.common.services.records.search import CommonSearchOptions


class CommonServiceConfig(PermissionsPresetsConfigMixin, InvenioRecordServiceConfig):
    """CommonRecord service config."""

    result_item_cls = CommonRecordItem

    result_list_cls = CommonRecordList

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/nr-metadata-common/"

    base_permission_policy_cls = CommonPermissionPolicy

    schema = NRCommonRecordSchema

    search = CommonSearchOptions

    record_cls = CommonRecord

    service_id = "common"

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

    model = "nr_metadata.common"

    @property
    def links_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-common/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-common/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": RecordLink(
                "{+api}/nr-metadata-common/{id}", when=has_permission("read")
            ),
            "self_html": RecordLink(
                "{+ui}/nr-metadata-common/{id}", when=has_permission("read")
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-common/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-common/{?args*}"),
        }
