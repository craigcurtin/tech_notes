#!/usr/bin/env bash

set -euxo pipefail

HEADER=/tmp/$$_Head
FOOTER=/tmp/$$_Tail

# make Header template
cat << EOF > ${HEADER}
[InternetShortcut]
EOF

# make footer Template
cat << EOF > ${FOOTER}
IconIndex=0
EOF

# for file in *.txt; do mv "$file" "${file%.txt}.py"; done
set -x
for MY_FILE in *.webloc; 
do
        # cat the file, grep for string .... create new file
        BODY="_${MY_FILE%.webloc}.url"
        TMP_BODY="/tmp/${BODY}"
        # reminder ... XML had tab in front ...
        cat "$MY_FILE" | grep "<string>" | sed 's/.*<string>/URL=/' | sed 's/<\/string>//' > "${TMP_BODY}"; 
        cat "${HEADER}" "${TMP_BODY}" "${FOOTER}" > "${BODY}"
        #rm "${TMP_BODY}"
done

#clean up
rm "${HEADER}" "${FOOTER}"



