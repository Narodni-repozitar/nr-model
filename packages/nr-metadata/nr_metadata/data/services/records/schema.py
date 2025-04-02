import marshmallow as ma
from edtf import Interval as EDTFInterval
from invenio_rdm_records.services.schemas.access import AccessSchema
from invenio_rdm_records.services.schemas.metadata import CreatorSchema
from invenio_rdm_records.services.schemas.pids import PIDSchema
from invenio_rdm_records.services.schemas.record import validate_scheme
from invenio_vocabularies.services.schema import i18n_strings
from marshmallow import fields as ma_fields
from marshmallow.fields import Dict, Nested, String
from marshmallow_utils.fields import SanitizedUnicode, TrimmedString
from marshmallow_utils.fields.nestedattr import NestedAttribute
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
from oarepo_vocabularies.services.schema import HierarchySchema
from oarepo_workflows.services.records.schema import RDMWorkflowParentSchema

from nr_metadata.common.services.records.schema_common import (
    AdditionalTitlesSchema,
    NRCommonMetadataSchema,
)
from nr_metadata.common.services.records.schema_datatypes import (
    NREventSchema,
    NRGeoLocationSchema,
    NRRelatedItemSchema,
    NRSeriesSchema,
    NRSubjectSchema,
)
from nr_metadata.schema.identifiers import (
    NRObjectIdentifierSchema,
    NRSystemIdentifierSchema,
)


class GeneratedParentSchema(RDMWorkflowParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class NRDataRecordSchema(RDMBaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    access = NestedAttribute(lambda: AccessSchema())

    metadata = ma_fields.Nested(lambda: NRDataMetadataSchema())

    pids = Dict(
        keys=SanitizedUnicode(validate=validate_scheme),
        values=Nested(PIDSchema),
    )

    state = ma_fields.String(dump_only=True)

    state_timestamp = ma_fields.String(dump_only=True, validate=[validate_datetime])
    parent = ma.fields.Nested(GeneratedParentSchema)


class NRDataMetadataSchema(NRCommonMetadataSchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesSchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: CreatorSchema()))

    creators = ma_fields.List(
        ma_fields.Nested(lambda: CreatorSchema()),
        required=True,
        validate=[ma.validate.Length(min=1)],
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

    funders = ma_fields.List(ma_fields.Nested(lambda: FundingSchema()))

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
