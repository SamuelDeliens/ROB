<?php

//-----------------------------------------------------------------
//------------------------ REQUETE BDD ----------------------------
//-----------------------------------------------------------------

    $db="Rov";
    $dbhost="localhost";
    $dbuser="root";
    $dbpasswd="pi";
    $pdo = new PDO('mysql:host='.$dbhost.';dbname='.$db.'', $dbuser, $dbpasswd);
    $requete = $pdo->prepare("SELECT * FROM capteur");
    $requete->execute();
    $reponse = $requete->fetchAll();
    $pdo = null;
    echo json_encode($reponse);
?>
