<?php
//-----------------------------------------------------------------
//------------------------ REQUETE BDD ----------------------------
//-----------------------------------------------------------------

    error_reporting(E_ALL);
    ini_set("display_errors", 1);   
    $db="Rov";
    $dbhost="localhost";
    $dbuser="root";
    $dbpasswd="pi";
    $pdo = new PDO('mysql:host='.$dbhost.';dbname='.$db.'', $dbuser, $dbpasswd);
    $requete = $pdo->prepare("SELECT * FROM capteur ORDER BY id DESC LIMIT 0,1");
    $requete->execute();
    $reponse = $requete->fetchAll();
    $pdo = null;
    echo json_encode($reponse);
?>
