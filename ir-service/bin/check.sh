
#!/bin/bash
#
# Check there are no unset values in the template.
#

echo checking $1

if grep -q "<no value>" $1 ; then
    exit 1
fi
