from invenio_db import db
from invenio_drafts_resources.records import ParentRecordMixin
from invenio_rdm_records.records.systemfields.deletion_status import (
    RecordDeletionStatusEnum,
)
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils.types import ChoiceType


class DataciteParentMetadata(db.Model, RecordMetadataBase):

    __tablename__ = "nr_metadata.datacite_parent_record_metadata"


class DataciteMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for DataciteRecord metadata."""

    __tablename__ = "datacite_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    deletion_status = db.Column(
        ChoiceType(RecordDeletionStatusEnum, impl=db.String(1)),
        nullable=False,
        default=RecordDeletionStatusEnum.PUBLISHED.value,
    )

    __parent_record_model__ = DataciteParentMetadata
