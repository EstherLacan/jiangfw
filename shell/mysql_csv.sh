#!/bin/bash
mysql_host=localhost
mysql_user=root
mysql_pass=root
database=mhealth_business
datetimestamp=$(date +"%Y-%m-%d")
outputfile="/tmp/active_User_$datetimestamp.csv"
MYSQL_CSV_FORMAT="fields terminated by ',' optionally enclosed by '\"' escaped by '\"' lines terminated by '\r\n'"  
#echo "$outputfile" 
  
mysql -p$mysql_pass --default-character-set=gbk -t --verbose $database <<EOF
use $database;  
SELECT
	r.User_ID,
	u.User_FullName,
	CASE u.User_Sex 
            WHEN 1 THEN '男'
            WHEN 2 THEN '女'
            ELSE '未知'
  END as User_Sex,
	u.User_Phone,
  u.User_Mail,
	u.User_Address,
	from_unixtime(File_Start_Time,'%Y-%m-%d') datetime,
  count(1) as '测量次数'
FROM
	m_ecg_record_r r
INNER JOIN m_ecg_user u ON r.User_ID = u.User_ID
WHERE
	from_unixtime(File_Start_Time, '%Y-%m-%d') = DATE_FORMAT(
		date_sub(now(), INTERVAL 1 DAY),
		'%Y-%m-%d'
	)
GROUP BY r.User_ID,
	u.User_Name,u.User_Sex ,u.User_Phone,u.User_Mail,
	u.User_Address,datetime into outfile '${outputfile}' $MYSQL_CSV_FORMAT;
EOF
  
echo "===== content in ${outputfile} ====="  
cat ${outputfile} 
