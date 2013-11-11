#!/bin/bash

#store arguments
args=("$@")
ELEMENTS=${#args[@])}

echo $ELEMENTS
echo ${args[@]}

python mg-compare-functions-adina.py --user aXXXXX --passwd XXXX --token XXXXXX --ids mgm4509396.3,mgm4509398.3,mgm4509400.3 > abundance.txt

for (( i=0;i<$ELEMENTS;i++)); do 
python mg-display-metadata.py --user XXXX --passwd XXX --token XXXXXX --id mgm${args[${i}]} --verbosity full > mgm${args[${i}]}
done