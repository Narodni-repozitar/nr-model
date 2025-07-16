from oarepo_runtime.records.dumpers.multilingual_dumper import MultilingualDumper


class MultilingualSearchDumperExt(MultilingualDumper):
    """Multilingual search dumper."""

    paths = [
        "metadata/abstract",
        "metadata/accessibility",
        "metadata/additionalTitles/title",
        "metadata/methods",
        "metadata/subjects/subject",
        "metadata/technicalInfo",
    ]
    SUPPORTED_LANGS = ["cs", "en"]

    def dump(self, record, data):
        super().dump(record, data)

    def load(self, record, data):
        super().load(record, data)
