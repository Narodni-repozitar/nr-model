from oarepo_runtime.records.dumpers import SearchDumper

from nr_metadata.documents.records.dumpers.edtf import DocumentsEDTFIntervalDumperExt
from nr_metadata.documents.records.dumpers.multilingual import (
    MultilingualSearchDumperExt,
)


class DocumentsDumper(SearchDumper):
    """DocumentsRecord opensearch dumper."""

    extensions = [DocumentsEDTFIntervalDumperExt(), MultilingualSearchDumperExt()]
