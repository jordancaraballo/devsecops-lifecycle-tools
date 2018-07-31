#!/bin/bash
# Script to run oscap-docker vulnerability scan and parse its scores.
# If for any chance there is a vulnerability, a fail will be triggered
# on bamboo. Systems are expected to be patched before running on workflow.
# Author: Jordan A. Caraballo-Vega

## Set command to run oscap-docker
## Red Hat example
output=$(cat base_scan_result_debian.txt)
#output=$(sudo oscap-docker image-cve registry.access.redhat.com/rhel7)

## Debian example
# Run oscap-docker scan
#sudo oscap-docker image debian_image xccdf \
#eval --profile xccdf_org.ssgproject.content_profile_common \
#/usr/share/xml/scap/ssg/content/ssg-debian8-ds.xml > base_scan_result.txt

## Vulnerabilities counter
numfails=0
numunkn=0
numnotapp=0
numpass=0
numnotch=0

## Parse lines from output and check if there are vulnerabilities
while read -r line
do
    clean_line=( $line )
    # Check last work from line
    if   [ ${clean_line[1]-0} == "pass" ]; then
        numpass=$((numpass+1))  
    elif [ ${clean_line[1]-0} == "fail" ]; then
        numfails=$((numfails+1))
    elif [ ${clean_line[1]-0} == "unknown" ]; then
        numunkn=$((numunkn+1))
    elif [ ${clean_line[1]-0} == "notapplicable" ]; then
        numnotapp=$((numnotapp+1))
    elif [ ${clean_line[1]-0} == "notchecked" ]; then
        numnotch=$((numnotch+1))
fi

# Trigger call using $output
done <<< "$output"

total=$(( $numpass + $numfails ))
percentage=`expr 200 \* $numpass / $total % 2 + 100 \* $numpass / $total`

echo "Compliance Score ${numpass}/${total} = $percentage%, ${numunkn}-unknown, ${numnotapp}-notapplicable, ${numnotch}-notchecked."  
exit 0
