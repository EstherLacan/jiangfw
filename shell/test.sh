#!/bin/bash
subhome=/home
echo `pwd`
echo $0
echo `dirname $0`
cd /
echo `pwd`
sleep 5
(cd $subhome && /home/xitong/test2.sh)
echo `pwd`
cd home/xitong/
echo `pwd`
