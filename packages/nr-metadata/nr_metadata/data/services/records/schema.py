import marshmallow as ma
from edtf import Interval as EDTFInterval
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from marshmallow_utils.fields import TrimmedString
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import (
    CachedMultilayerEDTFValidator,
    validate_date,
    validate_identifier,
)
from oarepo_vocabularies.services.schema import HierarchySchema

from nr_metadata.common.services.records.schema_common import (
    AdditionalTitlesSchema,
    NRCommonMetadataSchema,
)
from nr_metadata.common.services.records.schema_datatypes import (
    NREventSchema,
    NRFundingReferenceSchema,
    NRGeoLocationSchema,
    NRRelatedItemSchema,
    NRSeriesSchema,
    NRSubjectSchema,
)
from nr_metadata.schema.identifiers import (
    NRObjectIdentifierSchema,
    NRSystemIdentifierSchema,
)


class NRDataRecordSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDataMetadataSchema())


class NRDataMetadataSchema(NRCommonMetadataSchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesSchema())
    )

    dateCollected = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    dateCreated = TrimmedString(
        validate=[CachedMultilayerEDTFValidator(types=(EDTFInterval,))]
    )

    dateValidTo = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    dateWithdrawn = ma_fields.Nested(lambda: DateWithdrawnSchema())

    events = ma_fields.List(ma_fields.Nested(lambda: NREventSchema()))

    fundingReferences = ma_fields.List(
        ma_fields.Nested(lambda: NRFundingReferenceSchema())
    )

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationSchema()))

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(
            lambda: NRObjectIdentifierSchema(),
            validate=[lambda value: validate_identifier(value)],
        )
    )

    publishers = ma_fields.List(
        ma_fields.Nested(lambda: PublishersItemSchema()),
        validate=[ma.validate.Length(min=1)],
    )

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: NRRelatedItemSchema()))

    series = ma_fields.List(ma_fields.Nested(lambda: NRSeriesSchema()))

    subjects = ma_fields.List(ma_fields.Nested(lambda: NRSubjectSchema()))

    systemIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRSystemIdentifierSchema())
    )


class DateWithdrawnSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateInformation = ma_fields.String()

    type = ma_fields.String(validate=[validate_date("%Y-%m-%d")])


class PublishersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchySchema())

    ror = ma_fields.String()

    title = i18n_strings
