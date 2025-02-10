import React from "react";
import { Image } from "semantic-ui-react";
import PropTypes from "prop-types";

const iconsObject = {
  open: "zamky_open_access.svg",
  restricted: "zamky_Partialy_closed_access.svg",
  embargoed: "zamky_Closed_access.svg",
  "metadata-only": "zamky_Partialy_closed_access.svg",
};

export const ResultsItemAccessStatus = ({ status }) => {
  const { id, title_l10n } = status;
  const iconFile = iconsObject[id] || null;
  return (
    iconFile && (
      <Image
        centered
        fluid
        title={title_l10n}
        aria-label={title_l10n}
        className={`access-status ${title_l10n}`}
        src={`/static/icons/locks/${iconFile}`}
      />
    )
  );
};

ResultsItemAccessStatus.propTypes = {
  status: PropTypes.shape({
    id: PropTypes.string.isRequired,
    title_l10n: PropTypes.string.isRequired,
  }),
};
