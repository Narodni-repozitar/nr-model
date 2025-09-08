import re

from flask import current_app
import marshmallow as ma
from invenio_access.permissions import system_identity
from invenio_i18n import gettext as _
from invenio_rdm_records.services.schemas.metadata import CreatorSchema
from invenio_records_resources.proxies import current_service_registry

class RDMNTKCreatorsSchema(CreatorSchema):
    """NTK version of RDM creators schema.

    This version makes sure that organizations are selected from the
    list of organizations in the system. Record will not be valid if
    organization is not in the system.
    """
    
    def _is_organization_exception(self, name):
        """Check if organization name is in exceptions list."""
        return name in current_app.config["NTK_ORGANIZATION_EXCEPTIONS"]

    @ma.validates_schema
    def check_organization_or_affiliation(self, data, **kwargs):
        """Check if organization is in the system."""
        person_or_org = data.get("person_or_org", {})
        if person_or_org.get("type") == "personal":
            affiliations = data.get("affiliations", [])
            for affiliation in affiliations:
                if not self.from_vocabulary(affiliation):
                    raise ma.ValidationError(
                        _(
                            "It is necessary to choose organization from the controlled vocabulary. "
                            "To add organization, please go to "
                            "https://nusl.techlib.cz/cs/migrace-nusl/navrh-novych-hesel/"
                        ),
                        field_name="affiliations",
                    )
        else:
            # organization
            name = person_or_org.get("name")
            affiliations = current_service_registry.get("affiliations")
            found = [
                x["name"]
                for x in affiliations.search(
                    system_identity,
                    q=f'name.suggest:"{escape_opensearch_query(name)}"',
                    size=100,
                ).hits
            ]
            if name not in found and not self._is_organization_exception(name):
                raise ma.ValidationError(
                    _(
                        "It is necessary to choose organization from the controlled vocabulary. "
                        "To add organization, please go to "
                        "https://nusl.techlib.cz/cs/migrace-nusl/navrh-novych-hesel/"
                    ),
                    field_name="person_or_org",
                )
        return data

    def from_vocabulary(self, affiliation):
        """Check if affiliation is from the vocabulary."""
        if "id" not in affiliation:
            return False
        return True
    
def escape_opensearch_query(value: str) -> str:
    """
    Escapes special characters in a string for safe use in OpenSearch query syntax.
    """
    # Escape each special character with a backslash
    escaped = re.sub(r'([\\+\-=&|><!(){}\[\]^"~*?:/])', r"\\\1", value)

    return escaped