from invenio_db import db
from invenio_drafts_resources.records import ParentRecordMixin
from invenio_files_rest.models import Bucket
from invenio_rdm_records.records.systemfields.deletion_status import (
    RecordDeletionStatusEnum,
)
from invenio_records.models import RecordMetadataBase
from oarepo_workflows.records.models import RecordWorkflowParentModelMixin
from sqlalchemy_utils.types import ChoiceType, UUIDType


class DocumentsParentMetadata(
    RecordWorkflowParentModelMixin, db.Model, RecordMetadataBase
):

    __tablename__ = "nr_metadata.documents_parent_record_metadata"


class DocumentsMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for DocumentsRecord metadata."""

    __tablename__ = "documents_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = DocumentsParentMetadata

    deletion_status = db.Column(
        ChoiceType(RecordDeletionStatusEnum, impl=db.String(1)),
        nullable=False,
        default=RecordDeletionStatusEnum.PUBLISHED.value,
    )

    media_bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id), index=True)
    media_bucket = db.relationship(Bucket, foreign_keys=[media_bucket_id])
