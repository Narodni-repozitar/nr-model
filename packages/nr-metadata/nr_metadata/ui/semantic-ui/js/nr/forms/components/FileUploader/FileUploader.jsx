import React, { useState } from "react";
import PropTypes from "prop-types";
import { i18next } from "@translations/nr/i18next";
import { Message, Icon, Button, Dimmer, Loader } from "semantic-ui-react";
import { FileUploaderTable } from "./FileUploaderTable";
import { UploadFileButton } from "./FileUploaderButtons";
import {
  useDepositApiClient,
  useDepositFileApiClient,
  useFormConfig,
  httpApplicationJson,
} from "@js/oarepo_ui";
import { Trans } from "react-i18next";
import { useQuery, useMutation } from "@tanstack/react-query";

export const FileUploader = ({
  fileUploaderMessage,
  record,
  recordFiles,
  allowedFileTypes,
}) => {
  const [filesState, setFilesState] = useState(recordFiles?.entries || []);
  const {
    formConfig: { filesLocked },
  } = useFormConfig();
  const { formik, isSubmitting, save, isSaving } = useDepositApiClient();
  const { read } = useDepositFileApiClient();
  const { values } = formik;
  const recordObject = record || values;

  const isDraftRecord = !recordObject.is_published;

  const lockFileUploader = !isDraftRecord && filesLocked;
  const hasParentRecord =
    recordObject?.versions?.index && recordObject?.versions?.index > 1;

  const displayImportBtn =
    recordObject?.files?.enabled &&
    isDraftRecord &&
    hasParentRecord &&
    !filesState.length;

  const {
    isError: isFileImportError,
    isLoading,
    mutate: importParentFiles,
    reset: resetImportParentFiles,
  } = useMutation({
    mutationFn: () =>
      httpApplicationJson.post(
        recordObject?.links?.self + "/actions/files-import",
        {}
      ),
    onSuccess: (data) => {
      setFilesState(data.data.entries);
      resetImportParentFiles();
    },
  });

  const { isFetching, isError, refetch } = useQuery(
    ["files"],
    () => read(values),
    {
      refetchOnWindowFocus: false,
      enabled: false,
      onSuccess: (data) => {
        setFilesState(data.entries);
        resetImportParentFiles();
      },
    }
  );

  const handleFilesUpload = () => {
    refetch();
  };
  const handleFileDeletion = (fileObject) => {
    setFilesState((prevFilesState) =>
      prevFilesState.filter((file) => file.key !== fileObject.key)
    );
  };

  if (!recordObject.id && recordObject?.files?.enabled) {
    return (
      <Message>
        <Icon name="info circle" className="text size large" />
        <Trans i18next={i18next}>
          <span>If you wish to upload files, you must </span>
          <Button
            className="ml-5 mr-5"
            primary
            onClick={() => save(true)}
            loading={isSaving}
            disabled={isSubmitting}
            size="mini"
          >
            save
          </Button>
          <span> your draft first.</span>
        </Trans>
      </Message>
    );
  }

  if (recordObject.id && recordObject?.files?.enabled) {
    return (
      <Dimmer.Dimmable dimmed={isFetching}>
        <Dimmer active={isFetching || isLoading} inverted>
          <Loader indeterminate>{i18next.t("Fetching files")}...</Loader>
        </Dimmer>
        {isError ? (
          <Message negative>
            {i18next.t(
              "Failed to fetch draft's files. Please try refreshing the page."
            )}
          </Message>
        ) : (
          <React.Fragment>
            {displayImportBtn && (
              <Message className="flex justify-space-between align-items-center">
                <p className="mb-0">
                  <Icon name="info circle" />
                  {i18next.t("You can import files from the previous version.")}
                </p>
                <Button
                  type="button"
                  size="mini"
                  primary
                  onClick={() => importParentFiles()}
                  icon="sync"
                  content={i18next.t("Import files")}
                />
              </Message>
            )}
            {isFileImportError && (
              <Message negative>
                <Message.Content>
                  {i18next.t(
                    "Failed to import files from previous version. Please try again."
                  )}
                </Message.Content>
              </Message>
            )}
            <FileUploaderTable
              files={filesState}
              handleFileDeletion={handleFileDeletion}
              record={recordObject}
              allowedFileTypes={allowedFileTypes}
              lockFileUploader={lockFileUploader}
            />
            {lockFileUploader && (
              <Message className="flex justify-space-between align-items-center">
                <p className="mb-0">
                  <Icon name="info circle" />
                  <Trans i18next={i18next}>
                    You must create a new version to add, modify or delete
                    files. It can be done on record's{" "}
                    <a
                      target="_blank"
                      rel="noopener noreferrer"
                      href={recordObject.links.self_html.replace(
                        "/preview",
                        ""
                      )}
                    >
                      detail
                    </a>{" "}
                    page.
                  </Trans>
                </p>
              </Message>
            )}
            {!lockFileUploader && (
              <UploadFileButton
                record={recordObject}
                handleFilesUpload={handleFilesUpload}
                allowedFileTypes={allowedFileTypes}
                lockFileUploader={lockFileUploader}
              />
            )}
          </React.Fragment>
        )}
        {!recordObject.is_published && (
          <Message
            negative
            className="flex justify-space-between align-items-center"
          >
            <p className="mb-0">
              <Icon name="warning sign" />
              {fileUploaderMessage}
            </p>
          </Message>
        )}
      </Dimmer.Dimmable>
    );
  }

  return null;
};

FileUploader.propTypes = {
  fileUploaderMessage: PropTypes.string,
  record: PropTypes.object,
  recordFiles: PropTypes.object,
  allowedFileTypes: PropTypes.array,
};

FileUploader.defaultProps = {
  fileUploaderMessage: i18next.t(
    "After publishing the draft, it is not possible to add, modify or delete files. It will be necessary to create a new version of the record."
  ),
  allowedFileTypes: ["*/*"],
};
