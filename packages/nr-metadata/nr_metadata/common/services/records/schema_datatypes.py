import marshmallow as ma
from edtf import Interval as EDTFInterval
from invenio_rdm_records.services.schemas.metadata import CreatorSchema
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow_utils.fields import TrimmedString
from oarepo_runtime.services.schema.i18n import I18nStrField, MultilingualField
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.validation import (
    CachedMultilayerEDTFValidator,
    validate_identifier,
)

from nr_metadata.schema.identifiers import NRObjectIdentifierSchema


class NREventSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eventDate = TrimmedString(
        required=True, validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    eventLocation = ma_fields.Nested(lambda: NRLocationSchema(), required=True)

    eventNameAlternate = ma_fields.List(ma_fields.String())

    eventNameOriginal = ma_fields.String(required=True)


class NRGeoLocationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    geoLocationPlace = ma_fields.String()

    geoLocationPoint = ma_fields.Nested(lambda: NRGeoLocationPointSchema())


class NRLocationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    country = ma_fields.Nested(lambda: NRCountryVocabularySchema())

    place = ma_fields.String(required=True)


class NRRelatedItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(ma_fields.Nested(lambda: CreatorSchema()))

    itemCreators = ma_fields.List(ma_fields.Nested(lambda: CreatorSchema()))

    itemEndPage = ma_fields.String()

    itemIssue = ma_fields.String()

    itemPIDs = ma_fields.List(
        ma_fields.Nested(
            lambda: NRObjectIdentifierSchema(),
            validate=[lambda value: validate_identifier(value)],
        )
    )

    itemPublisher = ma_fields.String()

    itemRelationType = ma_fields.Nested(lambda: NRItemRelationTypeVocabularySchema())

    itemResourceType = ma_fields.Nested(lambda: NRResourceTypeVocabularySchema())

    itemStartPage = ma_fields.String()

    itemTitle = ma_fields.String(required=True)

    itemURL = ma_fields.String()

    itemVolume = ma_fields.String()

    itemYear = ma_fields.Integer()


class NRCountryVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRGeoLocationPointSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    pointLatitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    pointLongitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )


class NRItemRelationTypeVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRLanguageVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRResourceTypeVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRRightsVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRSeriesSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    seriesTitle = ma_fields.String(required=True)

    seriesVolume = ma_fields.String()


class NRSubjectCategoryVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRSubjectSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classificationCode = ma_fields.String()

    subject = MultilingualField(I18nStrField(), required=True)

    subjectScheme = ma_fields.String()

    valueURI = ma_fields.String()


class NRExternalLocationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    externalLocationNote = ma_fields.String()

    externalLocationURL = ma_fields.String(required=True)
