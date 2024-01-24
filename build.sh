#!/bin/bash

# Compiles the model into nr-metadata package and oarepo-model-builder-nr package.
# To run, call this script without any arguments.
#
# The following steps are called:
#
# compile_nr_metadata     - creates .venv-builder, installs it and runs it on model files,
#                           creating packages/nr-metadata
# test_nr_metadata        - creates a repository with the model and runs basic tests
# build_nr_metadata       - create a build of nr_metadata
# create_builder_plugin   - packages the model as oarepo-builder-builder-nr
# test_builder_plugin     - runs the packaged plugin on sample model to check that it generates
#                           correctly
#
# For debugging, pass $1 to point to directory which contains one of the following source packages.
# They will be installed in editable mode:
#
# oarepo-model-builder, oarepo-model-builder-vocabularies,
# oarepo-model-builder-ui, oarepo-model-builder-multilingual
#
# If you pass --no-clear in $1, virtual environments will not be cleared and packages reinstalled.

set -e

base_dir=$(cd "$(dirname "$0")" && pwd)

MODEL_VERSION=2.0

MODEL_BUILDER_VENV="$base_dir/.venv-builder"
TEST_VENV="$base_dir/.venv-tests"
MODEL_BUILDER_TEST_BUILDER_VENV="$base_dir/.venv-builder-tests-builder"
MODEL_BUILDER_TEST_VENV="$base_dir/.venv-builder-tests"

# for debugging, set this to the local package dir
NO_CLEAR="$1"

OAREPO_VERSION=${OAREPO_VERSION:-11}
OAREPO_VERSION_MAX=$((OAREPO_VERSION+1))

# region commands

compile_nr_metadata() {
  cd "$base_dir/packages/nr-metadata"
  create_builder_venv
  rm -rf nr_metadata/common
  rm -rf nr_metadata/documents

  decho "Compilling common metadata"
  "$MODEL_BUILDER_VENV"/bin/oarepo-compile-model nr-metadata.yaml -vvv \
      --include nr-common-metadata="$base_dir/models/nr_common_metadata_${MODEL_VERSION}.yaml" \
      --include nr-datatypes="$base_dir/models/nr_datatypes_${MODEL_VERSION}.yaml"

  decho "Compilling nr-documents"
  "$MODEL_BUILDER_VENV"/bin/oarepo-compile-model nr-documents.yaml -vvv \
      --include nr-common-metadata="$base_dir/models/nr_common_metadata_${MODEL_VERSION}.yaml" \
      --include nr-datatypes="$base_dir/models/nr_datatypes_${MODEL_VERSION}.yaml" \
      --include nr-documents="$base_dir/models/nr_documents_${MODEL_VERSION}.yaml"
  copy_version ../../version nr_metadata/version.py
  cp ../../README.md .
}

test_nr_metadata() {
  cd "$base_dir/packages/nr-metadata"
  create_metadata_test_venv
  "$TEST_VENV"/bin/pytest tests
}

build_nr_metadata() {
  cd "$base_dir/packages/nr-metadata"
  test -d build && rm -rf build || true
  test -d dist && rm -rf dist || true
  "$MODEL_BUILDER_VENV"/bin/python setup.py sdist bdist_wheel
}

create_builder_plugin() {
  cd "$base_dir/packages/oarepo-model-builder-nr"
  cp ../../models/*.yaml oarepo_model_builder_nr/models/
  copy_version ../../version oarepo_model_builder_nr/version.py
  cp ../../README.md .
  test -d build && rm -rf build || true
  test -d dist && rm -rf dist || true
  "$MODEL_BUILDER_VENV"/bin/python setup.py sdist bdist_wheel
}

test_builder_plugin() {
  cd "$base_dir/packages/oarepo-model-builder-nr"

  if [ -d tests/model ] ; then
    rm -rf tests/model
  fi

  create_builder_test_builder_venv
  "$MODEL_BUILDER_TEST_BUILDER_VENV"/bin/oarepo-compile-model --output-directory tests/model ../../examples/model.yaml

  create_builder_test_venv
  "$MODEL_BUILDER_TEST_VENV"/bin/pytest tests/test_import.py
}

#endregion

# region helper functions

create_builder_venv() {
  if [ "$NO_CLEAR" == "--no-clear" ] ; then
    decho "Not clearing builder's virtual environment"
  else
    create_virtual_environment "$MODEL_BUILDER_VENV"

    install_package "$MODEL_BUILDER_VENV" oarepo-model-builder
    install_package "$MODEL_BUILDER_VENV" oarepo-model-builder-vocabularies
    install_package "$MODEL_BUILDER_VENV" oarepo-model-builder-ui
    install_package "$MODEL_BUILDER_VENV" oarepo-model-builder-multilingual
  fi
}

create_metadata_test_venv() {
  if [ "$NO_CLEAR" == "--no-clear" ] ; then
    decho "Not clearing test's virtual environment"
  else
    create_virtual_environment "$TEST_VENV"
  fi
  "$TEST_VENV"/bin/pip install "oarepo>=$OAREPO_VERSION,<$OAREPO_VERSION_MAX"
  "$TEST_VENV"/bin/pip install -e '.[tests]'
}

create_builder_test_builder_venv() {
  if [ "$NO_CLEAR" == "--no-clear" ] ; then
    decho "Not clearing builder's virtual environment"
  else
    create_virtual_environment "$MODEL_BUILDER_TEST_BUILDER_VENV"

    install_package "$MODEL_BUILDER_TEST_BUILDER_VENV" oarepo-model-builder
    install_package "$MODEL_BUILDER_TEST_BUILDER_VENV" oarepo-model-builder-vocabularies
    install_package "$MODEL_BUILDER_TEST_BUILDER_VENV" oarepo-model-builder-ui
    install_package "$MODEL_BUILDER_TEST_BUILDER_VENV" oarepo-model-builder-multilingual
  fi
  "$MODEL_BUILDER_TEST_BUILDER_VENV"/bin/pip install dist/oarepo_model_builder_nr*.whl
}

create_builder_test_venv() {
  if [ "$NO_CLEAR" == "--no-clear" ] ; then
    decho "Not clearing builder's virtual environment"
  else
    create_virtual_environment "$MODEL_BUILDER_TEST_VENV"
  fi
  "$MODEL_BUILDER_TEST_VENV"/bin/pip install "oarepo>=$OAREPO_VERSION,<$OAREPO_VERSION_MAX"
  "$MODEL_BUILDER_TEST_VENV"/bin/pip install ../nr-metadata/dist/*.tar.gz
  "$MODEL_BUILDER_TEST_VENV"/bin/pip install -e "tests/model[tests]"
}

create_virtual_environment() {
  decho "creating virtual environment $1"
  if [ -d "$1" ] ; then
    rm -rf "$1"
  fi
  python3 -m venv "$1"

  "$1"/bin/pip install -U setuptools pip wheel
}

install_package() {
  uppercase_package=$(echo "$2" | tr '[:lower:]' '[:upper:]' | sed 's/-/_/g')
  package_dir="${!uppercase_package}"

  if [ "$package_dir" != "" ] && [ -d "$package_dir" ] ; then
    decho "installing local package $package_dir to $1"
    "$1/bin/pip" install -e "$package_dir" --config-settings editable_mode=compat
  else
    decho "installing pypi package $2 to $1"
    "$1/bin/pip" install "$2"
  fi
}


copy_version() {
  version=$(cat "$1")
  cat <<EOF >"$2"
__version__ = "${version}"
EOF
}

decho() {
  GREEN='\033[0;32m'
  NC='\033[0m' # No Color
  echo -e "${GREEN}$1${NC}"
}

#endregion

# region main

compile_nr_metadata
test_nr_metadata
build_nr_metadata
create_builder_plugin
test_builder_plugin

#endregion