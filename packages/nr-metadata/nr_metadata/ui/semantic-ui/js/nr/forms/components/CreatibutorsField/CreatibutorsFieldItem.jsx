// This file is part of Invenio-RDM-Records
// Copyright (C) 2020-2023 CERN.
// Copyright (C) 2020-2022 Northwestern University.
// Copyright (C) 2021 New York University.
//
// Invenio-RDM-Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import { i18next } from "@translations/nr/i18next";
import _get from "lodash/get";
import React from "react";
import { useDrag, useDrop } from "react-dnd";
import { Button, Label, List, Ref } from "semantic-ui-react";
import { CreatibutorsModal } from "./CreatibutorsModal";
import PropTypes from "prop-types";
import { useFormConfig, NestedErrors } from "@js/oarepo_ui/forms";
import { CreatibutorIdentifier } from "@nr/search";

export const CreatibutorsFieldItem = ({
  compKey,
  index,
  replaceCreatibutor,
  removeCreatibutor,
  moveCreatibutor,
  addLabel,
  editLabel,
  initialCreatibutor,
  displayName,
  schema,
  autocompleteNames,
  nameTypeHelpText,
}) => {
  const dropRef = React.useRef(null);
  // eslint-disable-next-line no-unused-vars
  const [_, drag, preview] = useDrag({
    item: { index, type: "creatibutor" },
  });
  const [{ hidden }, drop] = useDrop({
    accept: "creatibutor",
    hover(item, monitor) {
      if (!dropRef.current) {
        return;
      }
      const dragIndex = item.index;
      const hoverIndex = index;

      // Don't replace items with themselves
      if (dragIndex === hoverIndex) {
        return;
      }

      if (monitor.isOver({ shallow: true })) {
        moveCreatibutor(dragIndex, hoverIndex);
        item.index = hoverIndex;
      }
    },
    collect: (monitor) => ({
      hidden: monitor.isOver({ shallow: true }),
    }),
  });

  const {
    formConfig: { vocabularies },
  } = useFormConfig();

  const renderRole = (role) => {
    return (
      role && (
        <Label size="tiny">
          {
            vocabularies["contributor-types"].all.find(
              (item) => item.value === role.id
            ).text
          }
        </Label>
      )
    );
  };
  const authorityIdentifiers = _get(
    initialCreatibutor,
    "authorityIdentifiers",
    []
  );
  // Initialize the ref explicitely
  drop(dropRef);
  return (
    <Ref innerRef={dropRef} key={compKey}>
      <React.Fragment>
        <List.Item
          key={compKey}
          className={
            hidden ? "deposit-drag-listitem hidden" : "deposit-drag-listitem"
          }
          id={compKey}
        >
          <List.Content floated="right">
            <CreatibutorsModal
              key={`edit-creatibutor-modal-${index}`}
              addLabel={addLabel}
              editLabel={editLabel}
              onCreatibutorChange={(selectedCreatibutor) => {
                replaceCreatibutor(index, selectedCreatibutor);
              }}
              nameTypeHelpText={nameTypeHelpText}
              initialCreatibutor={initialCreatibutor}
              schema={schema}
              autocompleteNames={autocompleteNames}
              initialAction="edit"
              trigger={
                <Button size="mini" primary type="button">
                  {i18next.t("Edit")}
                </Button>
              }
            />
            <Button
              size="mini"
              type="button"
              onClick={() => removeCreatibutor(index)}
            >
              {i18next.t("Remove")}
            </Button>
          </List.Content>
          <Ref innerRef={drag}>
            <List.Icon name="bars" className="drag-anchor" />
          </Ref>
          <Ref innerRef={preview}>
            <List.Content>
              <List.Description>
                <span className="creatibutor">
                  {displayName}
                  <span className="mr-5 ml-5">
                    <CreatibutorIdentifier
                      identifiers={authorityIdentifiers}
                      creatibutorName={initialCreatibutor?.fullName}
                    />
                  </span>
                  {renderRole(initialCreatibutor?.contributorType)}
                </span>
              </List.Description>
            </List.Content>
          </Ref>
        </List.Item>
        <NestedErrors fieldPath={compKey} />
      </React.Fragment>
    </Ref>
  );
};

CreatibutorsFieldItem.propTypes = {
  compKey: PropTypes.string.isRequired,
  index: PropTypes.number.isRequired,
  replaceCreatibutor: PropTypes.func.isRequired,
  removeCreatibutor: PropTypes.func.isRequired,
  moveCreatibutor: PropTypes.func.isRequired,
  addLabel: PropTypes.node,
  editLabel: PropTypes.node,
  initialCreatibutor: PropTypes.object.isRequired,
  displayName: PropTypes.string,
  schema: PropTypes.string.isRequired,
  autocompleteNames: PropTypes.oneOfType([PropTypes.bool, PropTypes.string]),
  nameTypeHelpText: PropTypes.string,
};

CreatibutorsFieldItem.defaultProps = {
  addLabel: undefined,
  editLabel: undefined,
  displayName: undefined,
  autocompleteNames: undefined,
};
