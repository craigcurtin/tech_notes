#!/usr/bin/env bash

# for file in *.txt; do mv "$file" "${file%.txt}.py"; done

set -x
for MY_FILE in *.webloc; do cp "$MY_FILE" "${MY_FILE%.webloc}.url"; done




