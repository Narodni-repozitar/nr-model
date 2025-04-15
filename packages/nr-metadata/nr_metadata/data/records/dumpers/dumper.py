from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from nr_metadata.data.records.dumpers.edtf import DataEDTFIntervalDumperExt
from nr_metadata.data.records.dumpers.multilingual import MultilingualSearchDumperExt


class DataDumper(SearchDumper):
    """DataRecord opensearch dumper."""

    extensions = [
        SystemFieldDumperExt(),
        MultilingualSearchDumperExt(),
        DataEDTFIntervalDumperExt(),
    ]
