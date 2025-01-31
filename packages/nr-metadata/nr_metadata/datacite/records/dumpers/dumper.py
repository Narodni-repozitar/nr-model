from oarepo_runtime.records.dumpers import SearchDumper
from oarepo_runtime.records.systemfields.mapping import SystemFieldDumperExt

from nr_metadata.datacite.records.dumpers.edtf import DataciteEDTFIntervalDumperExt
from nr_metadata.datacite.records.dumpers.multilingual import (
    MultilingualSearchDumperExt,
)


class DataciteDumper(SearchDumper):
    """DataciteRecord opensearch dumper."""

    extensions = [
        SystemFieldDumperExt(),
        MultilingualSearchDumperExt(),
        DataciteEDTFIntervalDumperExt(),
    ]
