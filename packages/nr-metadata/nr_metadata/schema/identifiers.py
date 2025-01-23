import marshmallow as ma
from idutils import is_isbn, normalize_pid
from marshmallow import validate
from marshmallow.exceptions import ValidationError


class NRIdentifierSchema(ma.Schema):
    scheme = ma.fields.String(
        required=True,
    )
    identifier = ma.fields.String(required=True)


    @ma.pre_load
    def remove_url(self, value, *args, **kwargs):
        if not value or not isinstance(value, dict):
            return value
        url = value.pop("url", None)
        if url and not value.get("identifier"):
            value["identifier"] = url
        return value


class NRObjectIdentifierSchema(NRIdentifierSchema):
    scheme = ma.fields.String(
        required=True,
        validate=[
            validate.OneOf(["DOI", "Handle", "ISBN", "ISSN", "RIV"])
        ],  # RIV & ISBN are not normalized, others are
    )

    @ma.pre_load
    def validate_only(self, value, *args, **kwargs):
        value = super().remove_url(value, *args, **kwargs)
        if value.get("scheme") == "ISBN":
            # Only validate ISBN, no normalization
            if not is_isbn(value.get("identifier")):
                raise ValidationError("Invalid ISBN")
        return value


class NRAuthorityIdentifierSchema(NRIdentifierSchema):
    scheme = ma.fields.String(
        required=True,
        validate=[
            validate.OneOf(
                [
                    "orcid",  # normalized
                    "scopusID",
                    "researcherID",
                    "czenasAutID",
                    "vedidk",
                    "institutionalID",
                    "ISNI",
                    "ROR",
                    "ICO",
                    "DOI",  # normalized
                ]
            )
        ],
    )


class NRSystemIdentifierSchema(NRIdentifierSchema):
    scheme = ma.fields.String(
        required=True,
        validate=[
            validate.OneOf(
                ["nusl", "nuslOAI", "originalRecordOAI", "catalogueSysNo", "nrOAI"]
            )
        ],
    )

class NROrganizationIdentifierSchema(NRIdentifierSchema):
    scheme = ma.fields.String(
        required=True,
        validate=[
            validate.OneOf(
                [

                    "ISNI",
                    "ROR",
                    "ICO",
                    "DOI",  # normalized
                ]
            )
        ],
    )

class NRPersonIdentifierSchema(NRIdentifierSchema):
    scheme = ma.fields.String(
        required=True,
        validate=[
            validate.OneOf(
                [
                    "orcid",  # normalized
                    "scopusID",
                    "researcherID",
                    "czenasAutID",
                    "vedidk",
                    "institutionalID",
                    "ISNI",

                ]
            )
        ],
    )
