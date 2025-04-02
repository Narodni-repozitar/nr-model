// This file is part of Invenio-RDM-Records
// Copyright (C) 2020-2023 CERN.
// Copyright (C) 2020-2022 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
//
// Invenio-RDM-Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React, { Component } from "react";
import PropTypes from "prop-types";
import { getIn, FieldArray } from "formik";
import { Form, Label, List, Icon } from "semantic-ui-react";
import _get from "lodash/get";
import _truncate from "lodash/truncate";
import { FieldLabel } from "react-invenio-forms";
import { HTML5Backend } from "react-dnd-html5-backend";
import { DndProvider } from "react-dnd";
import { RelatedItemsModal } from "./RelatedItemsModal";
import { RelatedItemsFieldItem } from "./RelatedItemsFieldItem";
import { i18next } from "@translations/nr/i18next";
import { FieldDataProvider, useFieldData } from "@js/oarepo_ui/forms";

const relatedItemNameDisplay = (value) => {
  const name = _get(value, `itemTitle`);
  const URL = _get(value, `itemURL`);
  return (
    <span>
      {name}
      <a className="rel-ml-3" href={URL}>
        {URL && _truncate(URL, { length: 40, omission: "..." })}
      </a>
    </span>
  );
};

class RelatedItemsFieldForm extends Component {
  handleRelatedItemChange = (selectedRelatedItem) => {
    const { push: formikArrayPush } = this.props;
    formikArrayPush(selectedRelatedItem);
  };

  render() {
    const {
      form: { values, errors, initialErrors, initialValues },
      remove: formikArrayRemove,
      replace: formikArrayReplace,
      move: formikArrayMove,
      fieldPath,
      label,
      labelIcon,
      modal,
      addButtonLabel,
      required,
      helpText,
    } = this.props;

    const relatedItemsList = getIn(values, fieldPath, []);
    const formikInitialValues = getIn(initialValues, fieldPath, []);

    const error = getIn(errors, fieldPath, null);
    const initialError = getIn(initialErrors, fieldPath, null);
    const relatedItemsError =
      error || (relatedItemsList === formikInitialValues && initialError);
    return (
      <FieldDataProvider fieldPathPrefix={`${fieldPath}.0`}>
        <DndProvider backend={HTML5Backend}>
          <Form.Field
            required={required}
            className={relatedItemsError ? "error" : ""}
          >
            <FieldLabel htmlFor={fieldPath} icon={labelIcon} label={label} />
            <label className="helptext">{helpText}</label>
            <List>
              {relatedItemsList.map((value, index) => {
                const key = `${fieldPath}.${index}`;
                const displayName = relatedItemNameDisplay(value);
                return (
                  <RelatedItemsFieldItem
                    compKey={key}
                    key={key}
                    displayName={displayName}
                    index={index}
                    initialRelatedItem={value}
                    removeRelatedItem={formikArrayRemove}
                    replaceRelatedItem={formikArrayReplace}
                    moveRelatedItem={formikArrayMove}
                    addLabel={modal.addLabel}
                    editLabel={modal.editLabel}
                  />
                );
              })}
              <RelatedItemsModal
                key="add-related-item-modal"
                onRelatedItemChange={this.handleRelatedItemChange}
                initialAction="add"
                addLabel={modal.addLabel}
                editLabel={modal.editLabel}
                trigger={
                  <Form.Button
                    type="button"
                    icon
                    labelPosition="left"
                    className="array-field-add-button inline-block"
                  >
                    <Icon name="add" />
                    {addButtonLabel}
                  </Form.Button>
                }
              />

              {relatedItemsError && typeof relatedItemsError == "string" && (
                <Label pointing="left" prompt>
                  {relatedItemsError}
                </Label>
              )}
            </List>
          </Form.Field>
        </DndProvider>
      </FieldDataProvider>
    );
  }
}

export class RelatedItemsFieldComponent extends Component {
  render() {
    const { fieldPath } = this.props;

    return (
      <FieldArray
        name={fieldPath}
        render={(formikProps) => (
          <RelatedItemsFieldForm {...formikProps} {...this.props} />
        )}
      />
    );
  }
}

RelatedItemsFieldForm.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  addButtonLabel: PropTypes.string,
  modal: PropTypes.shape({
    addLabel: PropTypes.string.isRequired,
    editLabel: PropTypes.string.isRequired,
  }),
  label: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
  labelIcon: PropTypes.string,
  form: PropTypes.object.isRequired,
  remove: PropTypes.func.isRequired,
  replace: PropTypes.func.isRequired,
  move: PropTypes.func.isRequired,
  push: PropTypes.func.isRequired,
  required: PropTypes.bool,
  helpText: PropTypes.string,
};

RelatedItemsFieldForm.defaultProps = {
  label: i18next.t("Related items"),
  modal: {
    addLabel: i18next.t("Add related item"),
    editLabel: i18next.t("Edit related item"),
  },
  addButtonLabel: i18next.t("Add related item"),
  helpText: i18next.t(
    "Write down information about a resource related to the resource being described (i.e. if you are describing an article, here you can identify a magazine in which the article was published)."
  ),
};

RelatedItemsFieldComponent.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  addButtonLabel: PropTypes.string,
  modal: PropTypes.shape({
    addLabel: PropTypes.string,
    editLabel: PropTypes.string,
  }),

  label: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
  labelIcon: PropTypes.string,
  required: PropTypes.bool,
};

RelatedItemsFieldComponent.defaultProps = {
  label: undefined,
  labelIcon: undefined,
  modal: {
    addLabel: i18next.t("Add related item"),
    editLabel: i18next.t("Edit related item"),
  },
  addButtonLabel: i18next.t("Add related item"),
};

export const RelatedItemsField = ({
  overrides,
  icon = "pencil",
  label,
  required,
  helpText,
  fieldPath,
  ...props
}) => {
  const { getFieldData } = useFieldData();
  const fieldData = {
    ...getFieldData({ fieldPath, icon }),
    ...(label && { label }),
    ...(required && { required }),
    ...(helpText && { helpText }),
  };

  return (
    <RelatedItemsFieldComponent
      fieldPath={fieldPath}
      {...fieldData}
      {...props}
    />
  );
};

RelatedItemsField.propTypes = {
  label: PropTypes.string,
  overrides: PropTypes.object,
  icon: PropTypes.string,
  fieldPath: PropTypes.string.isRequired,
  required: PropTypes.bool,
  helpText: PropTypes.string,
};
