<?php
//-----------------------------------------------------------------
//------------------------ REQUETE BDD ----------------------------
//-----------------------------------------------------------------
    error_reporting(E_ALL);
    ini_set("display_errors", 1);

    function connectBDD() {
        $db="Rov";
        $dbhost="localhost";
        $dbuser="root";
        $dbpasswd="pi";
        $pdo = new PDO('mysql:host='.$dbhost.';dbname='.$db.'', $dbuser, $dbpasswd);
        return $pdo;
    }

    function getUser($user, $password) {
        $pdo = connectBDD();
        $requete = $pdo->prepare("SELECT * FROM `users` WHERE username='".$user."' and password='".hash('sha256', $password)."'");
        $requete->execute();
        $reponse = $requete->fetchAll();
        $pdo = null;
        echo json_encode($reponse);
    }
?>