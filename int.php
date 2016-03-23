<?php
$a=5;
$b=$a;
$c=&$b;
var_dump($a,$b,$c);
$a=10;
$b=100;
var_dump($a,$b,$c);

$arr=array('1',23,TRUE);
print_r($arr);
var_dump($arr);
print_r($a);

$arr2=array('2'=>1,2.3=>2323,34=>TRUE,'12b'=>"adfafsafs");
print_r($arr2);
var_dump($arr2);

print_r($_SERVER);
echo "this is a new row!";
