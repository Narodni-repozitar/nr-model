import React from "react";
import PropTypes from "prop-types";
import { ArrayField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import {
  ArrayFieldItem,
  useFieldData,
  useSanitizeInput,
  TextField,
} from "@js/oarepo_ui/forms";
import { useFormikContext, getIn } from "formik";

export const SeriesField = ({ fieldPath }) => {
  const { values, setFieldValue, setFieldTouched } = useFormikContext();

  const { sanitizeInput } = useSanitizeInput();
  const { getFieldData } = useFieldData();

  return (
    <ArrayField
      addButtonLabel={i18next.t("Add series")}
      fieldPath={fieldPath}
      {...getFieldData({ fieldPath, fieldRepresentation: "text" })}
      addButtonClassName="array-field-add-button"
    >
      {({ arrayHelpers, indexPath }) => {
        const fieldPathPrefix = `${fieldPath}.${indexPath}`;
        const seriesTitleFieldPath = `${fieldPathPrefix}.seriesTitle`;
        return (
          <ArrayFieldItem
            indexPath={indexPath}
            arrayHelpers={arrayHelpers}
            fieldPathPrefix={fieldPathPrefix}
          >
            <TextField
              width={8}
              fieldPath={seriesTitleFieldPath}
              fieldRepresentation="compact"
            />
            <TextField
              width={8}
              fieldPath={`${fieldPathPrefix}.seriesVolume`}
              fieldRepresentation="compact"
            />
          </ArrayFieldItem>
        );
      }}
    </ArrayField>
  );
};

SeriesField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
};
