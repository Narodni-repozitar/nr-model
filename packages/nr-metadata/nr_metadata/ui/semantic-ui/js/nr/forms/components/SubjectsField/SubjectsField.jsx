import React, { useCallback } from "react";
import PropTypes from "prop-types";
import { Form, Icon, Divider } from "semantic-ui-react";
import { i18next } from "@translations/nr/i18next";
import { SubjectsModal } from "./SubjectsModal";
import { useFormikContext, getIn } from "formik";
import _difference from "lodash/difference";
import { ExternalSubjects } from "./ExternalSubjects";
import { KeywordSubjects } from "./KeywordSubjects";
import { useFieldData } from "@js/oarepo_ui";

export const SubjectsField = ({ fieldPath, hasLocalLanguageSelectField }) => {
  const { values, setFieldValue } = useFormikContext();
  const subjects = getIn(values, fieldPath, []);
  const externalSubjects = subjects.filter(
    (subject) => subject?.subjectScheme !== "keyword"
  );

  const keywordSubjects = _difference(subjects, externalSubjects).map(
    (subject) => ({
      ...subject,
      id: crypto.randomUUID(),
    })
  );
  const handleSubjectRemoval = useCallback(
    (id, lang) => {
      const newKeywordSubjects = keywordSubjects.map((subject) => {
        if (subject.id === id) {
          subject.subject = subject.subject.filter((s) => s.lang !== lang);
          return subject;
        }
        return subject;
      });
      setFieldValue(fieldPath, [
        ...externalSubjects,
        ...newKeywordSubjects
          .filter((subject) => subject?.subject?.length > 0)
          .map((subject) => {
            const { id, ...subjectWithoutId } = subject;
            return subjectWithoutId;
          }),
      ]);
    },
    [fieldPath, externalSubjects, keywordSubjects, setFieldValue]
  );

  const handleSubjectAdd = useCallback(
    (newSubject) => {
      setFieldValue(fieldPath, [...subjects, newSubject]);
    },
    [fieldPath, subjects, setFieldValue]
  );
  const { getFieldData } = useFieldData();
  const { label, helpText } = getFieldData({ fieldPath });
  return (
    <Form.Field className="ui subjects-field">
      {label}
      <ExternalSubjects externalSubjects={externalSubjects} />
      {externalSubjects.length > 0 && (
        <Divider horizontal section>
          {i18next.t("Free text keywords")}
        </Divider>
      )}
      <KeywordSubjects
        keywordSubjects={keywordSubjects}
        externalSubjects={externalSubjects}
        handleSubjectRemoval={handleSubjectRemoval}
      />
      <div>
        <SubjectsModal
          handleSubjectAdd={handleSubjectAdd}
          fieldPath={fieldPath}
          helpText={helpText}
          hasLocalLanguageSelectField={hasLocalLanguageSelectField}
          trigger={
            <Form.Button
              className="array-field-add-button rel-mt-1"
              type="button"
              icon
              labelPosition="left"
            >
              <Icon name="add" />
              {i18next.t("Add keywords")}
            </Form.Button>
          }
        />
      </div>
    </Form.Field>
  );
};

SubjectsField.propTypes = {
  fieldPath: PropTypes.string.isRequired,
  hasLocalLanguageSelectField: PropTypes.bool,
};
