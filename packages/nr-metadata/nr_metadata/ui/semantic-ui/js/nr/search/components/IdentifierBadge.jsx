import React from "react";
import { i18next } from "@translations/nr/i18next";
import PropTypes from "prop-types";

export const IconIdentifier = ({ link, badgeTitle, icon, alt }) => {
  return link ? (
    <a
      className="no-text-decoration mr-0"
      href={link}
      aria-label={badgeTitle}
      title={badgeTitle}
      key={link}
      target="_blank"
      rel="noopener noreferrer"
    >
      <img className="inline-id-icon identifier-badge" src={icon} alt={alt} />
    </a>
  ) : (
    <img
      title={badgeTitle}
      className="inline-id-icon identifier-badge"
      src={icon}
      alt={alt}
    />
  );
};

IconIdentifier.propTypes = {
  link: PropTypes.string,
  badgeTitle: PropTypes.string,
  icon: PropTypes.string,
  alt: PropTypes.string,
};

export const IdentifierBadge = ({ identifier, creatibutorName }) => {
  if (!identifier) return null;

  const { scheme, identifier: value } = identifier;

  switch (scheme.toLowerCase()) {
    case "orcid":
      return (
        <IconIdentifier
          link={`https://orcid.org/${value}`}
          badgeTitle={`${creatibutorName}: ${i18next.t("ORCID profile")}`}
          icon="/static/images/identifiers/ORCID-iD_icon-vector.svg"
          alt="ORCID logo"
        />
      );
    case "scopusid":
      return (
        <IconIdentifier
          link={`https://www.scopus.com/authid/detail.uri?authorId=${value}`}
          badgeTitle={`${creatibutorName}: ${i18next.t("Scopus ID profile")}`}
          icon="/static/images/identifiers/id.png"
          alt="ScopusID logo"
        />
      );
    case "ror":
      return (
        <IconIdentifier
          link={`https://ror.org/${value}`}
          badgeTitle={`${creatibutorName}: ${i18next.t("ROR profile")}`}
          icon="/static/images/identifiers/ror-icon-rgb.svg"
          alt="ROR logo"
        />
      );
    case "researcherid":
      return (
        <IconIdentifier
          link={`https://www.webofscience.com/wos/author/record/${value}`}
          badgeTitle={`${creatibutorName}: ${i18next.t("WOS Researcher ID")}`}
          icon="/static/images/identifiers/id.png"
          alt="WOS Researcher ID logo"
        />
      );
    case "isni":
      return (
        <IconIdentifier
          link={`https://isni.org/isni/${value}`}
          badgeTitle={`${creatibutorName}: ${i18next.t("ISNI profile")}`}
          icon="/static/images/identifiers/id.png"
          alt="ISNI logo"
        />
      );
    case "doi":
      return (
        <IconIdentifier
          link={`https://doi.org/{value}`}
          badgeTitle={`${creatibutorName}: ${i18next.t("DOI profile")}`}
          icon="/static/images/identifiers/DOI_logo.svg"
          alt="DOI logo"
        />
      );
    case "gnd":
      return (
        <IconIdentifier
          link={`https://d-nb.info/gnd/${value}`}
          badgeTitle={`${creatibutorName}: ${i18next.t("GND profile")}`}
          icon="/static/images/identifiers/id.png"
          alt="GND logo"
        />
      );
    case "czenasautid":
      return (
        <IconIdentifier
          link={null}
          badgeTitle={`${scheme} ${value}`}
          icon="/static/images/identifiers/id.png"
          alt="CZENAS logo"
        />
      );
    case "vedidk":
      return (
        <IconIdentifier
          link={null}
          badgeTitle={`${scheme} ${value}`}
          icon="/static/images/identifiers/id.png"
          alt="VEDIDK logo"
        />
      );
    case "institutionalid":
      return (
        <IconIdentifier
          link={null}
          badgeTitle={`${scheme} ${value}`}
          icon="/static/images/identifiers/id.png"
          alt="Institutional ID logo"
        />
      );
    case "ico":
      return (
        <IconIdentifier
          link={null}
          badgeTitle={`${scheme} ${value}`}
          icon="/static/images/identifiers/id.png"
          alt="ICO logo"
        />
      );
    default:
      return null;
  }
};

IdentifierBadge.propTypes = {
  identifier: PropTypes.shape({
    scheme: PropTypes.string,
    identifier: PropTypes.string,
  }),
  creatibutorName: PropTypes.string,
};
