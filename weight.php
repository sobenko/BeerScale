<?php
error_reporting(E_ALL);
ini_set('display_errors', TRUE);
ini_set('display_startup_errors', TRUE);

//exec("/bin/stty -F /dev/ttyACM0 9600 sane raw cs8 hupcl cread clocal -echo -onlcr ");
$fp=fopen("/dev/ttyACM0","r");
if(!$fp) die("Can't open device");
while(true){
 sleep(2000);
 $data = fgets($fp);
 echo $data;
}

?>
