// This file is part of Invenio-RDM-Records
// Copyright (C) 2020-2023 CERN.
// Copyright (C) 2020-2022 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
// Copyright (C) 2022 data-futures.org.
//
// Invenio-RDM-Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React, { createRef, useState } from "react";
import {
  Button,
  Form,
  Grid,
  Header,
  Modal,
  Popup,
  Icon,
} from "semantic-ui-react";
import { Formik } from "formik";
import {
  Image,
  RadioField,
  RemoteSelectField,
  FieldLabel,
} from "react-invenio-forms";
import * as Yup from "yup";
import _get from "lodash/get";
import _isEmpty from "lodash/isEmpty";
import { CREATIBUTOR_TYPE } from "./constants";
import { i18next } from "@translations/nr/i18next";
import { Trans } from "react-i18next";
import { LocalVocabularySelectField } from "@js/oarepo_vocabularies";
import PropTypes from "prop-types";
import {
  IdentifiersField,
  personIdentifiersSchema,
  IdentifiersValidationSchema,
} from "../IdentifiersField";
import {
  getTitleFromMultilingualObject,
  handleValidateAndBlur,
  useFieldData,
} from "@js/oarepo_ui";
import { TextField } from "@js/oarepo_ui/forms";
import { RORAffiliationsField } from "./RORAffiliationsField";

const ModalActions = {
  ADD: "add",
  EDIT: "edit",
};

const NamesAutocompleteOptions = {
  SEARCH: "search",
  SEARCH_ONLY: "search_only",
  OFF: "off",
};

const makeIdEntry = (identifier) => {
  let icon = null;
  let link = null;
  if (identifier.scheme === "orcid") {
    icon = "/static/images/orcid.svg";
    link = "https://orcid.org/" + identifier.identifier;
  } else if (identifier.scheme === "gnd") {
    icon = "/static/images/gnd-icon.svg";
    link = "https://d-nb.info/gnd/" + identifier.identifier;
  } else if (identifier.scheme === "ror") {
    icon = "/static/images/ror-icon.svg";
    link = "https://ror.org/" + identifier.identifier;
  } else {
    return (
      <>
        {identifier.scehme}: {identifier.identifier}
      </>
    );
  }

  return (
    <span key={identifier.identifier}>
      <a href={link} target="_blank" rel="noopener noreferrer">
        <Image
          src={icon}
          className="inline-id-icon ml-5 mr-5"
          verticalAlign="middle"
        />
        {identifier.identifier}
      </a>
    </span>
  );
};

const typeFieldPath = "nameType";
const familyNameFieldPath = "familyName";
const givenNameFieldPath = "givenName";
const identifiersFieldPath = "authorityIdentifiers";
const affiliationsFieldPath = "affiliations";
const roleFieldPath = "contributorType";
const affiliationFullNameFieldPath = "affiliationNameFieldPath";
const fullNameFieldPath = "fullName";

/**
 * Function to transform formik creatibutor state
 * back to the external format.
 */
const serializeCreatibutor = (submittedCreatibutor, isCreator, isPerson) => {
  const contributorType = _get(submittedCreatibutor, roleFieldPath);
  const nameType = _get(submittedCreatibutor, typeFieldPath);

  if (isPerson) {
    const familyName = submittedCreatibutor[familyNameFieldPath];
    const givenName = submittedCreatibutor[givenNameFieldPath];
    const fullName = `${familyName}, ${givenName}`;
    const affiliations = _get(submittedCreatibutor, affiliationsFieldPath, []);
    const identifiers = _get(submittedCreatibutor, identifiersFieldPath, []);
    return {
      nameType,
      fullName,
      familyName,
      givenName,
      authorityIdentifiers: identifiers,
      affiliations: affiliations.map((aff) => aff?.data || aff),
      ...(!isCreator && { contributorType } && { contributorType }),
    };
  } else {
    const affiliation = _get(
      submittedCreatibutor,
      affiliationFullNameFieldPath,
      ""
    );
    const orgFullName =
      getTitleFromMultilingualObject(affiliation.title) ??
      (affiliation.id ?? typeof affiliation === "string"
        ? affiliation
        : i18next.t("Unknown item"));
    return {
      nameType,
      fullName: orgFullName,
      ...(!isCreator && { contributorType } && { contributorType }),
    };
  }
};

/**
 * Function to transform creatibutor object
 * to formik initialValues.
 */
const deserializeCreatibutor = (initialCreatibutor, isCreator, isPerson) => {
  if (isPerson) {
    const familyName = _get(initialCreatibutor, familyNameFieldPath, "");
    const givenName = _get(initialCreatibutor, givenNameFieldPath, "");

    return {
      nameType: CREATIBUTOR_TYPE.PERSON,
      familyName,
      givenName,
      ...initialCreatibutor,
      [identifiersFieldPath]: _get(
        initialCreatibutor,
        identifiersFieldPath,
        []
      ),
      affiliations: _get(initialCreatibutor, affiliationsFieldPath, []).map(
        (aff) => ({
          ...aff,
          text: getTitleFromMultilingualObject(aff?.title),
          value: aff?.id,
        })
      ),
      ...(!isCreator && {
        contributorType: _get(initialCreatibutor, roleFieldPath),
      }),
    };
  } else {
    return {
      nameType: CREATIBUTOR_TYPE.ORGANIZATION,
      [affiliationFullNameFieldPath]: _get(
        initialCreatibutor,
        fullNameFieldPath
      ),
      ...(!isCreator && {
        contributorType: _get(initialCreatibutor, "contributorType"),
      }),
    };
  }
};

const serializeSuggestions = (
  creatibutors,
  showPersonForm,
  autocompleteNames
) => {
  let results = creatibutors.map((creatibutor) => {
    let affNames = "";
    creatibutor.affiliations.forEach((affiliation, idx) => {
      affNames += affiliation.name;
      if (idx < creatibutor.affiliations.length - 1) {
        affNames += ", ";
      }
    });

    let idString = [];
    creatibutor.identifiers.forEach((i) => {
      idString.push(makeIdEntry(i));
    });

    return {
      text: creatibutor.name,
      value: creatibutor.id,
      extra: creatibutor,
      key: creatibutor.id,
      content: (
        <Header>
          <Header.Content>
            {creatibutor.name} {idString.length ? <>({idString})</> : null}
          </Header.Content>
          <Header.Subheader>{affNames}</Header.Subheader>
        </Header>
      ),
    };
  });

  const showManualEntry =
    autocompleteNames === NamesAutocompleteOptions.SEARCH_ONLY &&
    !showPersonForm;

  if (showManualEntry) {
    results.push({
      text: "Manual entry",
      value: "Manual entry",
      extra: "Manual entry",
      key: "manual-entry",
      content: (
        <Header textAlign="center">
          <Header.Content>
            <p>
              <Trans>
                {/* eslint-disable-next-line jsx-a11y/anchor-is-valid*/}
                Couldn't find your person? You can <a>create a new entry</a>.
              </Trans>
            </p>
          </Header.Content>
        </Header>
      ),
    });
  }
  return results;
};

export const CreatibutorsModal = ({
  autocompleteNames,
  initialCreatibutor,
  initialAction,
  addLabel,
  editLabel,
  schema,
  onCreatibutorChange,
  trigger,
  nameTypeHelpText,
}) => {
  const [open, setOpen] = useState(false);
  const [action, setAction] = useState(initialAction);
  const [saveAndContinueLabel, setSaveAndContinueLabel] = useState(
    i18next.t("Save and add another")
  );
  const [showPersonForm, setShowPersonForm] = useState(
    autocompleteNames !== NamesAutocompleteOptions.SEARCH_ONLY ||
      !_isEmpty(initialCreatibutor)
  );

  const { getFieldData } = useFieldData();

  const namesAutocompleteRef = createRef();
  const isCreator = schema === "creators";

  const CreatorSchema = Yup.object({
    nameType: Yup.string(),
    givenName: Yup.string().when("nameType", (nameType, schema) => {
      if (nameType === CREATIBUTOR_TYPE.PERSON) {
        return schema
          .trim()
          .required(i18next.t("Given name is a required field."));
      }
    }),
    familyName: Yup.string().when("nameType", (nameType, schema) => {
      if (nameType === CREATIBUTOR_TYPE.PERSON) {
        return schema
          .trim()
          .required(i18next.t("Family name is a required field."));
      }
    }),
    fullName: Yup.string(),
    contributorType: Yup.mixed().test(
      "text",
      i18next.t("Organization's name is a required field."),
      (value, testContext) => {
        if (!isCreator) {
          return !_isEmpty(value);
        } else {
          return true;
        }
      }
    ),
    affiliationNameFieldPath: Yup.mixed().test(
      "text",
      i18next.t("Organization's name is a required field."),
      (value, testContext) => {
        if (testContext.parent.nameType === CREATIBUTOR_TYPE.ORGANIZATION) {
          return !_isEmpty(value);
        } else {
          return true;
        }
      }
    ),
    [identifiersFieldPath]: Yup.array().when("nameType", {
      is: CREATIBUTOR_TYPE.PERSON,
      then: IdentifiersValidationSchema,
      otherwise: Yup.array().of(Yup.object()), // Or another schema for other cases
    }),
  });

  const openModal = () => {
    setOpen(true);
    setAction(initialAction);
  };

  const closeModal = () => {
    setOpen(false);
    setAction(initialAction);
  };

  const changeContent = () => {
    setSaveAndContinueLabel(i18next.t("Added"));
    // change in 2 sec
    setTimeout(() => {
      setSaveAndContinueLabel(i18next.t("Save and add another"));
    }, 2000);
  };

  const displayActionLabel =
    initialAction === ModalActions.ADD ? addLabel : editLabel;

  const onSubmit = (values, formikBag) => {
    const isPerson = _get(values, typeFieldPath) === CREATIBUTOR_TYPE.PERSON;
    onCreatibutorChange(serializeCreatibutor(values, isCreator, isPerson));

    formikBag.setSubmitting(false);
    formikBag.resetForm();
    switch (action) {
      case "saveAndContinue":
        closeModal();
        openModal();
        changeContent();
        break;
      case "saveAndClose":
        closeModal();
        break;
      default:
        break;
    }
  };

  const onPersonSearchChange = ({ formikProps }, selectedSuggestions) => {
    if (selectedSuggestions[0].key === "manual-entry") {
      // Empty the autocomplete's selected values
      namesAutocompleteRef.current.setState({
        suggestions: [],
        selectedSuggestions: [],
      });
      setShowPersonForm(true);
      return;
    }
    setShowPersonForm(true);
    const identifiers = selectedSuggestions[0].extra.authorityIdentifiers.map(
      (identifier) => {
        return identifier.identifier;
      }
    );
    const affiliations = selectedSuggestions[0].extra.affiliations.map(
      (affiliation) => {
        return affiliation;
      }
    );

    const personOrOrgPath = ``;
    const familyNameFieldPath = `${personOrOrgPath}family_name`;
    const givenNameFieldPath = `${personOrOrgPath}given_name`;
    const identifiersFieldPath = `${personOrOrgPath}authorityIdentifiers`;
    const affiliationsFieldPath = "affiliations";

    let chosen = {
      [givenNameFieldPath]: selectedSuggestions[0].extra.given_name,
      [familyNameFieldPath]: selectedSuggestions[0].extra.family_name,
      [identifiersFieldPath]: identifiers,
      [affiliationsFieldPath]: affiliations,
    };
    Object.entries(chosen).forEach(([path, value]) => {
      formikProps.form.setFieldValue(path, value);
    });
  };

  const ActionLabel = () => displayActionLabel;

  const initialValues = deserializeCreatibutor(
    initialCreatibutor,
    isCreator,
    _get(initialCreatibutor, typeFieldPath) === CREATIBUTOR_TYPE.PERSON
  );
  return (
    <Formik
      initialValues={initialValues}
      onSubmit={onSubmit}
      enableReinitialize
      validationSchema={CreatorSchema}
      validateOnChange={false}
      validateOnBlur={false}
    >
      {({
        values,
        resetForm,
        handleSubmit,
        validateField,
        setFieldTouched,
      }) => {
        const handleBlur = handleValidateAndBlur(
          validateField,
          setFieldTouched
        );
        const handleAction = (action) => {
          setAction(action);
          setShowPersonForm(
            autocompleteNames !== NamesAutocompleteOptions.SEARCH_ONLY
          );
          handleSubmit();
        };
        return (
          <Modal
            centered={false}
            onOpen={() => openModal()}
            open={open}
            trigger={trigger}
            onClose={() => {
              closeModal();
              resetForm();
            }}
            closeIcon
            closeOnDimmerClick={false}
            className="form-modal"
            size="large"
          >
            <Modal.Header as="h6" className="pt-10 pb-10">
              <Grid>
                <Grid.Column floated="left">
                  <Header as="h2">
                    <ActionLabel />
                  </Header>
                </Grid.Column>
              </Grid>
            </Modal.Header>
            <Modal.Content>
              <Form>
                <Form.Group>
                  <RadioField
                    fieldPath={typeFieldPath}
                    label={i18next.t("Person")}
                    checked={
                      _get(values, typeFieldPath) === CREATIBUTOR_TYPE.PERSON
                    }
                    value={CREATIBUTOR_TYPE.PERSON}
                    onChange={({ formikProps }) => {
                      formikProps.form.setFieldValue(
                        typeFieldPath,
                        CREATIBUTOR_TYPE.PERSON
                      );
                    }}
                    optimized
                  />
                  <RadioField
                    fieldPath={typeFieldPath}
                    label={i18next.t("Organization")}
                    checked={
                      _get(values, typeFieldPath) ===
                      CREATIBUTOR_TYPE.ORGANIZATION
                    }
                    value={CREATIBUTOR_TYPE.ORGANIZATION}
                    onChange={({ formikProps }) => {
                      formikProps.form.setFieldValue(
                        typeFieldPath,
                        CREATIBUTOR_TYPE.ORGANIZATION
                      );
                    }}
                    optimized
                  />
                  <Popup
                    content={nameTypeHelpText}
                    trigger={
                      <Icon
                        className="text size huge"
                        name="question circle outline"
                      ></Icon>
                    }
                  />
                </Form.Group>
                {_get(values, typeFieldPath, "") ===
                  CREATIBUTOR_TYPE.PERSON && (
                  <div>
                    {autocompleteNames !== NamesAutocompleteOptions.OFF && (
                      <RemoteSelectField
                        selectOnBlur={false}
                        selectOnNavigation={false}
                        searchInput={{
                          autoFocus: _isEmpty(initialCreatibutor),
                        }}
                        fieldPath="creators"
                        clearable
                        multiple={false}
                        allowAdditions={false}
                        placeholder={i18next.t(
                          "Search for persons by name, identifier, or affiliation..."
                        )}
                        noQueryMessage={i18next.t(
                          "Search for persons by name, identifier, or affiliation..."
                        )}
                        // Disable UI-side filtering of search results
                        search={(options) => options}
                        suggestionAPIUrl="/api/names"
                        serializeSuggestions={(suggestions) =>
                          serializeSuggestions(
                            suggestions,
                            showPersonForm,
                            autocompleteNames
                          )
                        }
                        onValueChange={onPersonSearchChange}
                        {...getFieldData({
                          fieldPath: familyNameFieldPath,
                          fieldRepresentation: "compact",
                        })}
                      />
                    )}
                    {showPersonForm && (
                      <div>
                        <Form.Group widths="equal">
                          <TextField
                            fieldPath={familyNameFieldPath}
                            onBlur={() => handleBlur(familyNameFieldPath)}
                          />
                          <TextField
                            fieldPath={givenNameFieldPath}
                            onBlur={() => handleBlur(givenNameFieldPath)}
                          />
                        </Form.Group>
                        <Form.Group widths="equal">
                          <IdentifiersField
                            className="modal-identifiers-field"
                            options={personIdentifiersSchema}
                            fieldPath={identifiersFieldPath}
                            selectOnBlur={false}
                            validateOnBlur
                          />
                        </Form.Group>
                        <RORAffiliationsField
                          multiple={true}
                          fieldPath={affiliationsFieldPath}
                          allowAdditions={false}
                        />
                      </div>
                    )}
                  </div>
                )}
                {_get(values, typeFieldPath) ===
                  CREATIBUTOR_TYPE.ORGANIZATION && (
                  <div>
                    <RORAffiliationsField
                      fieldPath={affiliationFullNameFieldPath}
                      onBlur={() => handleBlur(affiliationFullNameFieldPath)}
                      allowAdditions={false}
                      {...getFieldData({ fieldPath: fullNameFieldPath })}
                      label={
                        <FieldLabel
                          htmlFor={fullNameFieldPath}
                          label={i18next.t("Organization name")}
                        />
                      }
                      modalHeader={i18next.t("Organization name")}
                    />
                  </div>
                )}
                {!isCreator && (
                  <LocalVocabularySelectField
                    type="contributor-types"
                    fieldPath={roleFieldPath}
                    clearable
                    optionsListName="contributor-types"
                    onBlur={() => handleBlur(roleFieldPath)}
                    {...getFieldData({ fieldPath: roleFieldPath })}
                  />
                )}
              </Form>
            </Modal.Content>
            <Modal.Actions>
              <Button
                name="cancel"
                onClick={() => {
                  resetForm();
                  closeModal();
                }}
                icon="remove"
                content={i18next.t("Cancel")}
                floated="left"
              />
              {initialAction === ModalActions.ADD && (
                <Button
                  name="submit"
                  type="submit"
                  onMouseDown={() => {
                    handleAction("saveAndContinue");
                  }}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") {
                      handleAction("saveAndContinue");
                    }
                  }}
                  primary
                  icon="checkmark"
                  content={saveAndContinueLabel}
                />
              )}
              <Button
                name="submit"
                type="submit"
                onMouseDown={() => {
                  handleAction("saveAndClose");
                }}
                onKeyDown={(e) => {
                  if (e.key === "Enter") {
                    handleAction("saveAndClose");
                  }
                }}
                primary
                icon="checkmark"
                content={i18next.t("Save")}
              />
            </Modal.Actions>
          </Modal>
        );
      }}
    </Formik>
  );
};

CreatibutorsModal.propTypes = {
  autocompleteNames: PropTypes.string,
  initialCreatibutor: PropTypes.object,
  initialAction: PropTypes.oneOf([
    "add",
    "edit",
    "saveAndContinue",
    "saveAndClose",
  ]),
  addLabel: PropTypes.string,
  editLabel: PropTypes.string,
  schema: PropTypes.string,
  onCreatibutorChange: PropTypes.func.isRequired,
  trigger: PropTypes.node,
  nameTypeHelpText: PropTypes.string,
};
CreatibutorsModal.defaultProps = {
  initialCreatibutor: {
    nameType: CREATIBUTOR_TYPE.PERSON,
    fullName: "",
    affiliations: [],
    authorityIdentifiers: [],
  },
  autocompleteNames: "search",
  nameTypeHelpText: i18next.t(
    "Choose if the author is a person or an organization."
  ),
};
