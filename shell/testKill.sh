#!/bin/bash


test2()
{
echo "erro"
return "234"
}
DATE=`test2`
echo $?
echo "hubaoxi"
echo $DATE
echo $(($DATE + 48))

