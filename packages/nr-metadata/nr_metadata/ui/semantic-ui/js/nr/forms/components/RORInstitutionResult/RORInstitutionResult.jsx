import * as React from "react";

import { List, Label, Header, Icon } from "semantic-ui-react";
import _join from "lodash/join";
import { getTitleFromMultilingualObject } from "@js/oarepo_ui";

export const RORInstitutionResult = ({ result, handleSelect = () => {}, selected }) => {

  const { title, relatedURI, props } = result;

  const uriLinks =
    relatedURI &&
    Object.entries(relatedURI).map(([name, value]) => {
      return (
        <Label key={name} basic size="mini">
          <a
            onClick={(e) => e.stopPropagation()}
            href={value}
            target="_blank"
            rel="noopener noreferrer"
          >
            <Icon name="external alternate" />
            {name}
          </a>
        </Label>
      );
    });

  const propValues = props ? _join(Object.values(props).filter(prop => prop && prop !== ""), ", "): null;

  const onSelect = (result) => {
    // TODO: here you can convert the result to internal format
    handleSelect(result, selected);
  };

  return (
    <List.Item
      onClick={() => onSelect(result)}
      className="search-external-result-item"
      active={selected}
    >
      <List.Content>
        <Header className="mb-5" size="small">
          {getTitleFromMultilingualObject(title)} {uriLinks}
        </Header>
        <List.Description>{propValues}</List.Description>
      </List.Content>
    </List.Item>
  );
};

export default  RORInstitutionResult;