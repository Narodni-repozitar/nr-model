from oarepo_workflows.services.records.schema import RDMWorkflowParentSchema


class GeneratedParentSchema(RDMWorkflowParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class NRCommonRecordSchema(RDMBaseRecordSchema):
    parent = ma.fields.Nested(GeneratedParentSchema)
