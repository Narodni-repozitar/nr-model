import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import RecordResourceConfig

from nr_metadata.common.resources.records.ui import CommonUIJSONSerializer


class CommonResourceConfig(RecordResourceConfig):
    """CommonRecord resource config."""

    blueprint_name = "common"
    url_prefix = "/nr-metadata-common/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.nr_metadata.common.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                CommonUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
