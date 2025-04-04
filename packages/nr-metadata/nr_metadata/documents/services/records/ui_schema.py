import marshmallow as ma
from marshmallow import fields as ma_fields
from marshmallow.fields import String
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.rdm_ui import (
    RDMCreatorsUISchema,
    RDMFundersUISchema,
)
from oarepo_runtime.services.schema.ui import (
    InvenioRDMUISchema,
    LocalizedDateTime,
    LocalizedEDTF,
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
    NRExternalLocationUISchema,
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
from nr_metadata.ui_schema.versions import FillMissingVersionMixin


class NRDocumentRecordUISchema(FillMissingVersionMixin, InvenioRDMUISchema):
    class Meta:
        unknown = ma.RAISE

    deletion_status = ma_fields.String()

    is_deleted = ma_fields.Boolean()

    is_published = ma_fields.Boolean()

    metadata = ma_fields.Nested(lambda: NRDocumentMetadataUISchema())

    state = ma_fields.String(dump_only=True)

    state_timestamp = LocalizedDateTime(dump_only=True)

    syntheticFields = ma_fields.Nested(lambda: NRDocumentSyntheticFieldsUISchema())

    version_id = ma_fields.Integer()


class NRDocumentMetadataUISchema(NRCommonMetadataUISchema):
    class Meta:
        unknown = ma.RAISE

    additionalTitles = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalTitlesUISchema())
    )

    contributors = ma_fields.List(ma_fields.Nested(lambda: RDMCreatorsUISchema()))

    creators = ma_fields.List(
        ma_fields.Nested(lambda: RDMCreatorsUISchema()), required=True
    )

    dateModified = LocalizedEDTF()

    events = ma_fields.List(ma_fields.Nested(lambda: NREventUISchema()))

    externalLocation = ma_fields.Nested(lambda: NRExternalLocationUISchema())

    funders = ma_fields.List(ma_fields.Nested(lambda: RDMFundersUISchema()))

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: NRGeoLocationUISchema()))

    objectIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRObjectIdentifierUISchema())
    )

    publishers = ma_fields.List(ma_fields.String())

    relatedItems = ma_fields.List(ma_fields.Nested(lambda: NRRelatedItemUISchema()))

    series = ma_fields.List(ma_fields.Nested(lambda: NRSeriesUISchema()))

    subjects = NRSubjectListField(ma_fields.Nested(lambda: NRSubjectUISchema()))

    systemIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NRSystemIdentifierUISchema())
    )

    thesis = ma_fields.Nested(lambda: NRThesisUISchema())


class NRThesisUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    dateDefended = LocalizedEDTF()

    defended = ma_fields.Boolean()

    degreeGrantors = ma_fields.List(ma_fields.Nested(lambda: NRDegreeGrantorUISchema()))

    studyFields = ma_fields.List(ma_fields.String())


class KeywordsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE


class NRDegreeGrantorUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.INCLUDE

    _id = String(data_key="id", attribute="id")

    _version = String(data_key="@v", attribute="@v")

    hierarchy = ma_fields.Nested(lambda: HierarchyUISchema())

    title = VocabularyI18nStrUIField()


class NRDocumentSyntheticFieldsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    date = LocalizedEDTF()

    organizations = ma_fields.String()

    people = ma_fields.String()
