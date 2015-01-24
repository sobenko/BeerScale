<?php
    $file = "keg1.txt";
    $f = fopen($file, "r");
    while ( $line = fgets($f, 1000) ) {
    print $line;
    }
?>
