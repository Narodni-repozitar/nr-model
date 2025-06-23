import re
from functools import cached_property

from invenio_rdm_records.services.pids import PIDManager, PIDsService
from oarepo_runtime.config import build_config

from nr_metadata.common import config


class CommonExt:

    def __init__(self, app=None):

        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.app = app

        self.init_config(app)
        if not self.is_inherited():
            self.register_flask_extension(app)

        for method in dir(self):
            if method.startswith("init_app_callback_"):
                getattr(self, method)(app)

    def register_flask_extension(self, app):

        app.extensions["nr_metadata.common"] = self

    def init_config(self, app):
        """Initialize configuration."""
        for identifier in dir(config):
            if re.match("^[A-Z_0-9]*$", identifier) and not identifier.startswith("_"):
                if isinstance(app.config.get(identifier), list):
                    app.config[identifier] += getattr(config, identifier)
                elif isinstance(app.config.get(identifier), dict):
                    for k, v in getattr(config, identifier).items():
                        if k not in app.config[identifier]:
                            app.config[identifier][k] = v
                else:
                    app.config.setdefault(identifier, getattr(config, identifier))

    def is_inherited(self):
        from importlib_metadata import entry_points

        ext_class = type(self)
        for ep in entry_points(group="invenio_base.apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        for ep in entry_points(group="invenio_base.api_apps"):
            loaded = ep.load()
            if loaded is not ext_class and issubclass(ext_class, loaded):
                return True
        return False

    @cached_property
    def service_records(self):
        service_config = build_config(config.COMMON_RECORD_SERVICE_CONFIG, self.app)

        service_kwargs = {
            "pids_service": PIDsService(service_config, PIDManager),
            "config": service_config,
        }
        return config.COMMON_RECORD_SERVICE_CLASS(
            **service_kwargs,
            files_service=self.service_files,
            draft_files_service=self.service_draft_files
        )

    @cached_property
    def resource_records(self):
        return config.COMMON_RECORD_RESOURCE_CLASS(
            service=self.service_records,
            config=build_config(config.COMMON_RECORD_RESOURCE_CONFIG, self.app),
        )

    def init_app_callback_rdm_models(self, app):

        app.config.setdefault("GLOBAL_SEARCH_MODELS", [])
        for cfg in app.config["GLOBAL_SEARCH_MODELS"]:
            if cfg["model_service"] == RDM_MODEL_CONFIG["model_service"]:
                break
        else:
            app.config["GLOBAL_SEARCH_MODELS"].append(RDM_MODEL_CONFIG)

        app.config.setdefault("RDM_MODELS", [])
        for cfg in app.config["RDM_MODELS"]:
            if cfg["model_service"] == RDM_MODEL_CONFIG["model_service"]:
                break
        else:
            app.config["RDM_MODELS"].append(RDM_MODEL_CONFIG)


RDM_MODEL_CONFIG = {  # allows merging stuff from other builders
    "service_id": "common",
    # deprecated
    "model_service": "nr_metadata.common.services.records.service.CommonService",
    # deprecated
    "service_config": "nr_metadata.common.services.records.config.CommonServiceConfig",
    "api_service": "nr_metadata.common.services.records.service.CommonService",
    "api_service_config": (
        "nr_metadata.common.services.records.config.CommonServiceConfig"
    ),
    "api_resource": "nr_metadata.common.resources.records.resource.CommonResource",
    "api_resource_config": (
        "nr_metadata.common.resources.records.config.CommonResourceConfig"
    ),
    "ui_resource_config": "ui.nr_metadata.common.CommonUIResourceConfig",
    "record_cls": "nr_metadata.common.records.api.CommonRecord",
    "pid_type": "common",
}
