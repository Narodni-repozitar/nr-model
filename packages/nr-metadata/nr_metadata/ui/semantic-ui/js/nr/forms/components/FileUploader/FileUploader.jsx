import React, { useState } from "react";
import PropTypes from "prop-types";
import { i18next } from "@translations/nr/i18next";
import { Message, Icon, Button, Dimmer, Loader } from "semantic-ui-react";
import { FileUploaderTable } from "./FileUploaderTable";
import { UploadFileButton } from "./FileUploaderButtons";
import { useDepositApiClient, useDepositFileApiClient } from "@js/oarepo_ui";
import { Trans } from "react-i18next";
import { useQuery, useMutation } from "@tanstack/react-query";
import { http } from "react-invenio-forms";

export const FileUploader = ({
  fileUploaderMessage,
  record,
  recordFiles,
  allowedFileTypes,
}) => {
  const [filesState, setFilesState] = useState(recordFiles?.entries || []);
  const { formik, isSubmitting, save, isSaving } = useDepositApiClient();
  const { read } = useDepositFileApiClient();
  const { values } = formik;

  const {
    data,
    error,
    isError: isFileImportError,
    isLoading,
    mutate: importParentFiles,
  } = useMutation({
    mutationFn: () =>
      http.post(recordObject?.links?.self + "/actions/files-import", {}),
    // onError,
    onSuccess: (data) => {
      console.log(data);
      setFilesState(data.data.entries);
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
      },
    }
  );

  const recordObject = record || values;

  const handleFilesUpload = () => {
    refetch();
  };
  const handleFileDeletion = (fileObject) => {
    setFilesState((prevFilesState) =>
      prevFilesState.filter((file) => file.key !== fileObject.key)
    );
  };

  return values.id && recordObject?.files?.enabled ? (
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
          {filesState?.length === 0 && (
            <Message className="flex">
              <p className="display-inline-block">
                <Icon name="info circle" />
                {i18next.t("You can import files from the previous version.")}
              </p>
              <Button
                type="button"
                size="mini"
                primary
                onClick={() => importParentFiles()}
                icon="sync"
                content={i18next.t("Import parent files")}
              />
            </Message>
          )}
          <FileUploaderTable
            files={filesState}
            handleFileDeletion={handleFileDeletion}
            record={recordObject}
            allowedFileTypes={allowedFileTypes}
          />
          <UploadFileButton
            record={recordObject}
            handleFilesUpload={handleFilesUpload}
            allowedFileTypes={allowedFileTypes}
          />
        </React.Fragment>
      )}
      <Message icon>
        <Icon name="warning sign" className="text size large" />
        <Message.Content>{fileUploaderMessage}</Message.Content>
      </Message>
    </Dimmer.Dimmable>
  ) : (
    <Message>
      <Icon name="info circle" className="text size large" />
      <Trans>
        If you wish to upload files, you must
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
        your draft first.
      </Trans>
    </Message>
  );
};

FileUploader.propTypes = {
  fileUploaderMessage: PropTypes.string,
  record: PropTypes.object,
  recordFiles: PropTypes.object,
  allowedFileTypes: PropTypes.array,
};

FileUploader.defaultProps = {
  fileUploaderMessage: i18next.t(
    "File addition, removal or modification are not allowed after you have published your draft."
  ),
  allowedFileTypes: ["*/*"],
};
