import marshmallow as ma


class NRSubjectListField(ma.fields.List):
    def __init__(self, cls_or_instance, **kwargs):
        super().__init__(ma.fields.Raw(), **kwargs)

    def _serialize(self, value, attr=None, obj=None, **kwargs):
        raw = super()._serialize(value, attr, obj, **kwargs)
        ret = []
        for r in raw:
            for rr in r.get("subject", []):
                ret.append(
                    {
                        **r,
                        "subject": rr,
                    }
                )
        return ret
