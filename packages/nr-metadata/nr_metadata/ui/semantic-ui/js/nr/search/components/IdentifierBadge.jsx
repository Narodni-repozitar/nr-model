import React from "react";
import PropTypes from "prop-types";
import { Image } from "react-invenio-forms";

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
      <Image
        className="inline-id-icon identifier-badge"
        src={icon}
        alt={alt}
        fallbackSrc={"/static/images/identifiers/id.svg"}
      />
    </a>
  ) : (
    <Image
      title={badgeTitle}
      className="inline-id-icon identifier-badge"
      src={icon}
      alt={alt}
      fallbackSrc={"/static/images/identifiers/id.svg"}
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

  const lowerCaseScheme = scheme.toLowerCase();

  return (
    <IconIdentifier
      link={url}
      badgeTitle={badgeTitle}
      icon={`/static/images/identifiers/${lowerCaseScheme}.svg`}
      alt="ORCID logo"
    />
  );
};

IdentifierBadge.propTypes = {
  identifier: PropTypes.shape({
    scheme: PropTypes.string,
    identifier: PropTypes.string,
    url: PropTypes.string,
  }),
  creatibutorName: PropTypes.string,
};
