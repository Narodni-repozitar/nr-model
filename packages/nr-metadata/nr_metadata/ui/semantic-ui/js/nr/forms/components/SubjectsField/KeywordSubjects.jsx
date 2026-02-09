import React from "react";
import PropTypes from "prop-types";
import { Icon, Button, Label } from "semantic-ui-react";
import { i18next } from "@translations/nr/i18next";

export const KeywordSubjects = ({ keywordSubjects, handleSubjectRemoval }) => {
  return (
    keywordSubjects?.length > 0 && (
      <React.Fragment>
        {keywordSubjects.map(({ subject, id }, index) => (
          <React.Fragment key={id}>
            {subject?.map((s, i) => (
              <Label className="keyword-subjects label" image key={i}>
                {s.lang}
                <Label.Detail className="pr-0">
                  {s.value}
                  <Button
                    className="transparent p-0 m-0 rel-pl-1"
                    onClick={() => handleSubjectRemoval(id, s.lang)}
                    type="button"
                    aria-label={i18next.t("Remove keyword")}
                  >
                    <Icon name="close" size="small" />
                  </Button>
                </Label.Detail>
              </Label>
            ))}
            {index + 1 !== keywordSubjects?.length && (
              <span className="rel-mr-1 rel-ml-1">|</span>
            )}
          </React.Fragment>
        ))}
      </React.Fragment>
    )
  );
};

KeywordSubjects.propTypes = {
  keywordSubjects: PropTypes.array.isRequired,
  handleSubjectRemoval: PropTypes.func.isRequired,
};
