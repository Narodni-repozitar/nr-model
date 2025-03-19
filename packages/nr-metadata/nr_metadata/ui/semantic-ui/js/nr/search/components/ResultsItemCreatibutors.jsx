import React from "react";
import { List } from "semantic-ui-react";
import { DoubleSeparator } from "./DoubleSeparator";
import { IdentifierBadge } from "@js/oarepo_ui/components";
import { SearchFacetLink } from "./SearchFacetLink";
import { i18next } from "@translations/nr/i18next";
import PropTypes from "prop-types";

const CreatibutorSearchLink = ({
  personName = "No name",
  searchField = "creators",
  searchUrl = "/",
  nameType,
}) => (
  <SearchFacetLink
    searchUrl={searchUrl}
    searchFacet={
      nameType === "personal"
        ? "syntheticFields_people"
        : "syntheticFields_organizations"
    }
    value={personName}
    className={`${searchField}-link`}
    title={
      nameType === "Personal"
        ? i18next.t("Find more records by this person")
        : i18next.t("Find more records by this organization")
    }
    label={personName}
  />
);

CreatibutorSearchLink.propTypes = {
  personName: PropTypes.string,
  searchField: PropTypes.string,
  searchUrl: PropTypes.string,
  nameType: PropTypes.string,
};

CreatibutorSearchLink.defaultProps = {
  nameType: "personal",
};

export const CreatibutorIdentifier = ({
  identifiers = [],
  creatibutorName = "No name",
}) => {
  if (identifiers.length === 0) {
    return null;
  }

  const selectedIdentifier =
    identifiers.find(
      (identifier) =>
        identifier.scheme.toLowerCase() === "orcid" ||
        identifier.scheme.toLowerCase() === "ror"
    ) || identifiers[0];

  return (
    <IdentifierBadge
      identifier={selectedIdentifier}
      creatibutorName={creatibutorName}
    />
  );
};

CreatibutorIdentifier.propTypes = {
  creatibutorName: PropTypes.string,
  identifiers: PropTypes.array,
};

export function ResultsItemCreatibutors({
  creators = [],
  contributors = [],
  maxCreators = 3,
  maxContributors = 3,
  searchUrl,
  className,
}) {
  return (
    <>
      <List horizontal className="separated creators inline">
        {creators
          .slice(0, maxCreators)
          .map(({ person_or_org: { name, identifiers, type } }) => (
            <List.Item
              as="span"
              className={`creatibutor-wrap separated ${className}`}
              key={name}
            >
              <CreatibutorSearchLink
                personName={name}
                searchUrl={searchUrl}
                nameType={type}
              />
              <CreatibutorIdentifier
                creatibutorName={name}
                identifiers={identifiers}
              />
            </List.Item>
          ))}
      </List>
      {contributors.length > 0 && <DoubleSeparator />}
      <List horizontal className="separated contributors inline">
        {contributors
          .slice(0, maxContributors)
          .map(
            ({ role, person_or_org: { name, identifiers, type } }, index) => (
              <List.Item
                as="span"
                className={`creatibutor-wrap separated ${className}`}
                key={`${name}-${index}`}
              >
                <CreatibutorSearchLink
                  personName={name}
                  searchUrl={searchUrl}
                  searchField="contributors"
                />
                <CreatibutorIdentifier
                  creatibutorName={name}
                  identifiers={identifiers}
                />
                {role?.title && (
                  <span className="contributor-role">({role?.title})</span>
                )}
              </List.Item>
            )
          )}
      </List>
    </>
  );
}

ResultsItemCreatibutors.propTypes = {
  creators: PropTypes.array,
  contributors: PropTypes.array,
  maxCreators: PropTypes.number,
  maxContributors: PropTypes.number,
  searchUrl: PropTypes.string,
  className: PropTypes.string,
};
