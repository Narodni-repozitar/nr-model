from invenio_drafts_resources.services.records.schema import (
    ParentSchema as InvenioParentSchema,
)


class GeneratedParentSchema(InvenioParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class NRCommonRecordSchema(BaseRecordSchema, RDMRecordMixin):
    parent = ma.fields.Nested(GeneratedParentSchema)
