#!/usr/bin/env bash

# eval "$(conda shell.bash hook)"

# conda activate flaskapp

# export FLASK_APP=src/seguid_calculator/seguid_flask.py&&export FLASK_ENV=development&&flask run

# echo "press any key to close"
# read -n1 slask


#!/usr/bin/env bash

# eval "$(/home/bjorn/mambaforge/condabin/mamba shell hook)"

eval "$(/home/bjorn/miniforge3/bin/conda shell.bash hook)"
conda activate bjorn311

# source ~/.lib/mamba/bin/activate

export FLASK_APP=src/seguid_calculator2/seguid_flask.py&&export FLASK_ENV=development&&flask run --debug

echo "press any key to close"
read -n1 slask