<?php 
define("PI1",3.14);
$p = "PI1";
$is1=defined($p);
$is2=defined("PI2");
echo $is2;
if ($is1) {
    echo "yes\n";
}else {
    echo "no\n";
}
echo "pi11111111111111111111111\n";
echo M_PI."\n";
echo M_1_PI."\n";
echo M_2_PI."\n";
echo M_PI_2."\n";
echo M_PI_4."\n";

$a='bb';
$$a=0;
echo $bb;
var_dump($$a);


?>