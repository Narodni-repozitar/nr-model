from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from nr_metadata.common.records.dumpers.edtf import CommonEDTFIntervalDumperExt
from nr_metadata.common.records.dumpers.multilingual import MultilingualSearchDumperExt


class CommonDumper(SearchDumper):
    """CommonRecord opensearch dumper."""

    extensions = [
        SystemFieldDumperExt(),
        MultilingualSearchDumperExt(),
        CommonEDTFIntervalDumperExt(),
    ]
