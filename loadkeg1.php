<?php
	function mapfloat($x)
	{
		$loadA = 0; // kg
	    $analogvalA = 22.91; // analog reading taken with load A on the load cell

		$loadB = 55; // kg
		$analogvalB = 415.30; // analog reading taken with load B on the load cell
  		return (x-loadA) * (analogvalB-analogvalA)/(loadB-loadA) + analogvalA;
	}

	function lbsToOz($lbs)
	{
		//128 oz in a gallon
		// http://www.brewangels.com/Beerformation/Weight.html
		//Light Lager with a FG of 1.008: 8.345 x 1.008 = 8.422 lb/g (round to 8.4)
		//Barley Wine with a FG of 1.030: 8.345 x 1.030 = 8.595 lb/g (round to 8.6)
		$tare = $lbs - 17;
		return ($tare / 8.5) * 128;
	}

    $file = "keg1.txt";
    $f = fopen($file, "r");
    while ( $line = fgets($f, 1000) ) {
    	echo round(round(lbsToOz($line)) /16);
    }
?>