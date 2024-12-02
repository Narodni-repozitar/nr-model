import React from "react";
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

  const { scheme, identifier: identifierValue, url } = identifier;

  const badgeTitle = `${creatibutorName} ${scheme}: ${identifierValue}`;

  switch (scheme.toLowerCase()) {
    case "orcid":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/ORCID-iD_icon-vector.svg"
          alt="ORCID logo"
        />
      );
    case "scopusid":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/id.png"
          alt="ScopusID logo"
        />
      );
    case "ror":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/ror-icon-rgb.svg"
          alt="ROR logo"
        />
      );
    case "researcherid":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/id.png"
          alt="WOS Researcher ID logo"
        />
      );
    case "isni":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/id.png"
          alt="ISNI logo"
        />
      );
    case "doi":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/DOI_logo.svg"
          alt="DOI logo"
        />
      );
    case "gnd":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/id.png"
          alt="GND logo"
        />
      );
    case "czenasautid":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/id.png"
          alt="CZENAS logo"
        />
      );
    case "vedidk":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/id.png"
          alt="VEDIDK logo"
        />
      );
    case "institutionalid":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
          icon="/static/images/identifiers/id.png"
          alt="Institutional ID logo"
        />
      );
    case "ico":
      return (
        <IconIdentifier
          link={url}
          badgeTitle={badgeTitle}
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
