import React from "react";
import PropTypes from "prop-types";

export const ResultsItemAccessStatus = ({ status }) => {
  const { id } = status;

  return id && <i className={`ui access-status ${id}`} />;
};

ResultsItemAccessStatus.propTypes = {
  status: PropTypes.shape({
    id: PropTypes.string.isRequired,
    title_l10n: PropTypes.string.isRequired,
  }),
};
