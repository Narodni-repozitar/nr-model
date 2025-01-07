from oarepo_runtime.records.dumpers import SearchDumper

from nr_metadata.datacite.records.dumpers.edtf import DataciteEDTFIntervalDumperExt
from nr_metadata.datacite.records.dumpers.multilingual import (
    MultilingualSearchDumperExt,
)


class DataciteDumper(SearchDumper):
    """DataciteRecord opensearch dumper."""

    extensions = [DataciteEDTFIntervalDumperExt(), MultilingualSearchDumperExt()]
