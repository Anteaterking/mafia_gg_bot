#!/bin/bash
# Run from root directory ./
CONDA_ENV_NAME=mafia_gg_bot_dev
CONDA_ENV_FILE=./config/environment.yaml
CONDA_ENV_FILE_DEV=./config/environment-dev.yaml
source deactivate
echo "Building conda env ${CONDA_ENV_NAME}."
ENV_EXISTS=$(conda info --envs | grep ${CONDA_ENV_NAME})
if [[ -z ${ENV_EXISTS} ]]; then
  echo "Creating conda env ${CONDA_ENV_NAME} from ${CONDA_ENV_FILE}."
  conda env create -n ${CONDA_ENV_NAME} -f ${CONDA_ENV_FILE} -f ${CONDA_ENV_FILE_DEV}
else
  echo "Updating conda env ${CONDA_ENV_NAME} from ${CONDA_ENV_FILE}."
  conda env update -n ${CONDA_ENV_NAME} -f ${CONDA_ENV_FILE} -f ${CONDA_ENV_FILE_DEV}
  conda clean -tp --yes
fi
echo "Finished building conda env ${CONDA_ENV_NAME}."
source activate ${CONDA_ENV_NAME}
