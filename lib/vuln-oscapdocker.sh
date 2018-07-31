#!/bin/bash
# Script to run oscap-docker vulnerability scan and parse its scores.
# If for any chance there is a vulnerability, a fail will be triggered
# on bamboo. Systems are expected to be patched before running on workflow.
# Author: Jordan A. Caraballo-Vega

## Set command to run oscap-docker
## Red Hat example
output=$(cat vuln_scan_result_debian.txt)
#output=$(sudo oscap-docker image-cve registry.access.redhat.com/rhel7)

## Debian example
#sudo oscap-docker image debian_image oval eval \
#oval-definitions-jessie.xml

## Vulnerabilities counter
numvuln=0
numunkn=0

## Parse lines from output and check if there are vulnerabilities
while read -r line
do
    # Check last work from line
    if [ ${line##* } == "true" ]; then
        numvuln=$((numvuln+1))  
    elif [ ${line##* } == "unknown" ]; then
        numunkn=$((numunkn+1))
    fi
# Trigger call using $output
done <<< "$output"

echo "${numvuln} Vulnerabilities found, ${numunkn} Unknown checks."  
exit 0
