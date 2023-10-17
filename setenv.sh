#!/bin/bash
REPO_PATH="$PWD"
PYTHON_VERSION="3.9.1"

export PYENV_ROOT="${HOME}/.pyenv"
if [ ! -d ${PYENV_ROOT} ]; then
  echo ".pyenv not present so installing pyenv..."
  curl https://pyenv.run | bash
fi

export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"

pyenv install "${PYTHON_VERSION}" -s
pyenv global "${PYTHON_VERSION}"

if [ ! -d ".venv" ]; then
  echo "Creating virtual env with Python ${PYTHON_VERSION}"
  pip install --upgrade pip
  pip install --upgrade pipenv
  export PIPENV_VENV_IN_PROJECT=1
  pipenv --python "${PYTHON_VERSION}"
fi

pipenv shell
pipenv sync --dev
