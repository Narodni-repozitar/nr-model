import React from "react";
import PropTypes from "prop-types";
import { ArrayField, SelectField, TextField } from "react-invenio-forms";
import { i18next } from "@translations/nr/i18next";
import { ArrayFieldItem, useFieldData, useValidateOnBlur } from "@js/oarepo_ui";
import { useFormikContext } from "formik";
import * as Yup from "yup";

export const objectIdentifiersSchema = [
  { value: "DOI", text: i18next.t("DOI"), key: "DOI" },
  { value: "Handle", text: i18next.t("Handle"), key: "Handle" },
  { value: "ISBN", text: i18next.t("ISBN"), key: "ISBN" },
  { value: "ISSN", text: i18next.t("ISSN"), key: "ISSN" },
  { value: "RIV", text: i18next.t("RIV"), key: "RIV" },
];

export const personIdentifiersSchema = [
  { value: "orcid", text: i18next.t("ORCID"), key: "orcid" },
  { value: "scopusID", text: i18next.t("ScopusID"), key: "scopusID" },
  {
    value: "researcherID",
    text: i18next.t("ResearcherID"),
    key: "researcherID",
  },
  { value: "czenasAutID", text: i18next.t("CzenasAutID"), key: "czenasAutID" },
  { value: "vedidk", text: i18next.t("vedIDK"), key: "vedidk" },
  {
    value: "institutionalID",
    text: i18next.t("InstitutionalID"),
    key: "institutionalID",
  },
  { value: "ISNI", text: i18next.t("ISNI"), key: "ISNI" },
];

export const organizationIdentifiersSchema = [
  { value: "ISNI", text: i18next.t("ISNI"), key: "ISNI" },
  { value: "ROR", text: i18next.t("ROR"), key: "ROR" },
  { value: "ICO", text: i18next.t("ICO"), key: "ICO" },
  { value: "DOI", text: i18next.t("DOI"), key: "DOI" },
];

export const IdentifiersValidationSchema = Yup.array().of(
  Yup.object().shape({
    identifier: Yup.string().test(
      "Test if both identifier and identifier type are provided",
      i18next.t("Both identifier and identifier type must be filled."),
      (value, context) => {
        if (!value && !context.parent.scheme) return true;
        return !(!value && context.parent.scheme);
      }
    ),
    scheme: Yup.string().test(
      "Test if both identifier and identifier type are provided",
      i18next.t("Both identifier and identifier type must be filled."),
      (value, context) => {
        if (!value && !context.parent.identifier) return true;
        return !(!value && context.parent.identifier);
      }
    ),
  })
);
export const IdentifiersField = ({
  fieldPath,
  labelIcon,
  options,
  className,
  defaultNewValue,
  validateOnBlur,
  ...uiProps
}) => {
  const { setFieldTouched } = useFormikContext();
  const { getFieldData } = useFieldData();
  const handleValidateAndBlur = useValidateOnBlur();

  return (
    <ArrayField
      addButtonLabel={i18next.t("Add identifier")}
      fieldPath={fieldPath}
      className={className}
      defaultNewValue={defaultNewValue}
      {...getFieldData({
        fieldPath,
        icon: labelIcon,
        fieldRepresentation: "text",
      })}
      addButtonClassName="array-field-add-button"
    >
      {({ arrayHelpers, indexPath }) => {
        const fieldPathPrefix = `${fieldPath}.${indexPath}`;
        const schemeFieldPath = `${fieldPathPrefix}.scheme`;
        const identifierFieldPath = `${fieldPathPrefix}.identifier`;
        return (
          <ArrayFieldItem
            indexPath={indexPath}
            arrayHelpers={arrayHelpers}
            fieldPathPrefix={fieldPathPrefix}
          >
            <SelectField
              clearable
              width={5}
              fieldPath={schemeFieldPath}
              options={options}
              onBlur={
                validateOnBlur
                  ? () => handleValidateAndBlur(schemeFieldPath)
                  : () => setFieldTouched(schemeFieldPath)
              }
              {...uiProps}
              {...getFieldData({
                fieldPath: schemeFieldPath,
                fieldRepresentation: "compact",
              })}
            />
            <TextField
              width={11}
              fieldPath={identifierFieldPath}
              {...getFieldData({
                fieldPath: identifierFieldPath,
                fieldRepresentation: "compact",
              })}
              onBlur={
                validateOnBlur
                  ? () => handleValidateAndBlur(identifierFieldPath)
                  : () => setFieldTouched(identifierFieldPath)
              }
            />
          </ArrayFieldItem>
        );
      }}
    </ArrayField>
  );
};

IdentifiersField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  labelIcon: PropTypes.string,
  options: PropTypes.array.isRequired,
  className: PropTypes.string,
  defaultNewValue: PropTypes.object,
  validateOnBlur: PropTypes.bool,
};

IdentifiersField.defaultProps = {
  labelIcon: "pencil",
  defaultNewValue: { scheme: "", identifier: "" },
  validateOnBlur: false,
};
