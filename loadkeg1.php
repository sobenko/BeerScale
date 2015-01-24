<?php
	function mapfloat($x)
	{
		$loadA = 0; // kg
	    $analogvalA = 22.91; // analog reading taken with load A on the load cell

		$loadB = 55; // kg
		$analogvalB = 415.30; // analog reading taken with load B on the load cell
  		return (x-loadA) * (analogvalB-analogvalA)/(loadB-loadA) + analogvalA;
	}

    $file = "keg1.txt";
    $f = fopen($file, "r");
    while ( $line = fgets($f, 1000) ) {
    	print mapfloat($line);
    }
?>
