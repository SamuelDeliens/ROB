<?php
//-----------------------------------------------------------------
//------------------------ launch Camera --------------------------
//-----------------------------------------------------------------
    error_reporting(E_ALL);
    ini_set("display_errors", 1);
    require 'login/login.php';
    connection_auto();
    connection_manual();
    
	if ($_SESSION['username'] != "invite") {
		$cmd = "python ../python/script.py 'CAMERA' 'launch'";
		exec($cmd, $output, $rst);
		sleep(0.5);
	}
	header("Location: ../../camera.php");
	exit();
?>
