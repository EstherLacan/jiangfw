<?php
$a=array('a'=>1,'b'=>2,'c'=>3,'d'=>4,'e'=>5);
// var_dump($a);
// foreach ($a as $k => $v) {
//     $v=$v+3;
//     echo $v."\n";
// }
var_dump($a);
foreach ($a as $k => &$v) {
    $v=$v+3;
    echo $v."\n";
}
var_dump($a);
foreach ($a as $k1 => $v1) {
    echo $k1.":".$v1."\n";
    $v1=&$a[$k1];
}
    //echo $k.":".$v."\n";
var_dump($a);