<?php
//-----------------------------------------------------------------
//------------------------- stop Camera ---------------------------
//-----------------------------------------------------------------
	error_reporting(E_ALL);
    ini_set("display_errors", 1);
    require 'login/login.php';
    connection_auto();
    connection_manual();
    
	if ($_SESSION['username'] != "invite") {
		$cmd = "python ../python/script.py 'CAMERA' 'stop'";
		$outputTest = exec($cmd, $output, $rst);
		echo json_encode($rst);
		sleep(0.1);
	}
	header("Location: ../../camera.php");
	exit();
?>
