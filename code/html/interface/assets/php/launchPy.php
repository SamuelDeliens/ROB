<?php
    $cmd = "python ../python/script.py";
	$outputTest = exec($cmd, $output, $rst);
	sleep(1);
	echo json_encode($outputTest);
?>