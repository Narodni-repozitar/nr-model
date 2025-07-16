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

from nr_metadata.data.records.api import DataRecord
from nr_metadata.data.services.records.permissions import DataPermissionPolicy
from nr_metadata.data.services.records.results import DataRecordItem, DataRecordList
from nr_metadata.data.services.records.schema import NRDataRecordSchema
from nr_metadata.data.services.records.search import DataSearchOptions


class DataServiceConfig(
    SearchAllConfigMixin, PermissionsPresetsConfigMixin, RDMRecordServiceConfig
):
    """DataRecord service config."""

    result_item_cls = DataRecordItem

    result_list_cls = DataRecordList

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/nr-metadata-data/"

    base_permission_policy_cls = DataPermissionPolicy

    schema = NRDataRecordSchema

    search = DataSearchOptions

    record_cls = DataRecord

    service_id = "data"
    indexer_queue_name = "data"

    search_item_links_template = LinksTemplate

    @property
    def components(self):
        return process_service_configs(self, CustomFieldsComponent, WorkflowComponent)

    model = "nr_metadata.data"

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
                "{+api}/nr-metadata-data/{id}/draft",
                when=has_draft_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/nr-metadata-data/{id}/edit",
                when=has_draft_permission("update_draft"),
            ),
            "latest": RecordLink(
                "{+api}/nr-metadata-data/{id}/versions/latest",
                when=has_permission("read"),
            ),
            "latest_html": RecordLink(
                "{+ui}/nr-metadata-data/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/nr-metadata-data/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/nr-metadata-data/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/nr-metadata-data/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+api}/nr-metadata-data/{id}/draft",
                    when=has_permission("read_draft"),
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+ui}/nr-metadata-data/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+ui}/nr-metadata-data/{id}/preview",
                    when=has_permission("read_draft"),
                ),
            ),
            "versions": RecordLink(
                "{+api}/nr-metadata-data/{id}/versions",
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
                    "{+api}/nr-metadata-data/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+api}/nr-metadata-data/{id}/draft",
                    when=has_permission("read_draft"),
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+ui}/nr-metadata-data/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+ui}/nr-metadata-data/{id}/preview",
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
            **pagination_links("{+api}/nr-metadata-data/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-data/{?args*}"),
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
            **pagination_links("{+api}/user/nr-metadata-data/{?args*}"),
            **pagination_links_html("{+ui}/user/nr-metadata-data/{?args*}"),
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
            **pagination_links("{+api}/nr-metadata-data/{id}/versions{?args*}"),
        }
        return {k: v for k, v in links.items() if v is not None}
