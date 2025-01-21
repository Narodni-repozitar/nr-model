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

from nr_metadata.documents.records.api import DocumentsRecord
from nr_metadata.documents.services.records.permissions import DocumentsPermissionPolicy
from nr_metadata.documents.services.records.results import (
    DocumentsRecordItem,
    DocumentsRecordList,
)
from nr_metadata.documents.services.records.schema import NRDocumentRecordSchema
from nr_metadata.documents.services.records.search import DocumentsSearchOptions


class DocumentsServiceConfig(PermissionsPresetsConfigMixin, RDMRecordServiceConfig):
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

        return process_service_configs(self) + [OwnersComponent, CustomFieldsComponent]

    model = "nr_metadata.documents"

    @property
    def links_item(self):
        return {
            "draft": RecordLink(
                "{+api}/nr-metadata-documents/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/nr-metadata-documents/{id}/edit",
                when=has_draft() & has_permission("update"),
            ),
            "latest": RecordLink(
                "{+api}/nr-metadata-documents/{id}/versions/latest",
                when=has_permission("read"),
            ),
            "latest_html": RecordLink(
                "{+ui}/nr-metadata-documents/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/nr-metadata-documents/{id}/draft/actions/publish",
                when=has_permission("publish"),
            ),
            "record": RecordLink(
                "{+api}/nr-metadata-documents/{id}",
                when=has_published_record() & has_permission("read"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/nr-metadata-documents/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+api}/nr-metadata-documents/{id}/draft",
                    when=has_permission("read_draft"),
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+ui}/nr-metadata-documents/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+ui}/nr-metadata-documents/{id}/preview",
                    when=has_permission("read_draft"),
                ),
            ),
            "versions": RecordLink(
                "{+api}/nr-metadata-documents/{id}/versions",
                when=has_permission("search_versions"),
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/nr-metadata-documents/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+api}/nr-metadata-documents/{id}/draft",
                    when=has_permission("read_draft"),
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+ui}/nr-metadata-documents/{id}", when=has_permission("read")
                ),
                else_=RecordLink(
                    "{+ui}/nr-metadata-documents/{id}/preview",
                    when=has_permission("read_draft"),
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/nr-metadata-documents/{?args*}"),
            **pagination_links_html("{+ui}/nr-metadata-documents/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/nr-metadata-documents/{?args*}"),
            **pagination_links_html("{+ui}/user/nr-metadata-documents/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/nr-metadata-documents/{id}/versions{?args*}"),
        }
