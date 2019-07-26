#!/bin/bash

# --------------------------------------- VARIABLES -------------------------------------------
# runTest is a variable to control whether ares will run a test against a specific port
#       it is initially set to false at the default, and will only change to true if
#       the port number of this test is found in the masscan result file.
# port is simply a string that will print the port number and its service when called.

runTest=false
port="8080"


# ------------------------------- CHECK IF IP WAS SUPPLIED ------------------------------------
if [ -z "$1" ]; then
        echo "Usage: ./NAME.sh X.X.X.X"
        echo "Please supply IP address!"
        exit 1
   fi


# -------------------------------- READ PORTS INTO ARRAY  -------------------------------------
# Setting the array of ports by reading the masscan results into its indexes.

portArray=$'\r\n' GLOBIGNORE='*' command eval  'ports=($(cat /tmp/ports.txt))'


# ------------------------------ CHECK IF PORT IS IN ARRAY ------------------------------------
# Conditional if statement checks the indexes of the ports array for the port in question.
#       IMPORTANT: Ensure that the port number in the if statement has 1 space on both its
#               right and left sides (Example: " 80 "), otherwise, ports containing the one
#               being searched for (Example 8080 contains the string 80) will cause false
#               positives.

if [[ " ${ports[*]} " == *" 8080 "* ]]; then
        runTest=true
   fi


# ------------------------ IF PORT IS IN ARRAY, PROCEED WITH TESTS ----------------------------
if [ $runTest == true ]; then
        echo "Enumerating port ${port}"
        echo "------------------------------- Nmap Scan -------------------------------------"
        nmap -n -sV -p 8080  $1
        echo ""
        echo "------------------------------ Banner Grab ------------------------------------"
        nmap -sV -p 8080 --script=banner $1
        echo ""
        echo "------------------------------ Nikto Scan -------------------------------------"
        perl /nikto-master/program/nikto.pl -h $1 -port 8080
        echo ""
        echo "------------------------- Gobuster Brute Force --------------------------------"
        gobuster -t 25 -u http://$1:8080 -w /Wordlists/Dirs-220k.txt
   else
        echo "Port ${port} closed, no tests to perform."
   fi
