from invenio_records.dumpers import SearchDumperExt


class SyntheticFieldsDumperExtension(SearchDumperExt):
    paths = []

    def dump(self, record, data):
        """Dump the data."""
        data["syntheticFields"] = {}

        metadata = data.get("metadata", {})

        # Person synthetic field.
        person = []
        for item in metadata.get("contributors", []):
            person.append(item["fullName"])

        for item in metadata.get("creators", []):
            person.append(item["fullName"])

        data["syntheticFields"]["person"] = person

        # Institutions synthetic field.
        institutions = []
        for item in metadata.get("creators", []):
            if "affiliations" in item:
                institutions.extend(item["affiliations"])

        for item in metadata.get("contributors", []):
            if "affiliations" in item:
                institutions.extend(item["affiliations"])

        institutions.extend(metadata.get("thesis", {}).get("degreeGrantors", []))

        data["syntheticFields"]["institutions"] = institutions

        # Keywords synthetic fields. Note: called subjects in metadata.
        (
            data["syntheticFields"]["keywords_cs"],
            data["syntheticFields"]["keywords_en"],
        ) = ([], [])
        all_subjects = [
            item
            for subject in metadata.get("subjects", [])
            for item in subject["subject"]
        ]
        for subject in all_subjects:
            if subject["lang"] == "cs":
                data["syntheticFields"]["keywords_cs"].append(subject["value"])

            if subject["lang"] == "en":
                data["syntheticFields"]["keywords_en"].append(subject["value"])

    def load(self, data, record_cls):
        """Load the data.

        Reverse the changes made by the dump method.
        """

        data.pop("syntheticFields", None)
