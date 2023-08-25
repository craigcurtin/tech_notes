#!/usr/bin/env bash

# for file in *.txt; do mv "$file" "${file%.txt}.py"; done

set -x
for MY_FILE in *.webloc; 
do
        # cat the file, grep for string .... create new file
        cat "$MY_FILE" | grep "<string>" | sed 's/<string>/URL=/' | sed 's/<\/string>//' > "_${MY_FILE%.webloc}.url"; 
done




