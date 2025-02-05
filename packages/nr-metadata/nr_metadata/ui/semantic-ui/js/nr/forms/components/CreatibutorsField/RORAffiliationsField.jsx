import * as React from "react";

import { RORInstitutionResult } from "../RORInstitutionResult";
import { VocabularyRemoteSelectField, VocabularyModalTrigger } from "@js/oarepo_vocabularies";
import { useFieldData } from "@js/oarepo_ui";
import { i18next } from "@translations/nr/i18next";

export const RORAffiliationsField = ({
  fieldPath,
  multiple = false,
  ...rest
}) => {
  const { getFieldData } = useFieldData();

  return (
    <VocabularyRemoteSelectField
      overriddenComponents={{
        "VocabularyRemoteSelect.ext.ResultsList.item": RORInstitutionResult,
      }}
      vocabulary="institutions"
      multiple={multiple}
      fieldPath={fieldPath}
      modalHeader={
        getFieldData({
          fieldPath: fieldPath,
          fieldRepresentation: "text",
        }).label
      }
      closeOnDimmerClick={true}
      triggerLabel={i18next.t('Choose')}
      {...getFieldData({
        fieldPath: fieldPath,
      })}
      {...rest}
    />
  );
};
