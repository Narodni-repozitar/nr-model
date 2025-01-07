// This file is part of Invenio-RDM-Records
// Copyright (C) 2020-2023 CERN.
// Copyright (C) 2020-2022 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
// Copyright (C) 2022 data-futures.org.
//
// Invenio-RDM-Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import { Button, Form, Grid, Header, Modal } from "semantic-ui-react";
import { Formik, getIn } from "formik";
import * as Yup from "yup";
import { i18next } from "@translations/nr/i18next";
import { TextField, GroupField } from "react-invenio-forms";
import { CreatibutorsField } from "../CreatibutorsField";
import {
  IdentifiersField,
  objectIdentifiersSchema,
  IdentifiersValidationSchema,
} from "../IdentifiersField";
import { LocalVocabularySelectField } from "@js/oarepo_vocabularies";
import PropTypes from "prop-types";
import {
  requiredMessage,
  handleValidateAndBlur,
  useSanitizeInput,
  useFieldData,
} from "@js/oarepo_ui";
import _isEmpty from "lodash/isEmpty";

const RelatedItemsSchema = Yup.object({
  itemTitle: Yup.string().required(requiredMessage).label(i18next.t("Title")),
  itemURL: Yup.string().url(i18next.t("Please provide an URL in valid format")),
  itemYear: Yup.number()
    .typeError(i18next.t("Year must be a number."))
    .test("len", i18next.t("Year must be in format YYYY."), (val) => {
      if (val) {
        return val.toString().length === 4;
      }
      return true;
    }),
  itemPIDs: IdentifiersValidationSchema,
  itemVolume: Yup.string(),
  itemIssue: Yup.string(),
  itemStartPage: Yup.string(),
  itemEndPage: Yup.string(),
  itemPublisher: Yup.string(),
  itemRelationType: Yup.object(),
  itemResourceType: Yup.object(),
});

const modalActions = {
  ADD: "add",
  EDIT: "edit",
};
export const RelatedItemsModal = ({
  initialRelatedItem,
  initialAction,
  addLabel,
  editLabel,
  onRelatedItemChange,
  trigger,
}) => {
  const [open, setOpen] = React.useState(false);
  const [action, setAction] = React.useState(initialAction);
  const [saveAndContinueLabel, setSaveAndContinueLabel] = React.useState(
    i18next.t("Save and add another")
  );
  const { getFieldData } = useFieldData();
  const { sanitizeInput } = useSanitizeInput();

  const openModal = () => {
    setOpen(true);
    setAction(initialAction);
  };
  const closeModal = () => {
    setOpen(false);
    setAction(initialAction);
  };

  const changeContent = () => {
    setSaveAndContinueLabel(i18next.t("Added"));
    setTimeout(() => {
      setSaveAndContinueLabel(i18next.t("Save and add another"));
    }, 1000);
  };

  const onSubmit = (values, formikBag) => {
    const fieldValue = getIn(values, "itemTitle");
    const cleanedContent = sanitizeInput(fieldValue);
    const updatedValues = { ...values, itemTitle: cleanedContent };
    onRelatedItemChange(updatedValues);
    formikBag.setSubmitting(false);
    formikBag.resetForm();
    switch (action) {
      case "saveAndContinue":
        closeModal();
        openModal();
        changeContent();
        break;
      case "saveAndClose":
        closeModal();
        break;
      default:
        break;
    }
  };

  return (
    <Formik
      initialValues={
        !_isEmpty(initialRelatedItem)
          ? initialRelatedItem
          : {
              itemTitle: "",
              itemCreators: [],
              itemContributors: [],
              itemPIDs: [],
              itemURL: "",
              itemYear: "",
              itemVolume: "",
              itemIssue: "",
              itemStartPage: "",
              itemEndPage: "",
              itemPublisher: "",
              itemRelationType: {},
              itemResourceType: {},
            }
      }
      onSubmit={onSubmit}
      enableReinitialize
      validationSchema={RelatedItemsSchema}
      validateOnChange={false}
      validateOnBlur={false}
    >
      {({
        values,
        resetForm,
        handleSubmit,
        validateField,
        setFieldTouched,
      }) => {
        const handleBlur = handleValidateAndBlur(
          validateField,
          setFieldTouched
        );

        const handleAction = (action) => {
          setAction(action);
          handleSubmit();
        };

        return (
          <Modal
            className="form-modal"
            size="large"
            centered={false}
            onOpen={() => openModal()}
            open={open}
            trigger={trigger}
            onClose={() => {
              closeModal();
              resetForm();
            }}
            closeIcon
            closeOnDimmerClick={false}
          >
            <Modal.Header as="h6">
              <Grid>
                <Grid.Column floated="left" width={8}>
                  <Header as="h2">
                    {initialAction === modalActions.ADD ? addLabel : editLabel}
                  </Header>
                </Grid.Column>
              </Grid>
            </Modal.Header>
            <Modal.Content>
              <Form>
                <TextField
                  autoComplete="off"
                  fieldPath="itemTitle"
                  onBlur={() => handleBlur("itemTitle")}
                  {...getFieldData({ fieldPath: "itemTitle" })}
                />
                <CreatibutorsField
                  fieldPath="itemCreators"
                  schema="creators"
                  autocompleteNames="off"
                  {...getFieldData({ fieldPath: "itemCreators" })}
                  fieldPathPrefix="metadata.relatedItems.0.itemCreators.0"
                />
                <CreatibutorsField
                  addButtonLabel={i18next.t("Add contributor")}
                  modal={{
                    addLabel: i18next.t("Add contributor"),
                    editLabel: i18next.t("Edit contributor"),
                  }}
                  fieldPath="itemContributors"
                  schema="contributors"
                  autocompleteNames="off"
                  fieldPathPrefix="metadata.relatedItems.0.itemContributors.0"
                  {...getFieldData({
                    fieldPath: "itemContributors",
                    icon: "user",
                  })}
                />

                <IdentifiersField
                  className="related-items-identifiers"
                  options={objectIdentifiersSchema}
                  fieldPath="itemPIDs"
                  validateOnBlur
                />
                <TextField
                  autoComplete="off"
                  fieldPath="itemURL"
                  onBlur={() => handleBlur("itemURL")}
                  {...getFieldData({ fieldPath: "itemURL" })}
                />
                <GroupField widths="equal">
                  <TextField
                    fieldPath="itemYear"
                    onBlur={() => handleBlur("itemYear")}
                    {...getFieldData({
                      fieldPath: "itemYear",
                      fieldRepresentation: "compact",
                    })}
                  />
                  <TextField
                    fieldPath="itemVolume"
                    onBlur={() => handleBlur("itemVolume")}
                    {...getFieldData({
                      fieldPath: "itemVolume",
                      fieldRepresentation: "compact",
                    })}
                  />
                  <TextField
                    fieldPath="itemIssue"
                    onBlur={() => handleBlur("itemIssue")}
                    {...getFieldData({
                      fieldPath: "itemIssue",
                      fieldRepresentation: "compact",
                    })}
                  />
                  <TextField
                    fieldPath="itemStartPage"
                    onBlur={() => handleBlur("itemStartPage")}
                    {...getFieldData({
                      fieldPath: "itemStartPage",
                      fieldRepresentation: "compact",
                    })}
                  />
                  <TextField
                    fieldPath="itemEndPage"
                    onBlur={() => handleBlur("itemEndPage")}
                    {...getFieldData({
                      fieldPath: "itemEndPage",
                      fieldRepresentation: "compact",
                    })}
                  />
                </GroupField>
                <TextField
                  width={16}
                  fieldPath="itemPublisher"
                  onBlur={() => handleBlur("itemPublisher")}
                  {...getFieldData({ fieldPath: "itemPublisher" })}
                />
                <GroupField>
                  <LocalVocabularySelectField
                    width={16}
                    fieldPath="itemRelationType"
                    clearable
                    optionsListName="item-relation-types"
                    {...getFieldData({
                      fieldPath: "itemRelationType",
                      fieldRepresentation: "compact",
                    })}
                  />
                  <LocalVocabularySelectField
                    width={16}
                    fieldPath="itemResourceType"
                    clearable
                    optionsListName="resource-types"
                    showLeafsOnly
                    {...getFieldData({
                      fieldPath: "itemResourceType",
                      fieldRepresentation: "compact",
                    })}
                  />
                </GroupField>
              </Form>
            </Modal.Content>
            <Modal.Actions>
              <Button
                name="cancel"
                onClick={() => {
                  resetForm();
                  closeModal();
                }}
                icon="remove"
                content={i18next.t("Cancel")}
                floated="left"
              />
              {initialAction === modalActions.ADD && (
                <Button
                  name="submit"
                  type="submit"
                  onMouseDown={() => {
                    handleAction("saveAndContinue");
                  }}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") {
                      handleAction("saveAndContinue");
                    }
                  }}
                  primary
                  icon="checkmark"
                  content={saveAndContinueLabel}
                />
              )}
              <Button
                name="submit"
                type="submit"
                onMouseDown={() => {
                  handleAction("saveAndClose");
                }}
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    handleAction("saveAndClose");
                  }
                }}
                primary
                icon="checkmark"
                content={i18next.t("Save")}
              />
            </Modal.Actions>
          </Modal>
        );
      }}
    </Formik>
  );
};

RelatedItemsModal.propTypes = {
  initialRelatedItem: PropTypes.object,
  initialAction: PropTypes.string.isRequired,
  addLabel: PropTypes.string,
  editLabel: PropTypes.string,
  onRelatedItemChange: PropTypes.func,
  trigger: PropTypes.node,
};

RelatedItemsModal.defaultProps = {
  initialRelatedItem: {},
};
