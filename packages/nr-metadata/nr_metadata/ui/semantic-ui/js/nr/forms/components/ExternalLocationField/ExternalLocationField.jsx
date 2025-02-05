import React from "react";
import PropTypes from "prop-types";
import { TextField } from "react-invenio-forms";
import { Form, Icon, Button } from "semantic-ui-react";
import { useFieldData, ArrayFieldItem } from "@js/oarepo_ui";
import { i18next } from "@translations/nr/i18next";
import { useFormikContext, getIn } from "formik";

const RemoveButton = ({
  handleClick,
  removeButtonId,
  onMouseEnter,
  onMouseLeave,
}) => (
  <Button
    aria-label={i18next.t("Remove field")}
    className="close-btn"
    type="button"
    icon
    id={removeButtonId}
    onClick={() => {
      handleClick();
    }}
    onMouseEnter={onMouseEnter}
    onMouseLeave={onMouseLeave}
  >
    <Icon name="close" />
  </Button>
);

RemoveButton.propTypes = {
  handleClick: PropTypes.func.isRequired,
  removeButtonId: PropTypes.string.isRequired,
  onMouseEnter: PropTypes.func.isRequired,
  onMouseLeave: PropTypes.func.isRequired,
};

export const ExternalLocationField = ({ fieldPath }) => {
  const { getFieldData } = useFieldData();
  const { values, setFieldValue } = useFormikContext();
  const fieldValue = getIn(values, fieldPath, {});

  const hasValue = Object.values(fieldValue).some((v) => v);

  const [showInput, setShowInput] = React.useState(hasValue);

  const { label, helpText } = getFieldData({ fieldPath });
  return (
    <Form.Field>
      {label}
      {showInput && (
        <ArrayFieldItem
          removeButton={RemoveButton}
          removeButtonProps={{
            "aria-label": i18next.t("Remove field"),
            className: "close-btn",
            type: "button",
            removeButtonId: `${fieldPath}.remove-button`,
            handleClick: () => {
              setFieldValue(fieldPath, {
                externalLocationURL: "",
                externalLocationNote: "",
              });
              setShowInput(false);
            },
          }}
          fieldPathPrefix={`${fieldPath}`}
        >
          <TextField
            width={8}
            fieldPath={`${fieldPath}.externalLocationURL`}
            {...getFieldData({
              fieldPath: `${fieldPath}.externalLocationURL`,
              fieldRepresentation: "compact",
            })}
          />
          <TextField
            width={8}
            fieldPath={`${fieldPath}.externalLocationNote`}
            {...getFieldData({
              fieldPath: `${fieldPath}.externalLocationNote`,
              fieldRepresentation: "compact",
            })}
          />
        </ArrayFieldItem>
      )}
      {helpText && <label className="helptext">{helpText}</label>}
      {!showInput && (
        <Form.Button
          type="button"
          icon
          className={"array-field-add-button"}
          labelPosition="left"
          onClick={() => {
            setShowInput(true);
          }}
        >
          <Icon name="add" />
          {i18next.t("Add external location")}
        </Form.Button>
      )}
    </Form.Field>
  );
};

ExternalLocationField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
