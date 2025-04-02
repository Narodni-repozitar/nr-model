import marshmallow as ma
from invenio_rdm_records.services.schemas.access import AccessSchema
from invenio_rdm_records.services.schemas.pids import PIDSchema
from invenio_rdm_records.services.schemas.record import validate_scheme
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.fields import Dict, Nested
from marshmallow_utils.fields import SanitizedUnicode
from marshmallow_utils.fields.nestedattr import NestedAttribute
from oarepo_runtime.services.schema.marshmallow import RDMBaseRecordSchema
from oarepo_runtime.services.schema.validation import validate_datetime
from oarepo_workflows.services.records.schema import RDMWorkflowParentSchema

from nr_metadata.datacite.services.records.schema_datatypes import (
    AlternateIdentifierSchema,
    ContainerSchema,
    ContributorSchema,
    CreatorSchema,
    DateSchema,
    DescriptionSchema,
    FundingReferenceSchema,
    GeoLocationSchema,
    PublisherSchema,
    RelatedIdentifierSchema,
    RelatedItemSchema,
    ResourceTypeSchema,
    RightsSchema,
    SubjectSchema,
    TitleSchema,
)


class GeneratedParentSchema(RDMWorkflowParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class DataCiteRecordSchema(RDMBaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    access = NestedAttribute(lambda: AccessSchema())

    metadata = ma_fields.Nested(lambda: NRDataCiteMetadataSchema())

    pids = Dict(
        keys=SanitizedUnicode(validate=validate_scheme),
        values=Nested(PIDSchema),
    )

    state = ma_fields.String(dump_only=True)

    state_timestamp = ma_fields.String(dump_only=True, validate=[validate_datetime])
    parent = ma.fields.Nested(GeneratedParentSchema)


class NRDataCiteMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    alternateIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: AlternateIdentifierSchema())
    )

    container = ma_fields.Nested(lambda: ContainerSchema())

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorSchema()))

    creators = ma_fields.List(ma_fields.Nested(lambda: CreatorSchema()))

    dates = ma_fields.List(ma_fields.Nested(lambda: DateSchema()))

    descriptions = ma_fields.List(ma_fields.Nested(lambda: DescriptionSchema()))

    doi = ma_fields.String()

    formats = ma_fields.List(ma_fields.String())

    fundingReferences = ma_fields.List(
        ma_fields.Nested(lambda: FundingReferenceSchema())
    )

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: GeoLocationSchema()))

    language = ma_fields.String()

    publicationYear = ma_fields.String()

    publisher = ma_fields.Nested(lambda: PublisherSchema())

    relatedIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: RelatedIdentifierSchema())
    )

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: RelatedItemSchema()))

    resourceType = ma_fields.Nested(lambda: ResourceTypeSchema())

    rightsList = ma_fields.List(ma_fields.Nested(lambda: RightsSchema()))

    schemaVersion = ma_fields.String()

    sizes = ma_fields.List(ma_fields.String())

    subjects = ma_fields.List(ma_fields.Nested(lambda: SubjectSchema()))

    titles = ma_fields.List(ma_fields.Nested(lambda: TitleSchema()))

    url = ma_fields.String()

    version = ma_fields.String()
