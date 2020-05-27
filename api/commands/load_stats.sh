#!/bin/bash -l

set -e

if type "pipenv" >> /dev/null 2>&1; then
    PY_COMMAND="pipenv run python"
else
    PY_COMMAND="python"
fi

exec $PY_COMMAND manage.py runscript stats_loader >> stats_loader.log 2>&1
