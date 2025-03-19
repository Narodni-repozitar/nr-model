// This file is part of Invenio-RDM-Records
// Copyright (C) 2020-2023 CERN.
// Copyright (C) 2020-2022 Northwestern University.
// Copyright (C) 2021 New York University.
//
// Invenio-RDM-Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import { i18next } from "@translations/nr/i18next";
import React from "react";
import { useDrag, useDrop } from "react-dnd";
import { Button, List, Ref } from "semantic-ui-react";
import { RelatedItemsModal } from "./RelatedItemsModal";
import PropTypes from "prop-types";
import { NestedErrors } from "@js/oarepo_ui/forms";

export const RelatedItemsFieldItem = ({
  compKey,
  index,
  replaceRelatedItem,
  removeRelatedItem,
  moveRelatedItem,
  addLabel,
  editLabel,
  initialRelatedItem,
  displayName,
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
        moveRelatedItem(dragIndex, hoverIndex);
        item.index = hoverIndex;
      }
    },
    collect: (monitor) => ({
      hidden: monitor.isOver({ shallow: true }),
    }),
  });

  // Initialize the ref explicitely
  drop(dropRef);
  return (
    <Ref innerRef={dropRef} key={compKey}>
      <React.Fragment>
        <List.Item
          id={compKey}
          key={compKey}
          className={
            hidden ? "deposit-drag-listitem hidden" : "deposit-drag-listitem"
          }
        >
          <List.Content floated="right">
            <RelatedItemsModal
              key={`edit-related-item-modal-${index}`}
              addLabel={addLabel}
              editLabel={editLabel}
              onRelatedItemChange={(selectedRelatedItem) => {
                replaceRelatedItem(index, selectedRelatedItem);
              }}
              initialRelatedItem={initialRelatedItem}
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
              onClick={() => removeRelatedItem(index)}
            >
              {i18next.t("Remove")}
            </Button>
          </List.Content>
          <Ref innerRef={drag}>
            <List.Icon name="bars" className="drag-anchor" />
          </Ref>
          <Ref innerRef={preview}>
            <List.Content>
              <List.Description>{displayName}</List.Description>
            </List.Content>
          </Ref>
        </List.Item>
        <NestedErrors fieldPath={compKey} />
      </React.Fragment>
    </Ref>
  );
};

RelatedItemsFieldItem.propTypes = {
  compKey: PropTypes.string.isRequired,
  index: PropTypes.number.isRequired,
  replaceRelatedItem: PropTypes.func.isRequired,
  removeRelatedItem: PropTypes.func.isRequired,
  moveRelatedItem: PropTypes.func.isRequired,
  addLabel: PropTypes.node,
  editLabel: PropTypes.node,
  initialRelatedItem: PropTypes.object.isRequired,
  displayName: PropTypes.oneOfType([PropTypes.string, PropTypes.object]),
};

RelatedItemsFieldItem.defaultProps = {
  addLabel: undefined,
  editLabel: undefined,
  displayName: undefined,
};
