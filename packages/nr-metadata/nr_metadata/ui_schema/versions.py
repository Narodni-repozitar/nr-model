import marshmallow as ma


class FillMissingVersionMixin(ma.Schema):
    @ma.post_dump
    def fill_missing_version(self, value, **kwargs):
        value.setdefault("metadata", {}).setdefault(
            "version", value.get("versions", {}).get("index")
        )
        return value
