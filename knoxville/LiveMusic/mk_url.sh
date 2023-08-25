#!/usr/bin/env bash

set -euxo pipefail

# lets make a template Header and Footer here is document
HEADER=/tmp/$$_Head
FOOTER=/tmp/$$_Tail

# create Header template
cat << EOF > ${HEADER}
[InternetShortcut]
EOF

# create Footer Template
cat << EOF > ${FOOTER}
IconIndex=0
EOF

# for file in *.txt; do mv "$file" "${file%.txt}.py"; done

for MY_FILE in *.webloc; 
do
        # cat the file, grep for string .... create new file
        BODY="_${MY_FILE%.webloc}.url"
        TMP_BODY="/tmp/${BODY}"

        # reminder ... XML had tab in front ...
        # cat input file ... remove the leading and trailing string ... sub in "URL="
        cat "$MY_FILE" | grep "<string>" | sed 's/.*<string>/URL=/' | sed 's/<\/string>//' > "${TMP_BODY}"; 

        # put the Header + TmpBody + Footer together 
        cat "${HEADER}" "${TMP_BODY}" "${FOOTER}" > "${BODY}"

        # clean up the tmp file ...
        rm "${TMP_BODY}"
done

#clean up
rm "${HEADER}" "${FOOTER}"



