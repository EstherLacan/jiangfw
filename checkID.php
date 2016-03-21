<?php
/**
 * 函数说明：验证身份证是否真实
 * 注：加权因子和校验码串为互联网统计  尾数自己测试11次 任意身份证都可以通过
 * 传递参数：
 * $number身份证号码
 * 返回参数：
 * true验证通过
 * false验证失败
 */
function isIdCard($number) {
    $sigma = '';
    //加权因子 
    $wi = array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);
    //校验码串 
    $ai = array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');
    //按顺序循环处理前17位 
    for ($i = 0;$i < 17;$i++) { 
        //提取前17位的其中一位，并将变量类型转为实数 
        $b = (int) $number{$i}; 
        //提取相应的加权因子 
        $w = $wi[$i]; 
        //把从身份证号码中提取的一位数字和加权因子相乘，并累加 得到身份证前17位的乘机的和 
        $sigma += $b * $w;
    }
//echo $sigma;die;
    //计算序号  用得到的乘机模11 取余数
    $snumber = $sigma % 11; 
    //按照序号从校验码串中提取相应的余数来验证最后一位。 
    $check_number = $ai[$snumber];
    if ($number{17} == $check_number) {
        return true;
    } else {
        return false;
    }
}
//eg
if (!isIdCard('000000000000000001')) {
echo "身份证号码不合法";
} else {
echo "身份证号码正确";
}
?>