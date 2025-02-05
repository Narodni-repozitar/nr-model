import marshmallow as ma
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as InvenioParentSchema,
)
from marshmallow import Schema
from marshmallow import fields as ma_fields
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema
from oarepo_runtime.services.schema.rdm import RDMRecordMixin

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


class GeneratedParentSchema(InvenioParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class DataCiteRecordSchema(BaseRecordSchema, RDMRecordMixin):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: NRDataCiteMetadataSchema())
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
