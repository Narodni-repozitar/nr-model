import re
from functools import cached_property

from invenio_rdm_records.services.pids import PIDManager, PIDsService

from nr_metadata.datacite import config


class DataciteExt:

    def __init__(self, app=None):

        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.app = app

        self.init_config(app)
        if not self.is_inherited():
            self.register_flask_extension(app)

    def register_flask_extension(self, app):

        app.extensions["nr_metadata.datacite"] = self

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
        service_config = config.DATACITE_RECORD_SERVICE_CONFIG
        if hasattr(service_config, "build"):
            config_class = service_config.build(self.app)
        else:
            config_class = service_config()

        service_kwargs = {
            "pids_service": PIDsService(config_class, PIDManager),
            "config": config_class,
        }
        return config.DATACITE_RECORD_SERVICE_CLASS(
            **service_kwargs,
            files_service=self.service_files,
            draft_files_service=self.service_draft_files
        )

    @cached_property
    def resource_records(self):
        return config.DATACITE_RECORD_RESOURCE_CLASS(
            service=self.service_records,
            config=config.DATACITE_RECORD_RESOURCE_CONFIG(),
        )
