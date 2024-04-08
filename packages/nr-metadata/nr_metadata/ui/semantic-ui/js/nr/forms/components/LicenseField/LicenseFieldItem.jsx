// This file is part of React-Invenio-Deposit
// Copyright (C) 2021 CERN.
// Copyright (C) 2021-2022 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
//
// React-Invenio-Deposit is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import { Button, Grid } from "semantic-ui-react";
import { i18next } from "@translations/nr/i18next";
import PropTypes from "prop-types";
import { useFormikContext } from "formik";
import { getTitleFromMultilingualObject } from "@js/oarepo_ui";

export const LicenseFieldItem = ({ license, fieldPath }) => {
  const { setFieldValue } = useFormikContext();
  return (
    <Grid key={license.key}>
      <Grid.Column width={10}>
        {getTitleFromMultilingualObject(license.title)}
      </Grid.Column>
      <Grid.Column textAlign="right" width={6}>
        <Button
          size="mini"
          type="button"
          onClick={() => {
            setFieldValue(fieldPath, "");
          }}
        >
          {i18next.t("Remove")}
        </Button>
      </Grid.Column>
    </Grid>
  );
};

LicenseFieldItem.propTypes = {
  license: PropTypes.object.isRequired,
  fieldPath: PropTypes.string.isRequired,
};
