import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_vocabularies.services.ui_schema import VocabularyI18nStrUIField


class AwardUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _version = String(data_key="@v", attribute="@v")

    acronym = ma_fields.String()

    identifiers = ma_fields.List(ma_fields.Nested(lambda: IdentifiersItemUISchema()))

    number = ma_fields.String()

    organizations = ma_fields.List(
        ma_fields.Nested(lambda: OrganizationsItemUISchema())
    )

    program = ma_fields.String()

    subjects = ma_fields.List(ma_fields.Nested(lambda: SubjectsItemUISchema()))

    title = VocabularyI18nStrUIField()


class FunderUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _version = String(data_key="@v", attribute="@v")

    identifiers = ma_fields.Nested(lambda: IdentifiersItemUISchema())

    name = ma_fields.String()


class IdentifiersItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    identifier = ma_fields.String()


class OrganizationsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    organization = ma_fields.String()

    scheme = ma_fields.String()


class SubjectsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    subject = ma_fields.String()
