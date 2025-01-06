from oarepo_runtime.records.dumpers import SearchDumper

from nr_metadata.data.records.dumpers.edtf import DataEDTFIntervalDumperExt
from nr_metadata.data.records.dumpers.multilingual import MultilingualSearchDumperExt


class DataDumper(SearchDumper):
    """DataRecord opensearch dumper."""

    extensions = [DataEDTFIntervalDumperExt(), MultilingualSearchDumperExt()]
