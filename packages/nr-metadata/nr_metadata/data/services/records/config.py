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

from nr_metadata.data.records.api import DataRecord
from nr_metadata.data.services.records.permissions import DataPermissionPolicy
from nr_metadata.data.services.records.results import DataRecordItem, DataRecordList
from nr_metadata.data.services.records.schema import NRDataRecordSchema
from nr_metadata.data.services.records.search import DataSearchOptions


class DataServiceConfig(PermissionsPresetsConfigMixin, RDMRecordServiceConfig):
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

        return process_service_configs(self) + [OwnersComponent, CustomFieldsComponent]

    model = "nr_metadata.data"

    @property
    def links_item(self):
        return {
            "draft": RecordLink(
                "{+api}/nr-metadata-data/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/nr-metadata-data/{id}/edit",
                when=has_draft() & has_permission("update"),
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

    @property
    def links_search_item(self):
        return {
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

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-data/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-data/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/nr-metadata-data/{?args*}"),
            **pagination_links_html("{+ui}/user/nr-metadata-data/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/nr-metadata-data/{id}/versions{?args*}"),
        }
