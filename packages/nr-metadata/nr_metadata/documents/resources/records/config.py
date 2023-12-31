import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig

from nr_metadata.documents.resources.records.ui import DocumentsUIJSONSerializer


class DocumentsResourceConfig(RecordResourceConfig):
    """DocumentsRecord resource config."""

    blueprint_name = "documents"
    url_prefix = "/nr-metadata-documents/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.nr_metadata.documents.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                DocumentsUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
