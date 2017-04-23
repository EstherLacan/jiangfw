#!/bin/bash
#This script edit by badboy connect leezhenhua17@163.com
#This script used by repair tables
mysql_host=localhost
mysql_user=root
mysql_pass=root
database=test_nj

tables=$(mysql -h$mysql_host -u$mysql_user -p$mysql_pass $database -A -Bse "show tables")
for arg in $tables
do
check_status=$(mysql -h$mysql_host -u$mysql_user -p$mysql_pass $database -A -Bse "check table $arg" | awk '{ print $4 }')
if [ "$check_status" = "OK" ]
then
echo "$arg is ok"
else
echo $(mysql -h$mysql_host -u$mysql_user -p$mysql_pass $database -A -Bse "repair table $arg")

fi
echo $(mysql -h$mysql_host -u$mysql_user -p$mysql_pass $database -A -Bse "optimize table $arg")
done