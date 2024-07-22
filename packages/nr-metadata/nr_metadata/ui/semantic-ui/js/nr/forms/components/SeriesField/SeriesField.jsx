import React from "react";
import PropTypes from "prop-types";
import { ArrayField, TextField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import { ArrayFieldItem, useFieldData, useSanitizeInput } from "@js/oarepo_ui";
import { useFormikContext, getIn } from "formik";

export const SeriesField = ({ fieldPath, helpText }) => {
  const { values, setFieldValue, setFieldTouched } = useFormikContext();

  const { sanitizeInput } = useSanitizeInput();
  const { getFieldData } = useFieldData();

  return (
    <ArrayField
      addButtonLabel={i18next.t("Add series")}
      fieldPath={fieldPath}
      label={i18next.t("Series")}
      helpText={helpText}
      {...getFieldData(fieldPath).fullRepresentation}
      addButtonClassName="array-field-add-button"
    >
      {({ arrayHelpers, indexPath }) => {
        const fieldPathPrefix = `${fieldPath}.${indexPath}`;
        return (
          <ArrayFieldItem
            indexPath={indexPath}
            arrayHelpers={arrayHelpers}
            fieldPathPrefix={fieldPathPrefix}
          >
            <TextField
              width={8}
              fieldPath={`${fieldPathPrefix}.seriesTitle`}
              label={i18next.t("Series title")}
              {...getFieldData(`${fieldPathPrefix}.seriesTitle`)
                .compactRepresentation}
              required
              onBlur={() => {
                const cleanedContent = sanitizeInput(
                  getIn(values, `${fieldPathPrefix}.seriesTitle`)
                );
                setFieldValue(`${fieldPathPrefix}.seriesTitle`, cleanedContent);
                setFieldTouched(`${fieldPathPrefix}.seriesTitle`, true);
              }}
            />
            <TextField
              width={8}
              fieldPath={`${fieldPathPrefix}.seriesVolume`}
              label={i18next.t("Series volume")}
              {...getFieldData(`${fieldPathPrefix}.seriesVolume`)
                .compactRepresentation}
            />
          </ArrayFieldItem>
        );
      }}
    </ArrayField>
  );
};

SeriesField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  helpText: PropTypes.string,
};

SeriesField.defaultProps = {
  helpText: i18next.t(
    "Write down the name of the edition and write down the volume if name is provided."
  ),
};
