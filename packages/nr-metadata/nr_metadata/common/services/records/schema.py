import marshmallow as ma
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as InvenioParentSchema,
)
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema


class GeneratedParentSchema(InvenioParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class AwardSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _version = String(data_key="@v", attribute="@v")

    acronym = ma_fields.String()

    identifiers = ma_fields.List(ma_fields.Nested(lambda: IdentifiersItemSchema()))

    number = ma_fields.String()

    organizations = ma_fields.List(ma_fields.Nested(lambda: OrganizationsItemSchema()))

    program = ma_fields.String()

    subjects = ma_fields.List(ma_fields.Nested(lambda: SubjectsItemSchema()))

    title = i18n_strings


class FunderSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _version = String(data_key="@v", attribute="@v")

    identifiers = ma_fields.Nested(lambda: IdentifiersItemSchema())

    name = ma_fields.String()


class IdentifiersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    identifier = ma_fields.String()


class OrganizationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    organization = ma_fields.String()

    scheme = ma_fields.String()


class SubjectsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    subject = ma_fields.String()


class NRCommonRecordSchema(RDMBaseRecordSchema):
    parent = ma.fields.Nested(GeneratedParentSchema)
