import marshmallow as ma
from edtf import Date as EDTFDate
from invenio_rdm_records.services.schemas.access import AccessSchema
from invenio_rdm_records.services.schemas.metadata import CreatorSchema
from invenio_rdm_records.services.schemas.pids import PIDSchema
from invenio_rdm_records.services.schemas.record import validate_scheme
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import Dict, Nested
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode, TrimmedString
from marshmallow_utils.fields.nestedattr import NestedAttribute
from oarepo_runtime.services.schema.i18n import I18nStrField, MultilingualField
from oarepo_runtime.services.schema.marshmallow import (
    DictOnlySchema,
    RDMBaseRecordSchema,
)
from oarepo_runtime.services.schema.rdm import FundingSchema
from oarepo_runtime.services.schema.validation import (
    CachedMultilayerEDTFValidator,
    validate_date,
    validate_datetime,
    validate_identifier,
)

from nr_metadata.common.services.records.schema_datatypes import (
    NREventSchema,
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


class NRCommonRecordSchema(RDMBaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    access = NestedAttribute(lambda: AccessSchema())

    metadata = ma_fields.Nested(lambda: NRCommonMetadataSchema())

    pids = Dict(
        keys=SanitizedUnicode(validate=validate_scheme),
        values=Nested(PIDSchema),
    )

    state = ma_fields.String(dump_only=True)

    state_timestamp = ma_fields.String(dump_only=True, validate=[validate_datetime])


class NRCommonMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    abstract = MultilingualField(I18nStrField())

    accessibility = MultilingualField(I18nStrField())

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesSchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: CreatorSchema()))

    creators = ma_fields.List(
        ma_fields.Nested(lambda: CreatorSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
    )

    dateAvailable = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    dateIssued = TrimmedString(
        required=True, validate=[CachedMultilayerEDTFValidator(types=(EDTFDate,))]
    )

    events = ma_fields.List(ma_fields.Nested(lambda: NREventSchema()))

    funders = ma_fields.List(ma_fields.Nested(lambda: FundingSchema()))

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
