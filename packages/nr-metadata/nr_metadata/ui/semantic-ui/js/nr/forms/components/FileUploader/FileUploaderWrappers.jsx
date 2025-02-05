import React from "react";
import PropTypes from "prop-types";
import { i18next } from "@translations/nr/i18next";
import FileManagementDialog from "@oarepo/file-manager";

export const FileUploadWrapper = ({
  uploadWrapperClassName,
  uploadButtonClassName,
  lockFileUploader,
  props,
}) => {
  const TriggerComponent = ({ onClick, ...props }) => (
    <button
      className={uploadButtonClassName}
      onClick={onClick}
      type="button"
      aria-label={i18next.t("Upload files")}
      disabled={lockFileUploader}
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
  lockFileUploader: PropTypes.bool.isRequired,
};

FileUploadWrapper.defaultProps = {
  uploadWrapperClassName: "ui container centered",
  uploadButtonClassName: "ui button icon left labeled files-upload-button",
};

export const FileEditWrapper = ({
  editWrapperClassName,
  editButtonClassName,
  lockFileUploader,
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
        disabled={lockFileUploader}
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
  lockFileUploader: PropTypes.bool.isRequired,
};

FileEditWrapper.defaultProps = {
  // editWrapperClassName: "ui container centered",
  editButtonClassName: "ui button transparent",
};
