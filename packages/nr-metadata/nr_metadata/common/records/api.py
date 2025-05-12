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
from oarepo_vocabularies.records.api import Vocabulary
from oarepo_workflows.records.systemfields.state import (
    RecordStateField,
    RecordStateTimestampField,
)
from oarepo_workflows.records.systemfields.workflow import WorkflowField

from nr_metadata.common.records.dumpers.dumper import CommonDumper
from nr_metadata.common.records.models import CommonMetadata, CommonParentMetadata


class CommonParentRecord(RDMParent):
    model_cls = CommonParentMetadata

    workflow = WorkflowField()


class CommonIdProvider(UniversalPIDMixin, DraftRecordIdProviderV2):
    pid_type = "common"


class CommonRecord(RDMRecord):

    model_cls = CommonMetadata

    schema = ConstantField("$schema", "local://common-1.0.0.json")

    index = IndexField(
        "common-common-1.0.0",
    )

    pid = PIDField(provider=CommonIdProvider, context_cls=PIDFieldContext, create=True)

    dumper = CommonDumper()

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
    )


class RDMRecordMediaFiles(CommonRecord):
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
