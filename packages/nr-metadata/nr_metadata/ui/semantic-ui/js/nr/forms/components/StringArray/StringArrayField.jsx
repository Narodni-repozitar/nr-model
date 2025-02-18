import React from "react";
import PropTypes from "prop-types";
import { FieldLabel, TextField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import { useFormikContext, getIn, FieldArray } from "formik";
import { Icon, Form, Label } from "semantic-ui-react";
import {
  ArrayFieldItem,
  useShowEmptyValue,
  useSanitizeInput,
} from "@js/oarepo_ui";

export const StringArrayField = ({
  fieldPath,
  label,
  required,
  defaultNewValue,
  addButtonLabel,
  helpText,
  labelIcon,
  showEmptyValue,
  addButtonClassName,
  ...uiProps
}) => {
  const { values, setFieldValue, setFieldTouched, errors } = useFormikContext();
  useShowEmptyValue(fieldPath, defaultNewValue, showEmptyValue);
  const { sanitizeInput } = useSanitizeInput();
  const fieldError = getIn(errors, fieldPath, null);
  return (
    <Form.Field>
      <FieldLabel label={label} />
      <FieldArray
        name={fieldPath}
        render={(arrayHelpers) => (
          <React.Fragment>
            {getIn(values, fieldPath, []).map((item, index) => {
              const indexPath = `${fieldPath}.${index}`;
              const textInputError = Array.isArray(fieldError)
                ? fieldError[index]
                : fieldError;
              return (
                <ArrayFieldItem
                  key={index}
                  indexPath={index}
                  arrayHelpers={arrayHelpers}
                  fieldPathPrefix={indexPath}
                >
                  <TextField
                    width={16}
                    fieldPath={indexPath}
                    label={`#${index + 1}`}
                    optimized
                    fluid
                    onBlur={() => {
                      const cleanedContent = sanitizeInput(
                        getIn(values, indexPath)
                      );
                      setFieldValue(indexPath, cleanedContent);
                      setFieldTouched(indexPath, true);
                    }}
                    {...uiProps}
                    error={textInputError}
                  />
                </ArrayFieldItem>
              );
            })}
            {helpText ? <label className="helptext">{helpText}</label> : null}
            <Form.Button
              className={addButtonClassName}
              type="button"
              icon
              labelPosition="left"
              onClick={() => {
                arrayHelpers.push(defaultNewValue);
              }}
            >
              <Icon name="add" />
              {addButtonLabel}
            </Form.Button>
          </React.Fragment>
        )}
      />
      {fieldError && typeof fieldError == "string" && (
        <Label pointing="left" prompt>
          {fieldError}
        </Label>
      )}
    </Form.Field>
  );
};

StringArrayField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  label: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  defaultNewValue: PropTypes.string,
  addButtonLabel: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  helpText: PropTypes.string,
  labelIcon: PropTypes.string,
  required: PropTypes.bool,
  showEmptyValue: PropTypes.bool,
  addButtonClassName: PropTypes.string,
};

StringArrayField.defaultProps = {
  addButtonLabel: i18next.t("Add note"),
  defaultNewValue: "",
  showEmptyValue: false,
  addButtonClassName: "array-field-add-button inline",
};
