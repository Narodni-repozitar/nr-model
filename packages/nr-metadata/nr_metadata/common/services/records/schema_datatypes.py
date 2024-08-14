import marshmallow as ma
from edtf import Interval as EDTFInterval
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow.validate import OneOf
from marshmallow_utils.fields import TrimmedString
from oarepo_runtime.services.schema.i18n import I18nStrField, MultilingualField
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.polymorphic import PolymorphicSchema
from oarepo_runtime.services.schema.validation import (
    CachedMultilayerEDTFValidator,
    validate_identifier,
)
from oarepo_vocabularies.services.schema import HierarchySchema

from nr_metadata.schema.identifiers import (
    NRObjectIdentifierSchema,
    NROrganizationIdentifierSchema,
    NRPersonIdentifierSchema,
)


class NRRelatedItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    itemContributors = ma_fields.List(
        ma_fields.Nested(lambda: NRRelatedItemContributorSchema())
    )

    itemCreators = ma_fields.List(
        ma_fields.Nested(lambda: NRRelatedItemCreatorSchema())
    )

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


class NRContributorSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(lambda: NRContributorOrganizationSchema())

    Personal = ma_fields.Nested(lambda: NRContributorPersonSchema())

    type_field = "nameType"


class NRCreatorSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(lambda: NROrganizationSchema())

    Personal = ma_fields.Nested(lambda: NRPersonSchema())

    type_field = "nameType"


class NREventSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eventDate = TrimmedString(
        required=True, validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    eventLocation = ma_fields.Nested(lambda: NRLocationSchema(), required=True)

    eventNameAlternate = ma_fields.List(ma_fields.String())

    eventNameOriginal = ma_fields.String(required=True)


class NRRelatedItemContributorSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(
        lambda: NRRelatedItemContributorOrganizationSchema()
    )

    Personal = ma_fields.Nested(lambda: NRRelatedItemContributorPersonSchema())

    type_field = "nameType"


class NRRelatedItemCreatorSchema(PolymorphicSchema):
    class Meta:
        unknown = ma.RAISE

    Organizational = ma_fields.Nested(lambda: NROrganizationSchema())

    Personal = ma_fields.Nested(lambda: NRPersonSchema())

    type_field = "nameType"


class NRContributorOrganizationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NROrganizationIdentifierSchema())
    )

    contributorType = ma_fields.Nested(
        lambda: NRContributorTypeVocabularySchema(), required=True
    )

    fullName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Organizational"])])


class NRContributorPersonSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularySchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRPersonIdentifierSchema())
    )

    contributorType = ma_fields.Nested(
        lambda: NRContributorTypeVocabularySchema(), required=True
    )

    familyName = ma_fields.String(required=True)

    fullName = ma_fields.String(required=True)

    givenName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Personal"])])


class NRFundingReferenceSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    funder = ma_fields.Nested(lambda: NRFunderVocabularySchema())

    fundingProgram = ma_fields.String()

    projectID = ma_fields.String(required=True)

    projectName = ma_fields.String()


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


class NRPersonSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularySchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRPersonIdentifierSchema())
    )

    familyName = ma_fields.String(required=True)

    fullName = ma_fields.String(required=True)

    givenName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Personal"])])


class NRRelatedItemContributorOrganizationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NROrganizationIdentifierSchema())
    )

    contributorType = ma_fields.Nested(
        lambda: NRContributorTypeVocabularySchema(), required=True
    )

    fullName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Organizational"])])


class NRRelatedItemContributorPersonSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliations = ma_fields.List(
        ma_fields.Nested(lambda: NRAffiliationVocabularySchema())
    )

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRPersonIdentifierSchema())
    )

    contributorType = ma_fields.Nested(
        lambda: NRContributorTypeVocabularySchema(), required=True
    )

    familyName = ma_fields.String(required=True)

    fullName = ma_fields.String(required=True)

    givenName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Personal"])])


class NRAccessRightsVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRAffiliationVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    ror = ma_fields.String()

    title = i18n_strings


class NRContributorTypeVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRCountryVocabularySchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    title = i18n_strings


class NRFunderVocabularySchema(DictOnlySchema):
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


class NROrganizationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    authorityIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NROrganizationIdentifierSchema())
    )

    fullName = ma_fields.String(required=True)

    nameType = ma_fields.String(validate=[OneOf(["Organizational"])])


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
