from invenio_drafts_resources.records.api import DraftRecordIdProviderV2
from invenio_drafts_resources.services.records.components.media_files import (
    MediaFilesAttrConfig,
)
from invenio_rdm_records.records.api import RDMMediaFileRecord, RDMParent, RDMRecord
from invenio_records.systemfields import ConstantField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_runtime.records.pid_providers import UniversalPIDMixin
from oarepo_workflows.records.systemfields.state import (
    RecordStateField,
    RecordStateTimestampField,
)
from oarepo_workflows.records.systemfields.workflow import WorkflowField

from nr_metadata.datacite.records.dumpers.dumper import DataciteDumper
from nr_metadata.datacite.records.models import DataciteMetadata, DataciteParentMetadata


class DataciteParentRecord(RDMParent):
    model_cls = DataciteParentMetadata

    workflow = WorkflowField()


class DataciteIdProvider(UniversalPIDMixin, DraftRecordIdProviderV2):
    pid_type = "dtct"


class DataciteRecord(RDMRecord):

    model_cls = DataciteMetadata

    schema = ConstantField("$schema", "local://datacite-1.0.0.json")

    index = IndexField(
        "datacite-datacite-1.0.0",
    )

    pid = PIDField(
        provider=DataciteIdProvider, context_cls=PIDFieldContext, create=True
    )

    dumper = DataciteDumper()

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


class RDMRecordMediaFiles(DataciteRecord):
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
