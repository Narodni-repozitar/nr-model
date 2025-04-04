import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Form, Icon } from "semantic-ui-react";
import { LicenseModal } from "./LicenseModal";
import { LicenseFieldItem } from "./LicenseFieldItem";
import { i18next } from "@translations/nr/i18next";
import { useFieldData } from "@js/oarepo_ui";
import { FieldLabel } from "react-invenio-forms";

const defaultSearchConfig = {
  searchApi: {
    axios: {
      headers: {
        Accept: "application/vnd.inveniordm.v1+json",
      },
      url: "/api/vocabularies/rights",
    },
  },
  initialQueryState: {
    size: 25,
    page: 1,
    sortBy: "bestmatch",
    filters: [["tags", ""]],
  },
};

export const LicenseField = ({
  label,
  fieldPath,
  required,
  searchConfig = defaultSearchConfig,
  serializeLicense,
  helpText,
  icon = "drivers license",
}) => {
  const { getFieldData } = useFieldData();

  const fieldData = {
    ...getFieldData({ fieldPath, icon, fieldRepresentation: "text" }),
    ...(label && { label }),
    ...(required && { required }),
    ...(helpText && { helpText }),
  };
  const { values, setFieldValue } = useFormikContext();
  const license = getIn(values, fieldPath, {})?.id
    ? getIn(values, fieldPath, {})
    : "";
  const handleLicenseChange = (selectedLicense) => {
    setFieldValue(fieldPath, { id: selectedLicense.id });
  };
  return (
    <Form.Field required={fieldData.required}>
      <FieldLabel htmlFor={fieldPath} icon={icon} label={fieldData.label} />
      {fieldData.helpText && (
        <label className="helptext">{fieldData.helpText}</label>
      )}
      {license ? (
        <LicenseFieldItem
          key={license.id}
          license={license}
          fieldPath={fieldPath}
          searchConfig={searchConfig}
          handleLicenseChange={handleLicenseChange}
          serializeLicense={serializeLicense}
        />
      ) : (
        <LicenseModal
          searchConfig={searchConfig}
          initialLicense={license}
          trigger={
            <Form.Button
              className="array-field-add-button"
              type="button"
              key="license"
              icon
              labelPosition="left"
            >
              <Icon name="add" />
              {i18next.t("Choose license")}
            </Form.Button>
          }
          handleLicenseChange={handleLicenseChange}
          serializeLicense={serializeLicense}
        />
      )}
    </Form.Field>
  );
};

LicenseField.propTypes = {
  label: PropTypes.oneOfType([PropTypes.string, PropTypes.node]),
  fieldPath: PropTypes.string.isRequired,
  required: PropTypes.bool,
  searchConfig: PropTypes.object,
  serializeLicense: PropTypes.func,
  helpText: PropTypes.string,
  icon: PropTypes.string,
};
