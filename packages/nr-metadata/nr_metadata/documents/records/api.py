from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.api import Record as InvenioRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_runtime.records.relations import PIDRelation, RelationsField
from oarepo_runtime.records.systemfields import (
    FilteredSelector,
    FirstItemSelector,
    MultiSelector,
    PathSelector,
    SyntheticSystemField,
)
from oarepo_vocabularies.records.api import Vocabulary

from nr_metadata.documents.records.dumpers.dumper import DocumentsDumper
from nr_metadata.documents.records.models import DocumentsMetadata
from nr_metadata.records.synthetic_fields import KeywordsFieldSelector


class DocumentsIdProvider(RecordIdProviderV2):
    pid_type = "dcmnts"


class DocumentsRecord(InvenioRecord):

    model_cls = DocumentsMetadata

    schema = ConstantField("$schema", "local://documents-1.0.0.json")

    index = IndexField(
        "documents-documents-1.0.0",
    )

    pid = PIDField(
        provider=DocumentsIdProvider, context_cls=PIDFieldContext, create=True
    )

    dumper = DocumentsDumper()

    people = SyntheticSystemField(
        PathSelector("metadata.creators", "metadata.contributors"),
        filter=lambda x: x.get("nameType") == "Personal",
        map=lambda x: x.get("fullName"),
        key="syntheticFields.people",
    )

    organizations = SyntheticSystemField(
        MultiSelector(
            FilteredSelector(
                PathSelector("metadata.creators", "metadata.contributors"),
                filter=lambda x: x["nameType"] == "Personal",
                projection="affiliations.title.cs",
            ),
            FilteredSelector(
                PathSelector("metadata.creators", "metadata.contributors"),
                filter=lambda x: x["nameType"] == "Organizational",
                projection="fullName",
            ),
        ),
        key="syntheticFields.organizations",
    )

    keywords = SyntheticSystemField(
        selector=KeywordsFieldSelector("metadata.subjects.subject"),
        key="syntheticFields.keywords",
    )

    date = SyntheticSystemField(
        selector=FirstItemSelector("metadata.dateModified", "metadata.dateIssued"),
        key="syntheticFields.date",
    )

    year = SyntheticSystemField(
        selector=FirstItemSelector(
            "metadata.dateIssued", "metadata.thesis.dateDefended"
        ),
        key="syntheticFields.year",
        filter=lambda x: len(x) >= 4,
        map=lambda x: x[:4],
    )

    defenseYear = SyntheticSystemField(
        selector=PathSelector("metadata.thesis.dateDefended"),
        key="syntheticFields.defenseYear",
        filter=lambda x: len(x) >= 4,
        map=lambda x: x[:4],
    )

    relations = RelationsField(
        accessRights=PIDRelation(
            "metadata.accessRights",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("access-rights"),
        ),
        affiliations=PIDRelation(
            "metadata.contributors.affiliations",
            keys=["id", "title", {"key": "props.ror", "target": "ror"}, "hierarchy"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        contributorType=PIDRelation(
            "metadata.contributors.contributorType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
        ),
        Organizational_contributorType=PIDRelation(
            "metadata.contributors.contributorType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
        ),
        Personal_affiliations=PIDRelation(
            "metadata.creators.affiliations",
            keys=["id", "title", {"key": "props.ror", "target": "ror"}, "hierarchy"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        country=PIDRelation(
            "metadata.events.eventLocation.country",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("countries"),
        ),
        funder=PIDRelation(
            "metadata.fundingReferences.funder",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("funders"),
        ),
        languages=PIDRelation(
            "metadata.languages",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("languages"),
        ),
        itemContributors_Personal_affiliations=PIDRelation(
            "metadata.relatedItems.itemContributors.affiliations",
            keys=["id", "title", {"key": "props.ror", "target": "ror"}, "hierarchy"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        Personal_contributorType=PIDRelation(
            "metadata.relatedItems.itemContributors.contributorType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
        ),
        itemContributors_Organizational_contributorType=PIDRelation(
            "metadata.relatedItems.itemContributors.contributorType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
        ),
        itemCreators_Personal_affiliations=PIDRelation(
            "metadata.relatedItems.itemCreators.affiliations",
            keys=["id", "title", {"key": "props.ror", "target": "ror"}, "hierarchy"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
        itemRelationType=PIDRelation(
            "metadata.relatedItems.itemRelationType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("item-relation-types"),
        ),
        itemResourceType=PIDRelation(
            "metadata.relatedItems.itemResourceType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("resource-types"),
        ),
        resourceType=PIDRelation(
            "metadata.resourceType",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("resource-types"),
        ),
        rights=PIDRelation(
            "metadata.rights",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("rights"),
        ),
        subjectCategories=PIDRelation(
            "metadata.subjectCategories",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("subject-categories"),
        ),
        degreeGrantors=PIDRelation(
            "metadata.thesis.degreeGrantors",
            keys=["id", "title", "hierarchy"],
            pid_field=Vocabulary.pid.with_type_ctx("institutions"),
        ),
    )
