import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from oarepo_runtime.services.schema.i18n_ui import I18nStrUIField
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.rdm_ui import RDMCreatorsUISchema
from oarepo_runtime.services.schema.ui import LocalizedEDTFInterval
from oarepo_vocabularies.services.ui_schema import VocabularyI18nStrUIField

from nr_metadata.ui_schema.identifiers import NRObjectIdentifierUISchema


class NREventUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eventDate = LocalizedEDTFInterval(required=True)

    eventLocation = ma_fields.Nested(lambda: NRLocationUISchema(), required=True)

    eventNameAlternate = ma_fields.List(ma_fields.String())

    eventNameOriginal = ma_fields.String(required=True)


class NRGeoLocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    geoLocationPlace = ma_fields.String()

    geoLocationPoint = ma_fields.Nested(lambda: NRGeoLocationPointUISchema())


class NRLocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    country = ma_fields.Nested(lambda: NRCountryVocabularyUISchema())

    place = ma_fields.String(required=True)


class NRRelatedItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(ma_fields.Nested(lambda: RDMCreatorsUISchema()))

    itemCreators = ma_fields.List(ma_fields.Nested(lambda: RDMCreatorsUISchema()))

    itemEndPage = ma_fields.String()

    itemIssue = ma_fields.String()

    itemPIDs = ma_fields.List(ma_fields.Nested(lambda: NRObjectIdentifierUISchema()))

    itemPublisher = ma_fields.String()

    itemRelationType = ma_fields.Nested(lambda: NRItemRelationTypeVocabularyUISchema())

    itemResourceType = ma_fields.Nested(lambda: NRResourceTypeVocabularyUISchema())

    itemStartPage = ma_fields.String()

    itemTitle = ma_fields.String(required=True)

    itemURL = ma_fields.String()

    itemVolume = ma_fields.String()

    itemYear = ma_fields.Integer()


class NRCountryVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRGeoLocationPointUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    pointLatitude = ma_fields.Float(required=True)

    pointLongitude = ma_fields.Float(required=True)


class NRItemRelationTypeVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRLanguageVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRResourceTypeVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRRightsVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRSeriesUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    seriesTitle = ma_fields.String(required=True)

    seriesVolume = ma_fields.String()


class NRSubjectCategoryVocabularyUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRSubjectUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classificationCode = ma_fields.String()

    subject = I18nStrUIField()

    subjectScheme = ma_fields.String()

    valueURI = ma_fields.String()


class NRExternalLocationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    externalLocationNote = ma_fields.String()

    externalLocationURL = ma_fields.String(required=True)
