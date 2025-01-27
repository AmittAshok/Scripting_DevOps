#!/bin/bash
#
#
 log_file="/home/amitt-ashok/logfile/log_file.txt"

 grep -i "INFO" $log_file > info-error-log.txt

 echo "error log find"
