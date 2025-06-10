#!/bin/bash

# Define some basic environmental variables before launching the suite
 
# Load the analysis3 conda environment
module use /g/data/xp65/public/modules
module load conda/analysis3-25.02

# Root directory for this repo
export ROOT=/g/data/su28/tools/su28_catalog
export MODULES=${ROOT}/src/su28_catalog

# Append to our python path
export PYTHONPATH=${MODULES}:${PYTHONPATH}

echo " INFO : PYTHONPATH=${PYTHONPATH}"
echo " INFO : PATH=${PATH}"