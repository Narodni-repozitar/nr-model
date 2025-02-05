from invenio_rdm_records.services.config import RDMRecordServiceConfig
from invenio_records_resources.services import (
    ConditionalLink,
    LinksTemplate,
    RecordLink,
    pagination_links,
)
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    OwnersComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_draft,
    has_permission,
    has_published_record,
    is_published_record,
)
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


class CommonServiceConfig(PermissionsPresetsConfigMixin, RDMRecordServiceConfig):
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

        return process_service_configs(self) + [OwnersComponent, CustomFieldsComponent]

    model = "nr_metadata.common"

    @property
    def links_item(self):
        return {
            "draft": RecordLink(
                "{+api}/nr-metadata-common/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/nr-metadata-common/{id}/edit",
                when=has_draft() & has_permission("update"),
            ),
            "latest": RecordLink(
                "{+api}/nr-metadata-common/{id}/versions/latest",
                when=has_permission("read"),
            ),
            "latest_html": RecordLink(
                "{+ui}/nr-metadata-common/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/nr-metadata-common/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/nr-metadata-common/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/nr-metadata-common/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+api}/nr-metadata-common/{id}/draft",
                    when=has_permission("read_draft"),
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+ui}/nr-metadata-common/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+ui}/nr-metadata-common/{id}/preview",
                    when=has_permission("read_draft"),
                ),
            ),
            "versions": RecordLink(
                "{+api}/nr-metadata-common/{id}/versions",
                when=has_permission("search_versions"),
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/nr-metadata-common/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+api}/nr-metadata-common/{id}/draft",
                    when=has_permission("read_draft"),
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+ui}/nr-metadata-common/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+ui}/nr-metadata-common/{id}/preview",
                    when=has_permission("read_draft"),
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-common/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-common/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/nr-metadata-common/{?args*}"),
            **pagination_links_html("{+ui}/user/nr-metadata-common/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/nr-metadata-common/{id}/versions{?args*}"),
        }
