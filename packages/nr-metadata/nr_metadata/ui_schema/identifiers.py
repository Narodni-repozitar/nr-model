import marshmallow as ma
from idutils import to_url
from marshmallow import validate


class NRIdentifierUISchema(ma.Schema):
    scheme = ma.fields.String(
        required=True,
    )
    identifier = ma.fields.String(required=True)

    @ma.post_dump
    def add_url(self, value, **kwargs):
        if "identifier" in value and "scheme" in value:
            url = to_url(
                value["identifier"], value["scheme"].lower(), url_scheme="https"
            )
            if url:
                value["url"] = url
        return value


class NRObjectIdentifierUISchema(NRIdentifierUISchema):
    scheme = ma.fields.String(
        required=True,
        validate=[
            validate.OneOf(["DOI", "Handle", "ISBN", "ISSN", "RIV"])
        ],  # RIV is not normalized, others are
    )


class NRAuthorityIdentifierUISchema(NRIdentifierUISchema):
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


class NRSystemIdentifierUISchema(NRIdentifierUISchema):
    scheme = ma.fields.String(
        required=True,
        validate=[
            validate.OneOf(
                ["nusl", "nuslOAI", "originalRecordOAI", "catalogueSysNo", "nrOAI"]
            )
        ],
    )


class NROrganizationIdentifierUISchema(NRIdentifierUISchema):
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


class NRPersonIdentifierUISchema(NRIdentifierUISchema):
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
