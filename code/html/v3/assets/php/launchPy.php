<?php
//-----------------------------------------------------------------
//------------------------ Control Py -----------------------------
//-----------------------------------------------------------------

	$type = $_POST["type"];
	$action = $_POST["action"];
    $cmd = "python ../python/script.py '".$type."' '".$action."'";
	$outputTest = exec($cmd, $output, $rst);
	sleep(1);
	echo json_encode($outputTest);
?>