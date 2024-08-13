from oarepo_runtime.records.dumpers import SearchDumper

from nr_metadata.common.records.dumpers.edtf import CommonEDTFIntervalDumperExt
from nr_metadata.common.records.dumpers.multilingual import MultilingualSearchDumperExt


class CommonDumper(SearchDumper):
    """CommonRecord opensearch dumper."""

    extensions = [CommonEDTFIntervalDumperExt(), MultilingualSearchDumperExt()]
