from invenio_rdm_records.services.config import RDMRecordServiceConfig, _groups_enabled
from invenio_records_resources.services import (
    ConditionalLink,
    LinksTemplate,
    RecordLink,
    pagination_links,
)
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_draft_permission,
    has_permission,
    has_published_record,
    is_published_record,
)
from oarepo_runtime.services.config.service import (
    PermissionsPresetsConfigMixin,
    SearchAllConfigMixin,
)
from oarepo_runtime.services.records import pagination_links_html
from oarepo_workflows.services.components.workflow import WorkflowComponent

from nr_metadata.common.records.api import CommonRecord
from nr_metadata.common.services.records.permissions import CommonPermissionPolicy
from nr_metadata.common.services.records.results import (
    CommonRecordItem,
    CommonRecordList,
)
from nr_metadata.common.services.records.schema_common import NRCommonRecordSchema
from nr_metadata.common.services.records.search import CommonSearchOptions


class CommonServiceConfig(
    SearchAllConfigMixin, PermissionsPresetsConfigMixin, RDMRecordServiceConfig
):
    """CommonRecord service config."""

    result_item_cls = CommonRecordItem

    result_list_cls = CommonRecordList

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/nr-metadata-common/"

    base_permission_policy_cls = CommonPermissionPolicy

    schema = NRCommonRecordSchema

    search = CommonSearchOptions

    record_cls = CommonRecord

    service_id = "common"
    indexer_queue_name = "common"

    search_item_links_template = LinksTemplate

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent, WorkflowComponent)

    model = "nr_metadata.common"

    @property
    def links_item(self):
        try:
            supercls_links = super().links_item
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            "access_grants": RecordLink("{+api}/records/{id}/access/grants"),
            "access_groups": RecordLink(
                "{+api}/records/{id}/access/groups", when=_groups_enabled
            ),
            "access_links": RecordLink("{+api}/records/{id}/access/links"),
            "access_users": RecordLink("{+api}/records/{id}/access/users"),
            "draft": RecordLink(
                "{+api}/nr-metadata-common/{id}/draft",
                when=has_draft_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/nr-metadata-common/{id}/edit",
                when=has_draft_permission("update_draft"),
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
        return {k: v for k, v in links.items() if v is not None}

    @property
    def links_search_item(self):
        try:
            supercls_links = super().links_search_item
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
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
        return {k: v for k, v in links.items() if v is not None}

    @property
    def links_search(self):
        try:
            supercls_links = super().links_search
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            **pagination_links("{+api}/nr-metadata-common/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-common/{?args*}"),
        }
        return {k: v for k, v in links.items() if v is not None}

    @property
    def links_search_drafts(self):
        try:
            supercls_links = super().links_search_drafts
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            **pagination_links("{+api}/user/nr-metadata-common/{?args*}"),
            **pagination_links_html("{+ui}/user/nr-metadata-common/{?args*}"),
        }
        return {k: v for k, v in links.items() if v is not None}

    @property
    def links_search_versions(self):
        try:
            supercls_links = super().links_search_versions
        except AttributeError:  # if they aren't defined in the superclass
            supercls_links = {}
        links = {
            **supercls_links,
            **pagination_links("{+api}/nr-metadata-common/{id}/versions{?args*}"),
        }
        return {k: v for k, v in links.items() if v is not None}
