#!/bin/bash
cd /home/ec2-user
echo "start"
echo "[" > monitoring-data.json
count=0
ps -eo pcpu,pid,user,args | tail -n +2 | sort -k 1 -r | head -5 | while read line
do
    echo "Save process: $count"
    cpu_u=$(echo $line | cut -d ' ' -f 1)
    pid=$(echo $line | cut -d ' ' -f 2)
    user=$(echo $line | cut -d ' ' -f 3)
    echo "{" >> monitoring-data.json
    echo "\"pid\":$pid," >> monitoring-data.json
    echo "\"cpu\":$cpu_u," >> monitoring-data.json
    echo "\"user\":\"$user\"" >> monitoring-data.json
    if ((count < 4))
    then
        echo "}," >> monitoring-data.json
    else
        echo "}" >> monitoring-data.json
    fi
    ((count++))
done
echo "]" >> monitoring-data.json
aws s3 cp monitoring-data.json s3://cgn-aws-22-2-neuefische-website-1234/
echo "done"