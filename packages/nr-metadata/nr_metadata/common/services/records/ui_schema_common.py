import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from oarepo_runtime.services.schema.i18n_ui import (
    I18nStrUIField,
    MultilingualLocalizedUIField,
    MultilingualUIField,
)
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.rdm_ui import (
    RDMCreatorsUISchema,
    RDMFundersUISchema,
)
from oarepo_runtime.services.schema.ui import (
    InvenioRDMUISchema,
    LocalizedDate,
    LocalizedDateTime,
    LocalizedEDTF,
)

from nr_metadata.common.services.records.ui_schema_datatypes import (
    NREventUISchema,
    NRGeoLocationUISchema,
    NRLanguageVocabularyUISchema,
    NRRelatedItemUISchema,
    NRResourceTypeVocabularyUISchema,
    NRRightsVocabularyUISchema,
    NRSeriesUISchema,
    NRSubjectCategoryVocabularyUISchema,
    NRSubjectUISchema,
)
from nr_metadata.ui_schema.identifiers import (
    NRObjectIdentifierUISchema,
    NRSystemIdentifierUISchema,
)
from nr_metadata.ui_schema.subjects import NRSubjectListField


class NRCommonRecordUISchema(InvenioRDMUISchema):
    class Meta:
        unknown = ma.RAISE

    deletion_status = ma_fields.String()

    is_deleted = ma_fields.Boolean()

    is_published = ma_fields.Boolean()

    metadata = ma_fields.Nested(lambda: NRCommonMetadataUISchema())

    state = ma_fields.String(dump_only=True)

    state_timestamp = LocalizedDateTime(dump_only=True)

    version_id = ma_fields.Integer()


class NRCommonMetadataUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    abstract = MultilingualUIField(I18nStrUIField())

    accessibility = MultilingualLocalizedUIField(I18nStrUIField())

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesUISchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: RDMCreatorsUISchema()))

    creators = ma_fields.List(
        ma_fields.Nested(lambda: RDMCreatorsUISchema()), required=True
    )

    dateAvailable = LocalizedDate()

    dateIssued = LocalizedEDTF(required=True)

    events = ma_fields.List(ma_fields.Nested(lambda: NREventUISchema()))

    funders = ma_fields.List(ma_fields.Nested(lambda: RDMFundersUISchema()))

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationUISchema()))

    languages = ma_fields.List(ma_fields.Nested(lambda: NRLanguageVocabularyUISchema()))

    methods = MultilingualUIField(I18nStrUIField())

    notes = ma_fields.List(ma_fields.String())

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierUISchema())
    )

    originalRecord = ma_fields.String()

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: NRRelatedItemUISchema()))

    resourceType = ma_fields.Nested(
        lambda: NRResourceTypeVocabularyUISchema(), required=True
    )

    rights = ma_fields.Nested(lambda: NRRightsVocabularyUISchema())

    series = ma_fields.List(ma_fields.Nested(lambda: NRSeriesUISchema()))

    subjectCategories = ma_fields.List(
        ma_fields.Nested(lambda: NRSubjectCategoryVocabularyUISchema())
    )

    subjects = NRSubjectListField(ma_fields.Nested(lambda: NRSubjectUISchema()))

    systemIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRSystemIdentifierUISchema())
    )

    technicalInfo = MultilingualUIField(I18nStrUIField())

    title = ma_fields.String(required=True)

    version = ma_fields.String()


class AdditionalTitlesUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    title = I18nStrUIField(required=True)

    titleType = ma_fields.String(
        required=True,
        validate=[OneOf(["translatedTitle", "alternativeTitle", "subtitle", "other"])],
    )
