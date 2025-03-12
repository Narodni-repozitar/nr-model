import React from "react";
import PropTypes from "prop-types";
import { getIn, useFormikContext } from "formik";
import { Form, Icon } from "semantic-ui-react";
import { LicenseModal } from "./LicenseModal";
import { LicenseFieldItem } from "./LicenseFieldItem";
import { i18next } from "@translations/nr/i18next";
import { useFieldData } from "@js/oarepo_ui";

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
  label = i18next.t("License"),
  fieldPath,
  required = false,
  searchConfig = defaultSearchConfig,
  serializeLicense,
  helpText = i18next.t(
    "If a Creative Commons license is associated with the resource, select the appropriate license option from the menu. We recommend choosing the latest versions, namely 3.0 Czech and 4.0 International."
  ),
  icon = "drivers license",
}) => {
  const { getFieldData } = useFieldData();

  const {
    label: modelLabel,
    helpText: modelHelpText,
    required: modelRequired,
  } = getFieldData({ fieldPath, icon: icon });
  const { values, setFieldValue } = useFormikContext();
  const license = getIn(values, fieldPath, {})?.id
    ? getIn(values, fieldPath, {})
    : "";
  const handleLicenseChange = (selectedLicense) => {
    setFieldValue(fieldPath, { id: selectedLicense.id });
  };
  return (
    <Form.Field required={modelRequired ?? required}>
      {modelLabel ?? label}
      <label className="helptext">{modelHelpText ?? helpText}</label>
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
