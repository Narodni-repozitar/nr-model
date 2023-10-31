import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.validate import OneOf
from oarepo_runtime.i18n.ui_schema import I18nStrUIField
from oarepo_runtime.services.schema.ui import LocalizedEDTFInterval
from oarepo_vocabularies.services.ui_schema import (
    HierarchyUISchema,
    VocabularyI18nStrUIField,
)

from nr_metadata.ui_schema.identifiers import (
    NRAuthorityIdentifierUISchema,
    NRObjectIdentifierUISchema,
)


class NREventUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    eventDate = LocalizedEDTFInterval(required=True)

    eventLocation = ma_fields.Nested(lambda: NRLocationUISchema(), required=True)

    eventNameAlternate = ma_fields.List(ma_fields.String())

    eventNameOriginal = ma_fields.String(required=True)


class NRRelatedItemUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(
        ma_fields.Nested(lambda: NRRelatedItemContributorUISchema())
    )

    itemCreators = ma_fields.List(
        ma_fields.Nested(lambda: NRRelatedItemCreatorUISchema())
    )

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


class NRFundingReferenceUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    funder = ma_fields.Nested(lambda: NRFunderVocabularyUISchema())

    fundingProgram = ma_fields.String()

    projectID = ma_fields.String(required=True)

    projectName = ma_fields.String()


class NRGeoLocationUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    geoLocationPlace = ma_fields.String(required=True)

    geoLocationPoint = ma_fields.Nested(lambda: NRGeoLocationPointUISchema())


class NRLocationUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    country = ma_fields.Nested(lambda: NRCountryVocabularyUISchema())

    place = ma_fields.String(required=True)


class NRRelatedItemContributorUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularyUISchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierUISchema())
    )

    fullName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])

    role = ma_fields.Nested(lambda: NRAuthorityRoleVocabularyUISchema())


class NRRelatedItemCreatorUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularyUISchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRAuthorityIdentifierUISchema())
    )

    fullName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])


class NRAccessRightsVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRAffiliationVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    title = VocabularyI18nStrUIField()


class NRAuthorityRoleVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRCountryVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRExternalLocationUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    externalLocationNote = ma_fields.String()

    externalLocationURL = ma_fields.String(required=True)


class NRFunderVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRGeoLocationPointUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    pointLatitude = ma_fields.Float(required=True)

    pointLongitude = ma_fields.Float(required=True)


class NRItemRelationTypeVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRLanguageVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRLicenseVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRResourceTypeVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRSeriesUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    seriesTitle = ma_fields.String(required=True)

    seriesVolume = ma_fields.String()


class NRSubjectCategoryVocabularyUISchema(Schema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = VocabularyI18nStrUIField()


class NRSubjectUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    classificationCode = ma_fields.String()

    subject = I18nStrUIField()

    subjectScheme = ma_fields.String()

    valueURI = ma_fields.String()
