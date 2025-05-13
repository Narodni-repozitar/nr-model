from invenio_drafts_resources.records.api import DraftRecordIdProviderV2
from invenio_drafts_resources.services.records.components.media_files import (
    MediaFilesAttrConfig,
)
from invenio_rdm_records.records.api import RDMMediaFileRecord, RDMParent, RDMRecord
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from invenio_vocabularies.contrib.affiliations.api import Affiliation
from invenio_vocabularies.contrib.awards.api import Award
from invenio_vocabularies.contrib.funders.api import Funder
from oarepo_runtime.records.pid_providers import UniversalPIDMixin
from oarepo_runtime.records.relations import (
    PIDRelation,
    RelationsField,
    UnstrictPIDRelation,
)
from oarepo_runtime.records.systemfields import (
    FilteredSelector,
    FirstItemSelector,
    MultiSelector,
    PathSelector,
    SyntheticSystemField,
)
from oarepo_vocabularies.records.api import Vocabulary
from oarepo_workflows.records.systemfields.state import (
    RecordStateField,
    RecordStateTimestampField,
)
from oarepo_workflows.records.systemfields.workflow import WorkflowField

from nr_metadata.documents.records.dumpers.dumper import DocumentsDumper
from nr_metadata.documents.records.models import (
    DocumentsMetadata,
    DocumentsParentMetadata,
)
from nr_metadata.records.synthetic_fields import KeywordsFieldSelector


class DocumentsParentRecord(RDMParent):
    model_cls = DocumentsParentMetadata

    workflow = WorkflowField()


class DocumentsIdProvider(UniversalPIDMixin, DraftRecordIdProviderV2):
    pid_type = "dcmnts"


class DocumentsRecord(RDMRecord):

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
        PathSelector(
            "metadata.creators.person_or_org", "metadata.contributors.person_or_org"
        ),
        filter=lambda x: x.get("type") == "personal",
        map=lambda x: x.get("name"),
        key="syntheticFields.people",
    )

    organizations = SyntheticSystemField(
        MultiSelector(
            FilteredSelector(
                PathSelector(
                    "metadata.creators.person_or_org",
                    "metadata.contributors.person_or_org",
                ),
                filter=lambda x: x["type"] == "personal",
                projection="affiliations.title.cs",
            ),
            FilteredSelector(
                PathSelector(
                    "metadata.creators.person_or_org",
                    "metadata.contributors.person_or_org",
                ),
                filter=lambda x: x["type"] == "organizational",
                projection="name",
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

    state = RecordStateField(initial="published")

    state_timestamp = RecordStateTimestampField()

    media_files = FilesField(
        key=MediaFilesAttrConfig["_files_attr_key"],
        bucket_id_attr=MediaFilesAttrConfig["_files_bucket_id_attr_key"],
        bucket_attr=MediaFilesAttrConfig["_files_bucket_attr_key"],
        store=False,
        dump=False,
        file_cls=RDMMediaFileRecord,
        create=False,
        delete=False,
    )

    relations = RelationsField(
        affiliations=UnstrictPIDRelation(
            "metadata.contributors.affiliations",
            keys=["name", "id"],
            pid_field=Affiliation.pid,
        ),
        role=PIDRelation(
            "metadata.contributors.role",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
        ),
        creators_affiliations=UnstrictPIDRelation(
            "metadata.creators.affiliations",
            keys=["name", "id"],
            pid_field=Affiliation.pid,
        ),
        creators_role=PIDRelation(
            "metadata.creators.role",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
        ),
        country=PIDRelation(
            "metadata.events.eventLocation.country",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("countries"),
        ),
        award=UnstrictPIDRelation(
            "metadata.funders.award",
            keys=[
                "title",
                "id",
                "number",
                "program",
                "acronym",
                "identifiers",
                "subjects",
                "organizations",
                "@v",
            ],
            pid_field=Award.pid,
        ),
        funder=UnstrictPIDRelation(
            "metadata.funders.funder",
            keys=["id", "@v", "name", "title"],
            pid_field=Funder.pid,
        ),
        languages=PIDRelation(
            "metadata.languages",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("languages"),
        ),
        itemContributors_affiliations=UnstrictPIDRelation(
            "metadata.relatedItems.itemContributors.affiliations",
            keys=["name", "id"],
            pid_field=Affiliation.pid,
        ),
        itemContributors_role=PIDRelation(
            "metadata.relatedItems.itemContributors.role",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
        ),
        itemCreators_affiliations=UnstrictPIDRelation(
            "metadata.relatedItems.itemCreators.affiliations",
            keys=["name", "id"],
            pid_field=Affiliation.pid,
        ),
        itemCreators_role=PIDRelation(
            "metadata.relatedItems.itemCreators.role",
            keys=["id", "title"],
            pid_field=Vocabulary.pid.with_type_ctx("contributor-types"),
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
            pid_field=Vocabulary.pid.with_type_ctx("degree-grantors"),
        ),
    )


class RDMRecordMediaFiles(DocumentsRecord):
    """RDM Media file record API."""

    files = FilesField(
        key=MediaFilesAttrConfig["_files_attr_key"],
        bucket_id_attr=MediaFilesAttrConfig["_files_bucket_id_attr_key"],
        bucket_attr=MediaFilesAttrConfig["_files_bucket_attr_key"],
        store=False,
        dump=False,
        file_cls=RDMMediaFileRecord,
        # Don't create
        create=False,
        # Don't delete, we'll manage in the service
        delete=False,
    )


RDMMediaFileRecord.record_cls = RDMRecordMediaFiles
