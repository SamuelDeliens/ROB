<?php
//-----------------------------------------------------------------
//------------------------ Control Py -----------------------------
//-----------------------------------------------------------------

	$type = $_POST["type"];
	$action = $_POST["action"];
	$step = $_POST["step"];
    $cmd = "python ../python/script.py '".$type."' '".$action."' '".$step."'";
	$outputTest = exec($cmd, $output, $rst);
	sleep(1);
	echo json_encode($outputTest);
?>
