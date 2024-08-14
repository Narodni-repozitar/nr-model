import marshmallow as ma
from edtf import Date as EDTFDate
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from marshmallow_utils.fields import TrimmedString
from oarepo_runtime.services.schema.i18n import I18nStrField, MultilingualField
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import (
    CachedMultilayerEDTFValidator,
    validate_date,
    validate_identifier,
)

from nr_metadata.common.services.records.schema_datatypes import (
    NRAccessRightsVocabularySchema,
    NRContributorSchema,
    NRCreatorSchema,
    NREventSchema,
    NRFundingReferenceSchema,
    NRGeoLocationSchema,
    NRLanguageVocabularySchema,
    NRRelatedItemSchema,
    NRResourceTypeVocabularySchema,
    NRRightsVocabularySchema,
    NRSeriesSchema,
    NRSubjectCategoryVocabularySchema,
    NRSubjectSchema,
)
from nr_metadata.schema.identifiers import (
    NRObjectIdentifierSchema,
    NRSystemIdentifierSchema,
)


class NRCommonRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRCommonMetadataSchema())


class NRCommonMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    abstract = MultilingualField(I18nStrField())

    accessRights = ma_fields.Nested(lambda: NRAccessRightsVocabularySchema())

    accessibility = MultilingualField(I18nStrField())

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesSchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: NRContributorSchema()))

    creators = ma_fields.List(
        ma_fields.Nested(lambda: NRCreatorSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    dateAvailable = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    dateIssued = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFDate,))]
    )

    events = ma_fields.List(ma_fields.Nested(lambda: NREventSchema()))

    fundingReferences = ma_fields.List(
        ma_fields.Nested(lambda: NRFundingReferenceSchema())
    )

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationSchema()))

    languages = ma_fields.List(ma_fields.Nested(lambda: NRLanguageVocabularySchema()))

    methods = MultilingualField(I18nStrField())

    notes = ma_fields.List(ma_fields.String())

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(
            lambda: NRObjectIdentifierSchema(),
            validate=[lambda value: validate_identifier(value)],
        )
    )

    originalRecord = ma_fields.String()

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: NRRelatedItemSchema()))

    resourceType = ma_fields.Nested(
        lambda: NRResourceTypeVocabularySchema(), required=True
    )

    rights = ma_fields.Nested(lambda: NRRightsVocabularySchema())

    series = ma_fields.List(ma_fields.Nested(lambda: NRSeriesSchema()))

    subjectCategories = ma_fields.List(
        ma_fields.Nested(lambda: NRSubjectCategoryVocabularySchema())
    )

    subjects = ma_fields.List(ma_fields.Nested(lambda: NRSubjectSchema()))

    systemIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRSystemIdentifierSchema())
    )

    technicalInfo = MultilingualField(I18nStrField())

    title = ma_fields.String(required=True)

    version = ma_fields.String()


class AdditionalTitlesSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    title = I18nStrField(required=True)

    titleType = ma_fields.String(
        required=True,
        validate=[OneOf(["translatedTitle", "alternativeTitle", "subtitle", "other"])],
    )
