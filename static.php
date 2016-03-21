<?php

function myTest() {
  static $x=0;
  static $loadedConfigs = array();
  $loadedConfigs[$x]="123";
  
  echo $x;
  var_dump($loadedConfigs);
  
  $x++;
}

myTest();
myTest();
myTest();
myTest();

?>