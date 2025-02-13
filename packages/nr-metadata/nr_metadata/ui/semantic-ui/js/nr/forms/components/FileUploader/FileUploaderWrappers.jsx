import React from "react";
import PropTypes from "prop-types";
import { i18next } from "@translations/nr/i18next";
import FileManagementDialog from "@oarepo/file-manager";

export const FileUploadWrapper = ({
  uploadWrapperClassName,
  uploadButtonClassName,
  props,
}) => {
  const TriggerComponent = ({ onClick, ...props }) => (
    <button
      className={uploadButtonClassName}
      onClick={onClick}
      type="button"
      aria-label={i18next.t("Upload files")}
      {...props}
    >
      {i18next.t("Upload files")}
      <i aria-hidden="true" className="upload icon" />
    </button>
  );

  return (
    <div className={uploadWrapperClassName}>
      <FileManagementDialog TriggerComponent={TriggerComponent} {...props} />
    </div>
  );
};

FileUploadWrapper.propTypes = {
  uploadWrapperClassName: PropTypes.string,
  uploadButtonClassName: PropTypes.string,
  props: PropTypes.object,
};

FileUploadWrapper.defaultProps = {
  uploadWrapperClassName: "ui container centered",
  uploadButtonClassName: "ui button icon left labeled files-upload-button",
};

export const FileEditWrapper = ({
  editWrapperClassName,
  editButtonClassName,
  props,
}) => {
  const TriggerComponent = ({ onClick, ...props }) => {
    return (
      <button
        className={editButtonClassName}
        onClick={onClick}
        {...props}
        aria-label={i18next.t("Edit file")}
        type="button"
      >
        <i
          aria-hidden="true"
          className="pencil icon"
          style={{ margin: "0", opacity: "1" }}
        />
      </button>
    );
  };

  return (
    <div className={editWrapperClassName}>
      <FileManagementDialog TriggerComponent={TriggerComponent} {...props} />
    </div>
  );
};

FileEditWrapper.propTypes = {
  editWrapperClassName: PropTypes.string,
  editButtonClassName: PropTypes.string,
  props: PropTypes.object,
};

FileEditWrapper.defaultProps = {
  // editWrapperClassName: "ui container centered",
  editButtonClassName: "ui button transparent",
};
