import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig

from nr_metadata.datacite.resources.records.ui import DataciteUIJSONSerializer


class DataciteResourceConfig(RecordResourceConfig):
    """DataciteRecord resource config."""

    blueprint_name = "datacite"
    url_prefix = "/nr-metadata-datacite/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.nr_metadata.datacite.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                DataciteUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
