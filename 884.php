<?php
$a = "张先生";
$tip = $a.",欢迎您在慕课网学习PHP！";

$b = "东边日出西边雨";
$b .= ",道是无晴却有晴";
$c = "东边日出西边雨";
$c = $c.",道是无晴却有晴";
echo $tip;
echo $tip."<br />";
echo $b."<br />";
echo $c."<br />";
$key='1.11';

$key   = str_replace('.', '->', $key);
echo $key;
?>