import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import (
    InvenioUISchema,
    LocalizedDate,
    LocalizedEDTFInterval,
)
from oarepo_vocabularies.services.ui_schema import (
    HierarchyUISchema,
    VocabularyI18nStrUIField,
)

from nr_metadata.common.services.records.ui_schema_common import (
    AdditionalTitlesUISchema,
    NRCommonMetadataUISchema,
)
from nr_metadata.common.services.records.ui_schema_datatypes import (
    NREventUISchema,
    NRFundingReferenceUISchema,
    NRGeoLocationUISchema,
    NRRelatedItemUISchema,
    NRSeriesUISchema,
    NRSubjectUISchema,
)
from nr_metadata.ui_schema.identifiers import (
    NRObjectIdentifierUISchema,
    NRSystemIdentifierUISchema,
)
from nr_metadata.ui_schema.subjects import NRSubjectListField


class NRDataRecordUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    deletion_status = ma_fields.String()

    is_deleted = ma_fields.Boolean()

    is_published = ma_fields.Boolean()

    metadata = ma_fields.Nested(lambda: NRDataMetadataUISchema())

    version_id = ma_fields.Integer()


class NRDataMetadataUISchema(NRCommonMetadataUISchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesUISchema())
    )

    dateCollected = LocalizedEDTFInterval()

    dateCreated = LocalizedEDTFInterval()

    dateValidTo = LocalizedDate()

    dateWithdrawn = ma_fields.Nested(lambda: DateWithdrawnUISchema())

    events = ma_fields.List(ma_fields.Nested(lambda: NREventUISchema()))

    fundingReferences = ma_fields.List(
        ma_fields.Nested(lambda: NRFundingReferenceUISchema())
    )

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationUISchema()))

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierUISchema())
    )

    publishers = ma_fields.List(ma_fields.Nested(lambda: PublishersItemUISchema()))

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: NRRelatedItemUISchema()))

    series = ma_fields.List(ma_fields.Nested(lambda: NRSeriesUISchema()))

    subjects = NRSubjectListField(ma_fields.Nested(lambda: NRSubjectUISchema()))

    systemIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRSystemIdentifierUISchema())
    )


class DateWithdrawnUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateInformation = ma_fields.String()

    type = LocalizedDate()


class PublishersItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    ror = ma_fields.String()

    title = VocabularyI18nStrUIField()
