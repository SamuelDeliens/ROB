<?php

//------------------------------------- SCRIPT -------------------------------------

error_reporting(E_ALL);
ini_set("display_errors", 1);
session_start();
init();


//-------------------------------------- INIT --------------------------------------

function init() {
    $_SESSION['flash']['success'] = 'disconnect';
}


//------------------------------------- COOKIE -------------------------------------

function createCookie($time) {
    setcookie(
        "Bluerov_Log",
        $_SESSION['username'],
        time() + $time,
    );
}


//------------------------------------- CONNECTION -------------------------------------

function connection_auto() {
    if (isset($_COOKIE["Bluerov_Log"])) {
        $_SESSION['username'] = $_COOKIE["Bluerov_Log"];
        $_SESSION['flash']['success'] = 'connect';
    } else {
        $_SESSION['username'] = "invite";
        createCookie(24*3600);
    }
}

function connection_manual() {
    if(!empty($_REQUEST) && !empty($_REQUEST['username']) && !empty($_REQUEST['password'])) {
        $username = stripslashes($_REQUEST['username']);
        $password = stripslashes($_REQUEST['password']);
    
        $user = ["username" => "Samsam", "password" => "pi"];

        if($username == $user["username"] && $password == $user["password"]) {
            $_SESSION['username'] = $username;
            $_SESSION['flash']['success'] = 'connect';
            $time = 24*3600;
            if(isset($_REQUEST["remember"])) {
                $time = 265*$time;
            }
            createCookie($time);
        } else {
            deconnection();
            $_SESSION['flash']['success'] = 'Error';
        }
    } else {
        $_SESSION['flash']['success'] = 'disconnect';
    }
}


//------------------------------------ DECONNECTION ------------------------------------

function deconnection() {
    $_SESSION['flash']['success'] = 'disconnect';
    $_SESSION['username'] = "invite";
    createCookie(24*3600);
    session_destroy();
}

//{0:i, 1:"13/12/07 18:19:11", 2:7.1, 3: 1.2, 4: 3.1, 5: null, id:i, date:"13/12/07 18:19:11", pH:7.1, oxygen: 1.2, conductivity: 3.1, turbidifty: null}
?>