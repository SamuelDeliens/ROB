<?php
    error_reporting(E_ALL);
    ini_set("display_errors", 1);
    require 'assets/php/login/login.php';
    connection_auto();
    connection_manual();
?>

<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Table - Brand</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="assets/css/Nunito.css">
    <link rel="stylesheet" href="assets/fonts/fontawesome-all.min.css">
    <link rel="stylesheet" href="assets/fonts/font-awesome.min.css">
    <link rel="stylesheet" href="assets/fonts/fontawesome5-overrides.min.css">
    <link rel="stylesheet" href="assets/bootstrap/css/animate.min.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <script src="assets/js/role/roles.js"></script>
    <script src="assets/js/role/roles_display.js"></script>
    <script src="assets/js/requete.js"></script>
    <script src="assets/js/settings.js"></script>
    <script src="assets/js/controler.js"></script>
    <script src="assets/js/donnees.js"></script>
</head>

<body id="page-top">
    <div id="wrapper">
        <nav class="navbar navbar-dark align-items-start sidebar sidebar-dark accordion bg-gradient-primary p-0">
            <div class="container-fluid d-flex flex-column p-0"><a class="navbar-brand d-flex justify-content-center align-items-center sidebar-brand m-0" href="#">
                <div id="love" class="sidebar-brand-icon rotate-n-15"><i class="fas fa-heart jello animated" data-bss-hover-animate="jello"></i></div>
                    <div class="sidebar-brand-text mx-3"><span>mWL</span></div>
                </a>
                <hr class="sidebar-divider my-0">
                <ul class="navbar-nav text-light" id="accordionSidebar">
                    <li class="nav-item"><a class="nav-link active" href="index.php"><i class="fa fa-feed"></i><span>Real Time</span></a></li>
                    <li class="nav-item"><a class="nav-link" href="table.php"><i class="fas fa-table"></i><span>Donnee</span></a></li>
                    <li class="nav-item"><a class="nav-link" href="stat.php"><i class="fas fa-tachometer-alt"></i><span>Statistique</span></a></li>
                    <li class="nav-item"><a class="nav-link" href="camera.php"><i class="fas fa-camera-retro"></i><span>Camera</span></a></li>
                </ul>
                <div class="text-center d-none d-md-inline"><button class="btn rounded-circle border-0" data-bss-hover-animate="pulse" id="sidebarToggle" type="button"></button></div>
            </div>
        </nav>
        <div class="d-flex flex-column" id="content-wrapper"> 
                <div id="content">
                <nav class="navbar navbar-light navbar-expand bg-white shadow mb-4 topbar static-top">
                    <div class="container-fluid"><button class="btn btn-link d-md-none rounded-circle me-3" id="sidebarToggleTop" type="button"><i class="fas fa-bars"></i></button>
                        <form class="d-none d-sm-inline-block ms-md-3 my-2 my-md-0 mw-100 navbar-search" style="margin-right: 20px;">
                            <div class="input-group"><input class="bg-light form-control border-0 small" type="text" placeholder="Search for ..."><button class="btn btn-primary py-0" type="button"><i class="fas fa-search"></i></button></div>
                        </form>
                        <div>
                            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto;" width="50px" height="50px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                                <g>
                                  <animateTransform attributeName="transform" type="rotate" values="360 50 50;0 50 50" keyTimes="0;1" dur="1.7543859649122806s" repeatCount="indefinite" calcMode="spline" keySplines="0.5 0 0.5 1" begin="-0.17543859649122806s"></animateTransform>
                                  <circle cx="50" cy="50" r="39.891" stroke="#6994b7" stroke-width="14.4" fill="none" stroke-dasharray="0 300">
                                    <animate attributeName="stroke-dasharray" values="15 300;55.1413599195142 300;15 300" keyTimes="0;0.5;1" dur="1.7543859649122806s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.0807017543859649s"></animate>
                                  </circle>
                                  <circle cx="50" cy="50" r="39.891" stroke="#eeeeee" stroke-width="7.2" fill="none" stroke-dasharray="0 300">
                                    <animate attributeName="stroke-dasharray" values="15 300;55.1413599195142 300;15 300" keyTimes="0;0.5;1" dur="1.7543859649122806s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.0807017543859649s"></animate>
                                  </circle>
                                  <circle cx="50" cy="50" r="32.771" stroke="#000000" stroke-width="1" fill="none" stroke-dasharray="0 300">
                                    <animate attributeName="stroke-dasharray" values="15 300;45.299378454348094 300;15 300" keyTimes="0;0.5;1" dur="1.7543859649122806s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.0807017543859649s"></animate>
                                  </circle>
                                  <circle cx="50" cy="50" r="47.171" stroke="#000000" stroke-width="1" fill="none" stroke-dasharray="0 300">
                                    <animate attributeName="stroke-dasharray" values="15 300;66.03388996804073 300;15 300" keyTimes="0;0.5;1" dur="1.7543859649122806s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.0807017543859649s"></animate>
                                  </circle>
                                </g>
                                
                                <g>
                                  <animateTransform attributeName="transform" type="rotate" values="360 50 50;0 50 50" keyTimes="0;1" dur="1.7543859649122806s" repeatCount="indefinite" calcMode="spline" keySplines="0.5 0 0.5 1"></animateTransform>
                                  <path fill="#6994b7" stroke="#000000" d="M97.2,50.1c0,6.1-1.2,12.2-3.5,17.9l-13.3-5.4c1.6-3.9,2.4-8.2,2.4-12.4"></path>
                                  <path fill="#eeeeee" d="M93.5,49.9c0,1.2,0,2.7-0.1,3.9l-0.4,3.6c-0.4,2-2.3,3.3-4.1,2.8l-0.2-0.1c-1.8-0.5-3.1-2.3-2.7-3.9l0.4-3 c0.1-1,0.1-2.3,0.1-3.3"></path>
                                  <path fill="#6994b7" stroke="#000000" d="M85.4,62.7c-0.2,0.7-0.5,1.4-0.8,2.1c-0.3,0.7-0.6,1.4-0.9,2c-0.6,1.1-2,1.4-3.2,0.8c-1.1-0.7-1.7-2-1.2-2.9 c0.3-0.6,0.5-1.2,0.8-1.8c0.2-0.6,0.6-1.2,0.7-1.8"></path>
                                  <path fill="#6994b7" stroke="#000000" d="M94.5,65.8c-0.3,0.9-0.7,1.7-1,2.6c-0.4,0.9-0.7,1.7-1.1,2.5c-0.7,1.4-2.3,1.9-3.4,1.3h0 c-1.1-0.7-1.5-2.2-0.9-3.4c0.4-0.8,0.7-1.5,1-2.3c0.3-0.8,0.7-1.5,0.9-2.3"></path>
                                </g>
                                <g>
                                  <animateTransform attributeName="transform" type="rotate" values="360 50 50;0 50 50" keyTimes="0;1" dur="1.7543859649122806s" repeatCount="indefinite" calcMode="spline" keySplines="0.5 0 0.5 1" begin="-0.17543859649122806s"></animateTransform>
                                  <path fill="#eeeeee" stroke="#000000" d="M86.9,35.3l-6,2.4c-0.4-1.2-1.1-2.4-1.7-3.5c-0.2-0.5,0.3-1.1,0.9-1C82.3,33.8,84.8,34.4,86.9,35.3z"></path>
                                  <path fill="#eeeeee" stroke="#000000" d="M87.1,35.3l6-2.4c-0.6-1.7-1.5-3.3-2.3-4.9c-0.3-0.7-1.2-0.6-1.4,0.1C88.8,30.6,88.2,33,87.1,35.3z"></path>
                                  <path fill="#6994b7" stroke="#000000" d="M82.8,50.1c0-3.4-0.5-6.8-1.6-10c-0.2-0.8-0.4-1.5-0.3-2.3c0.1-0.8,0.4-1.6,0.7-2.4c0.7-1.5,1.9-3.1,3.7-4l0,0 c1.8-0.9,3.7-1.1,5.6-0.3c0.9,0.4,1.7,1,2.4,1.8c0.7,0.8,1.3,1.7,1.7,2.8c1.5,4.6,2.2,9.5,2.3,14.4"></path>
                                  <path fill="#eeeeee" d="M86.3,50.2l0-0.9l-0.1-0.9l-0.1-1.9c0-0.9,0.2-1.7,0.7-2.3c0.5-0.7,1.3-1.2,2.3-1.4l0.3,0 c0.9-0.2,1.9,0,2.6,0.6c0.7,0.5,1.3,1.4,1.4,2.4l0.2,2.2l0.1,1.1l0,1.1"></path>
                                  <path fill="#ff9922" d="M93.2,34.6c0.1,0.4-0.3,0.8-0.9,1c-0.6,0.2-1.2,0.1-1.4-0.2c-0.1-0.3,0.3-0.8,0.9-1 C92.4,34.2,93,34.3,93.2,34.6z"></path>
                                  <path fill="#ff9922" d="M81.9,38.7c0.1,0.3,0.7,0.3,1.3,0.1c0.6-0.2,1-0.6,0.9-0.9c-0.1-0.3-0.7-0.3-1.3-0.1 C82.2,38,81.8,38.4,81.9,38.7z"></path>
                                  <path fill="#000000" d="M88.5,36.8c0.1,0.3-0.2,0.7-0.6,0.8c-0.5,0.2-0.9,0-1.1-0.3c-0.1-0.3,0.2-0.7,0.6-0.8C87.9,36.3,88.4,36.4,88.5,36.8z"></path>
                                  <path stroke="#000000" d="M85.9,38.9c0.2,0.6,0.8,0.9,1.4,0.7c0.6-0.2,0.9-0.9,0.6-2.1c0.3,1.2,1,1.7,1.6,1.5c0.6-0.2,0.9-0.8,0.8-1.4"></path>
                                  <path fill="#6994b7" stroke="#000000" d="M86.8,42.3l0.4,2.2c0.1,0.4,0.1,0.7,0.2,1.1l0.1,1.1c0.1,1.2-0.9,2.3-2.2,2.3c-1.3,0-2.5-0.8-2.5-1.9l-0.1-1 c0-0.3-0.1-0.6-0.2-1l-0.3-1.9"></path>
                                  <path fill="#6994b7" stroke="#000000" d="M96.2,40.3l0.5,2.7c0.1,0.5,0.2,0.9,0.2,1.4l0.1,1.4c0.1,1.5-0.9,2.8-2.2,2.9h0c-1.3,0-2.5-1.1-2.6-2.4 L92.1,45c0-0.4-0.1-0.8-0.2-1.2l-0.4-2.5"></path>
                                  <path fill="#000000" d="M91.1,34.1c0.3,0.7,0,1.4-0.7,1.6c-0.6,0.2-1.3-0.1-1.6-0.7c-0.2-0.6,0-1.4,0.7-1.6C90.1,33.1,90.8,33.5,91.1,34.1z"></path>
                                  <path fill="#000000" d="M85.5,36.3c0.2,0.6-0.1,1.2-0.7,1.5c-0.6,0.2-1.3,0-1.5-0.6C83,36.7,83.4,36,84,35.8C84.6,35.5,85.3,35.7,85.5,36.3z"></path>
                                
                                </g>
                                </svg>
                            </div>
                        <ul class="navbar-nav flex-nowrap ms-auto">
                            <li class="nav-item dropdown show d-sm-none no-arrow"><a class="dropdown-toggle nav-link" aria-expanded="true" data-bs-toggle="dropdown" href="#"><i class="fas fa-search"></i></a>
                                <div class="dropdown-menu show dropdown-menu-end p-3 animated--grow-in" aria-labelledby="searchDropdown">
                                    <form class="me-auto navbar-search w-100">
                                        <div class="input-group"><input class="bg-light form-control border-0 small" type="text" placeholder="Search for ...">
                                            <div class="input-group-append"><button class="btn btn-primary py-0" type="button"><i class="fas fa-search"></i></button></div>
                                        </div>
                                    </form>
                                </div>
                            </li>
                            <div class="d-none d-sm-block topbar-divider"></div>
                            <li class="nav-item dropdown no-arrow">
                                <div class="nav-item dropdown no-arrow"><a class="dropdown-toggle nav-link" aria-expanded="false" data-bs-toggle="dropdown" href="#"><span class="d-none d-lg-inline me-2 text-gray-600 small">Jiji <3 Samsam</span><img class="border rounded-circle img-profile" data-bss-hover-animate="rubberBand" src="assets/img/ROV.png"></a>
                                    <div class="dropdown-menu shadow dropdown-menu-end animated--grow-in">
                                        <a class="dropdown-item account_param" href="#"><i class="fas fa-user fa-sm fa-fw me-2 text-gray-400"></i>&nbsp;Profile</a>
                                        <a class="dropdown-item account_param" href="#" data-bs-target="#Settings" data-bs-toggle="modal"><i class="fas fa-cogs fa-sm fa-fw me-2 text-gray-400"></i>&nbsp;Settings</a>
                                        <a class="dropdown-item account_param" href="#"><i class="fas fa-list fa-sm fa-fw me-2 text-gray-400"></i>&nbsp;Activity log</a>
                                        <div class="dropdown-divider account_param"></div>
                                        <a class="dropdown-item account_param" href="assets/php/login/logout.php"><i class="fas fa-sign-out-alt fa-sm fa-fw me-2 text-gray-400"></i>&nbsp;Logout</a>
                                        <a class="dropdown-item account_param" href="#" data-bs-target="#Login" data-bs-toggle="modal"><i class="fas fa-sign-in-alt fa-sm fa-fw me-2 text-gray-400"></i>&nbsp;Login</a>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </nav>
                <div class="container-fluid">
                    <h3 class="text-dark mb-4"><i class="fa fa-feed"></i> Capteur</h3>
                    <div class="card shadow" style="margin-bottom: 30px;">
                        <div class="card-header py-3">
                            <div class="row">
                                <div class="col align-self-center">
                                    <p class="text-primary m-0 fw-bold">Données Temps Réel</p>
                                </div>
                                <div class="col-2 text-end align-self-center"><button class="btn btn-primary" type="button" id="GETDATA">GETDATA</button></div>
                                <div class="col-2 text-start align-self-center">
                                    <div class="row">
                                        <div class="col">
                                            <button class="btn btn-primary" type="button" id="GETRT">GETRT</button>
                                        </div>
                                        <div class="col">
                                            <svg style="display: none" width="50px" height="40px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                                                <circle cx="18" cy="50" r="4" fill="#0275d8">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="0s" repeatCount="indefinite"></animate>
                                                </circle><circle cx="27" cy="61.31370849898476" r="4" fill="#d002d8">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="-0.125s" repeatCount="indefinite"></animate>
                                                </circle><circle cx="36" cy="66" r="4" fill="#d86502">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="-0.25s" repeatCount="indefinite"></animate>
                                                </circle><circle cx="45" cy="61.31370849898476" r="4" fill="#0ad802">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="-0.375s" repeatCount="indefinite"></animate>
                                                </circle><circle cx="54" cy="50" r="4" fill="#0275d8">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="-0.5s" repeatCount="indefinite"></animate>
                                                </circle><circle cx="63" cy="38.68629150101524" r="4" fill="#d002d8">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="-0.625s" repeatCount="indefinite"></animate>
                                                </circle><circle cx="72" cy="34" r="4" fill="#d86502">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="-0.75s" repeatCount="indefinite"></animate>
                                                </circle><circle cx="81" cy="38.68629150101523" r="4" fill="#0ad802">
                                                  <animate attributeName="cy" values="34;66;34" times="0;0.5;1" dur="1s" calcMode="spline" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" begin="-0.875s" repeatCount="indefinite"></animate>
                                                </circle>
                                                </svg>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="card-body" style="padding-left: 30px;padding-right: 30px;">
                            <div class="row" id="dataTable" style="background: var(--bs-gray-900);border-radius: 35px;" data-bss-hover-animate="pulse">
                                <div class="col-3" style="padding: 12px;border-right: 1px solid var(--bs-white) ;border-left: 1px none var(--bs-white) ;">
                                    <h4 class="text-center tabRT" style="font-weight: bold;color: var(--bs-yellow);">Get your first</h4>
                                    <h6 class="text-center">date</h6>
                                </div>
                                <div class="col-3" style="padding: 12px;border-right: 1px solid var(--bs-white) ;border-left: 1px solid var(--bs-white) ;">
                                    <h4 class="text-center tabRT" style="font-weight: bold;color: var(--bs-yellow);">data by clicking</h4>
                                    <h6 class="text-center">pH</h6>
                                </div>
                                <div class="col-3" style="padding: 12px;border-right: 1px solid var(--bs-white) ;border-left: 1px solid var(--bs-white) ;">
                                    <h4 class="text-center tabRT" style="font-weight: bold;color: var(--bs-yellow);">on one of</h4>
                                    <h6 class="text-center">oxygen</h6>
                                </div>
                                <div class="col-3" style="padding: 12px;border-right: 1px none var(--bs-white) ;border-left: 1px solid var(--bs-white) ;">
                                    <h4 class="text-center tabRT" style="font-weight: bold;color: var(--bs-yellow);">the two buttons</h4>
                                    <h6 class="text-center">conductivity</h6>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card shadow">
                        <div class="card-header py-3">
                            <div class="row">
                                <div class="col align-self-center">
                                    <p class="text-primary m-0 fw-bold">Données</p>
                                </div>
                                <div class="col-2 text-start align-self-center"><button class="btn btn-primary" type="button" id="Refresh">Refresh</button></div>
                            </div>
                        </div>
                        <div class="card-body">
                            <div class="table-responsive table mt-2" id="dataTable-1" role="grid" aria-describedby="dataTable_info">
                                <table class="table my-0" id="dataTable">
                                    <thead>
                                        <tr>
                                            <th></th>
                                            <th>ID</th>
                                            <th style="text-align: left;">date</th>
                                            <th style="width: 16%;text-align: center;">pH</th>
                                            <th style="width: 16%;text-align: center;">oxygen</th>
                                            <th style="width: 16%;text-align: center;">conductivity</th>
                                            <th style="width: 16%;text-align: center;">turbi</th>
                                        </tr>
                                    </thead>
                                    <tbody id="capteurDonnee">
                                        <td><strong>Get your first data by clicking on one of the two buttons ! </strong><small>( GETDATA / GETRT )</small></td>
                                    </tbody>
                                    <tfoot>
                                        <tr>
                                            <th></th>
                                            <th>ID</th>
                                            <th style="text-align: left;">date</th>
                                            <th style="width: 16%;text-align: center;">pH</th>
                                            <th style="width: 16%;text-align: center;">oxygen</th>
                                            <th style="width: 16%;text-align: center;">conductivity</th>
                                            <th style="width: 16%;text-align: center;">turbi</th>
                                        </tr>
                                    </tfoot>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
                </div>
            </div>
    </div>
    <div class="modal fade" role="dialog" tabindex="-1" id="Login">
        <div class="modal-dialog modal-xl" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title text-primary">
                        <svg style="margin: auto;" width="50px" height="50px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                            <g transform="translate(50 50)"><g transform="scale(0.23055509576307065)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(0 0 0)" stroke="none" fill="#d002d8"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.23055509576307065;0.30495658227799793;0.7844553129649303;0.6330122535401268;0.23055509576307065" keyTimes="0;0.25;0.5;0.75;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.7563281940591027)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(30 0 0)" stroke="none" fill="#d80275"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.7563281940591027;0.4321476348518495;0.3054792696097095;0.8800714637121553;0.33107991131092196;0.770662563492935;0.7563281940591027" keyTimes="0;0.16666666666666666;0.3333333333333333;0.5;0.6666666666666666;0.8333333333333334;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.792185567152214)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(60 0 0)" stroke="none" fill="#0ad802"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.792185567152214;0.16495778784531223;0.792185567152214" keyTimes="0;0.5;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.6244633880416197)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(90 0 0)" stroke="none" fill="#d86502"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.6244633880416197;0.825268015716231;0.6040428719138717;0.9222078457517047;0.1906597428997563;0.6607476891077467;0.6244633880416197" keyTimes="0;0.16666666666666666;0.3333333333333333;0.5;0.6666666666666666;0.8333333333333334;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.8554014785599822)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(120 0 0)" stroke="none" fill="#d002d8"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.8554014785599822;0.8175732998315592;0.15250676206701652;0.8554014785599822" keyTimes="0;0.3333333333333333;0.6666666666666666;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.2641268660464312)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(150 0 0)" stroke="none" fill="#d80275"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.2641268660464312;0.0453891097835496;0.2641268660464312" keyTimes="0;0.5;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.0822393826619301)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(180 0 0)" stroke="none" fill="#0ad802"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.0822393826619301;0.5076994396266454;0.5163530281760724;0.338134211088839;0.0822393826619301" keyTimes="0;0.25;0.5;0.75;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.6243416189995064)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(210 0 0)" stroke="none" fill="#d86502"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.6243416189995064;0.5438130745863236;0.7498547820083945;0.49611517327250454;0.6243416189995064" keyTimes="0;0.25;0.5;0.75;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.13350743781080965)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(240 0 0)" stroke="none" fill="#d002d8"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.13350743781080965;0.7138965733543937;0.8769271711978104;0.06694550648496034;0.34481581334966316;0.5835242510648233;0.13350743781080965" keyTimes="0;0.16666666666666666;0.3333333333333333;0.5;0.6666666666666666;0.8333333333333334;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.6461691376154014)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(270 0 0)" stroke="none" fill="#d80275"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.6461691376154014;0.025529055457246264;0.7857692802800377;0.03073983087118426;0.6461691376154014" keyTimes="0;0.25;0.5;0.75;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.27601299043232097)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(300 0 0)" stroke="none" fill="#0ad802"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.27601299043232097;0.7654334068222957;0.7722025145401563;0.3288975790468356;0.9097445640336147;0.27601299043232097" keyTimes="0;0.2;0.4;0.6;0.8;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g><g transform="scale(0.7562814965621921)">
                            <path d="M0 0L0 -40A40 40 0 0 1 19.999999999999996 -34.64101615137755" transform="rotate(330 0 0)" stroke="none" fill="#d86502"></path>
                            <animateTransform attributeName="transform" type="scale" values="0.7562814965621921;0.11479883701677895;0.4963544387344554;0.9312789363834434;0.24014885420700227;0.7562814965621921" keyTimes="0;0.2;0.4;0.6;0.8;1" dur="0.98s" repeatCount="indefinite"></animateTransform>
                            </g></g>
                            </svg>
                    &nbsp;Login</h4><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" style="padding: 25px;">
                    <div style="border-bottom-color: var(--bs-orange);box-shadow: 3px 10px 17px 6px var(--bs-gray-200);border-radius: 10px;padding: 15px 15px;">
                        <div class="row">
                            <div class="col-lg-6 d-none d-lg-flex">
                                <div class="flex-grow-1 bg-login-image" style="background-image: url(&quot;assets/img/dogs/image3.jpeg&quot;);"></div>
                            </div>
                            <div class="col-lg-6">
                                <div class="p-5">
                                    <div class="text-center">
                                        <h4 class="text-dark mb-4">Welcome Back!</h4>
                                    </div>
                                    <form class="user">
                                        <div class="mb-3"><input class="form-control form-control-user" id="exampleInputEmail" aria-describedby="emailHelp" placeholder="Enter Username" name="username"></div>
                                        <div class="mb-3"><input class="form-control form-control-user" type="password" id="exampleInputPassword" placeholder="Password" name="password"></div>
                                        <div class="mb-3">
                                            <div class="custom-control custom-checkbox small">
                                                <div class="form-check"><input class="form-check-input custom-control-input" type="checkbox" id="formCheck-1" name="remember"><label class="form-check-label custom-control-label" for="formCheck-1">Remember Me</label></div>
                                            </div>
                                        </div><button class="btn btn-primary d-block btn-user w-100" type="submit">Login</button>
                                        <hr>
                                    </form>
                                </div>
                            </div>
                        </div>                    </div>
                </div>
                <div class="modal-footer"><button class="btn btn-light btn-sm" type="button" data-bs-dismiss="modal">Close</button></div>
            </div>
        </div>
    </div>
    <div class="modal fade" role="dialog" tabindex="-1" id="Settings">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title text-primary">
                        <svg style="margin: auto;" width="40px" height="40px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                        <g transform="translate(50 50)"> <g transform="translate(-17 -17) scale(0.5)"> <g>
                        <animateTransform attributeName="transform" type="rotate" values="0;45" keyTimes="0;1" dur="0.2s" begin="0s" repeatCount="indefinite"></animateTransform><path d="M37.3496987939662 -7 L47.3496987939662 -7 L47.3496987939662 7 L37.3496987939662 7 A38 38 0 0 1 31.359972760794346 21.46047782418268 L31.359972760794346 21.46047782418268 L38.431040572659825 28.531545636048154 L28.531545636048154 38.431040572659825 L21.46047782418268 31.359972760794346 A38 38 0 0 1 7.0000000000000036 37.3496987939662 L7.0000000000000036 37.3496987939662 L7.000000000000004 47.3496987939662 L-6.999999999999999 47.3496987939662 L-7 37.3496987939662 A38 38 0 0 1 -21.46047782418268 31.35997276079435 L-21.46047782418268 31.35997276079435 L-28.531545636048154 38.431040572659825 L-38.43104057265982 28.531545636048158 L-31.359972760794346 21.460477824182682 A38 38 0 0 1 -37.3496987939662 7.000000000000007 L-37.3496987939662 7.000000000000007 L-47.3496987939662 7.000000000000008 L-47.3496987939662 -6.9999999999999964 L-37.3496987939662 -6.999999999999997 A38 38 0 0 1 -31.35997276079435 -21.460477824182675 L-31.35997276079435 -21.460477824182675 L-38.431040572659825 -28.531545636048147 L-28.53154563604818 -38.43104057265981 L-21.4604778241827 -31.35997276079434 A38 38 0 0 1 -6.999999999999992 -37.3496987939662 L-6.999999999999992 -37.3496987939662 L-6.999999999999994 -47.3496987939662 L6.999999999999977 -47.3496987939662 L6.999999999999979 -37.3496987939662 A38 38 0 0 1 21.460477824182686 -31.359972760794342 L21.460477824182686 -31.359972760794342 L28.531545636048158 -38.43104057265982 L38.4310405726598 -28.53154563604818 L31.35997276079433 -21.4604778241827 A38 38 0 0 1 37.3496987939662 -6.999999999999995 M0 -23A23 23 0 1 0 0 23 A23 23 0 1 0 0 -23" fill="#0275d8"></path></g></g> <g transform="translate(0 22) scale(0.4)"> <g>
                        <animateTransform attributeName="transform" type="rotate" values="45;0" keyTimes="0;1" dur="0.2s" begin="-0.1s" repeatCount="indefinite"></animateTransform><path d="M37.3496987939662 -7 L47.3496987939662 -7 L47.3496987939662 7 L37.3496987939662 7 A38 38 0 0 1 31.359972760794346 21.46047782418268 L31.359972760794346 21.46047782418268 L38.431040572659825 28.531545636048154 L28.531545636048154 38.431040572659825 L21.46047782418268 31.359972760794346 A38 38 0 0 1 7.0000000000000036 37.3496987939662 L7.0000000000000036 37.3496987939662 L7.000000000000004 47.3496987939662 L-6.999999999999999 47.3496987939662 L-7 37.3496987939662 A38 38 0 0 1 -21.46047782418268 31.35997276079435 L-21.46047782418268 31.35997276079435 L-28.531545636048154 38.431040572659825 L-38.43104057265982 28.531545636048158 L-31.359972760794346 21.460477824182682 A38 38 0 0 1 -37.3496987939662 7.000000000000007 L-37.3496987939662 7.000000000000007 L-47.3496987939662 7.000000000000008 L-47.3496987939662 -6.9999999999999964 L-37.3496987939662 -6.999999999999997 A38 38 0 0 1 -31.35997276079435 -21.460477824182675 L-31.35997276079435 -21.460477824182675 L-38.431040572659825 -28.531545636048147 L-28.53154563604818 -38.43104057265981 L-21.4604778241827 -31.35997276079434 A38 38 0 0 1 -6.999999999999992 -37.3496987939662 L-6.999999999999992 -37.3496987939662 L-6.999999999999994 -47.3496987939662 L6.999999999999977 -47.3496987939662 L6.999999999999979 -37.3496987939662 A38 38 0 0 1 21.460477824182686 -31.359972760794342 L21.460477824182686 -31.359972760794342 L28.531545636048158 -38.43104057265982 L38.4310405726598 -28.53154563604818 L31.35997276079433 -21.4604778241827 A38 38 0 0 1 37.3496987939662 -6.999999999999995 M0 -23A23 23 0 1 0 0 23 A23 23 0 1 0 0 -23" fill="#d002d8"></path></g></g> <g transform="translate(28 4) scale(0.3)"> <g>
                        <animateTransform attributeName="transform" type="rotate" values="0;45" keyTimes="0;1" dur="0.2s" begin="-0.1s" repeatCount="indefinite"></animateTransform><path d="M37.3496987939662 -7 L47.3496987939662 -7 L47.3496987939662 7 L37.3496987939662 7 A38 38 0 0 1 31.359972760794346 21.46047782418268 L31.359972760794346 21.46047782418268 L38.431040572659825 28.531545636048154 L28.531545636048154 38.431040572659825 L21.46047782418268 31.359972760794346 A38 38 0 0 1 7.0000000000000036 37.3496987939662 L7.0000000000000036 37.3496987939662 L7.000000000000004 47.3496987939662 L-6.999999999999999 47.3496987939662 L-7 37.3496987939662 A38 38 0 0 1 -21.46047782418268 31.35997276079435 L-21.46047782418268 31.35997276079435 L-28.531545636048154 38.431040572659825 L-38.43104057265982 28.531545636048158 L-31.359972760794346 21.460477824182682 A38 38 0 0 1 -37.3496987939662 7.000000000000007 L-37.3496987939662 7.000000000000007 L-47.3496987939662 7.000000000000008 L-47.3496987939662 -6.9999999999999964 L-37.3496987939662 -6.999999999999997 A38 38 0 0 1 -31.35997276079435 -21.460477824182675 L-31.35997276079435 -21.460477824182675 L-38.431040572659825 -28.531545636048147 L-28.53154563604818 -38.43104057265981 L-21.4604778241827 -31.35997276079434 A38 38 0 0 1 -6.999999999999992 -37.3496987939662 L-6.999999999999992 -37.3496987939662 L-6.999999999999994 -47.3496987939662 L6.999999999999977 -47.3496987939662 L6.999999999999979 -37.3496987939662 A38 38 0 0 1 21.460477824182686 -31.359972760794342 L21.460477824182686 -31.359972760794342 L28.531545636048158 -38.43104057265982 L38.4310405726598 -28.53154563604818 L31.35997276079433 -21.4604778241827 A38 38 0 0 1 37.3496987939662 -6.999999999999995 M0 -23A23 23 0 1 0 0 23 A23 23 0 1 0 0 -23" fill="#d86502"></path></g></g></g>
                        </svg>&nbsp;Settings</h4><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" style="padding: 25px;">
                    <div style="border-bottom-color: var(--bs-orange);box-shadow: 3px 10px 17px 6px var(--bs-gray-200);border-radius: 10px;padding: 15px 15px;">
                        <h5 style="color: var(--bs-orange);border-radius: 5px;border-bottom-width: 2px;border-bottom-style: none;padding: 5px;box-shadow: 1px 1px 1px 1px var(--bs-gray-200);margin-bottom: 30px;">Sensor :</h5>
                        <div class="row" style="padding: 5px 5px;">
                            <div class="col">
                                <h6>Sensor Name:&nbsp;</h6>
                            </div>
                            <div class="col"><input type="text" style="width: 90%;border: 1px solid var(--bs-gray-200);border-radius: 5px;padding: 2px 5px;" placeholder="pH"></div>
                            <div class="col"><input type="text" style="width: 90%;border: 1px solid var(--bs-gray-200);border-radius: 5px;padding: 2px 5px;" placeholder="Oxygen"></div>
                            <div class="col"><input type="text" style="width: 90%;border: 1px solid var(--bs-gray-200);border-radius: 5px;padding: 2px 5px;" placeholder="Conductivity"></div>
                        </div>
                        <hr style="text-align: center;margin: 10px 20%;">
                        <div class="row" style="padding: 5px 5px;">
                            <div class="col">
                                <h6>Calibration:</h6>
                            </div>
                            <div class="col"><a class="btn btn-light btn-sm calibrationType" role="button" data-bs-target="#Calibration" data-bs-toggle="modal" data-backdrop="static" data-keyboard="false" value=0>Calibrate</a></div>
                            <div class="col"><a class="btn btn-light btn-sm calibrationType" role="button" data-bs-target="#Settings" data-bs-toggle="modal" data-backdrop="static" data-keyboard="false" value=1>Calibrate</a></div>
                            <div class="col"><a class="btn btn-light btn-sm calibrationType" role="button" data-bs-target="#Settings" data-bs-toggle="modal" data-backdrop="static" data-keyboard="false" value=2>Calibrate</a></div>
                        </div>
                        <hr style="text-align: center;margin: 10px 20%;">
                    </div>
                </div>
                <div class="modal-footer"><button class="btn btn-light btn-sm" type="button" data-bs-dismiss="modal">Close</button><button class="btn btn-primary btn-sm" type="button">Save</button></div>
            </div>
        </div>
    </div>
    <div class="modal fade" role="dialog" tabindex="-1" id="Calibration" data-keyboard="false" data-backdrop="static">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title">
                        <svg style="margin: auto;" width="50px" height="50px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                        <g>
                          <animateTransform attributeName="transform" type="rotate" values="360 50 50;0 50 50" keyTimes="0;1" dur="2.272727272727273s" repeatCount="indefinite" calcMode="spline" keySplines="0.5 0 0.5 1" begin="-0.2272727272727273s"></animateTransform>
                          <circle cx="50" cy="50" r="39.891" stroke="#0275d8" stroke-width="14.4" fill="none" stroke-dasharray="0 300">
                            <animate attributeName="stroke-dasharray" values="15 300;55.1413599195142 300;15 300" keyTimes="0;0.5;1" dur="2.272727272727273s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.10454545454545454s"></animate>
                          </circle>
                          <circle cx="50" cy="50" r="39.891" stroke="#eeeeee" stroke-width="7.2" fill="none" stroke-dasharray="0 300">
                            <animate attributeName="stroke-dasharray" values="15 300;55.1413599195142 300;15 300" keyTimes="0;0.5;1" dur="2.272727272727273s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.10454545454545454s"></animate>
                          </circle>
                          <circle cx="50" cy="50" r="32.771" stroke="#000000" stroke-width="1" fill="none" stroke-dasharray="0 300">
                            <animate attributeName="stroke-dasharray" values="15 300;45.299378454348094 300;15 300" keyTimes="0;0.5;1" dur="2.272727272727273s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.10454545454545454s"></animate>
                          </circle>
                          <circle cx="50" cy="50" r="47.171" stroke="#000000" stroke-width="1" fill="none" stroke-dasharray="0 300">
                            <animate attributeName="stroke-dasharray" values="15 300;66.03388996804073 300;15 300" keyTimes="0;0.5;1" dur="2.272727272727273s" repeatCount="indefinite" calcMode="linear" keySplines="0 0.4 0.6 1;0.4 0 1 0.6" begin="-0.10454545454545454s"></animate>
                          </circle>
                        </g>
                        
                        <g>
                          <animateTransform attributeName="transform" type="rotate" values="360 50 50;0 50 50" keyTimes="0;1" dur="2.272727272727273s" repeatCount="indefinite" calcMode="spline" keySplines="0.5 0 0.5 1"></animateTransform>
                          <path fill="#0275d8" stroke="#000000" d="M97.2,50.1c0,6.1-1.2,12.2-3.5,17.9l-13.3-5.4c1.6-3.9,2.4-8.2,2.4-12.4"></path>
                          <path fill="#eeeeee" d="M93.5,49.9c0,1.2,0,2.7-0.1,3.9l-0.4,3.6c-0.4,2-2.3,3.3-4.1,2.8l-0.2-0.1c-1.8-0.5-3.1-2.3-2.7-3.9l0.4-3 c0.1-1,0.1-2.3,0.1-3.3"></path>
                          <path fill="#0275d8" stroke="#000000" d="M85.4,62.7c-0.2,0.7-0.5,1.4-0.8,2.1c-0.3,0.7-0.6,1.4-0.9,2c-0.6,1.1-2,1.4-3.2,0.8c-1.1-0.7-1.7-2-1.2-2.9 c0.3-0.6,0.5-1.2,0.8-1.8c0.2-0.6,0.6-1.2,0.7-1.8"></path>
                          <path fill="#0275d8" stroke="#000000" d="M94.5,65.8c-0.3,0.9-0.7,1.7-1,2.6c-0.4,0.9-0.7,1.7-1.1,2.5c-0.7,1.4-2.3,1.9-3.4,1.3h0 c-1.1-0.7-1.5-2.2-0.9-3.4c0.4-0.8,0.7-1.5,1-2.3c0.3-0.8,0.7-1.5,0.9-2.3"></path>
                        </g>
                        <g>
                          <animateTransform attributeName="transform" type="rotate" values="360 50 50;0 50 50" keyTimes="0;1" dur="2.272727272727273s" repeatCount="indefinite" calcMode="spline" keySplines="0.5 0 0.5 1" begin="-0.2272727272727273s"></animateTransform>
                          <path fill="#eeeeee" stroke="#000000" d="M86.9,35.3l-6,2.4c-0.4-1.2-1.1-2.4-1.7-3.5c-0.2-0.5,0.3-1.1,0.9-1C82.3,33.8,84.8,34.4,86.9,35.3z"></path>
                          <path fill="#eeeeee" stroke="#000000" d="M87.1,35.3l6-2.4c-0.6-1.7-1.5-3.3-2.3-4.9c-0.3-0.7-1.2-0.6-1.4,0.1C88.8,30.6,88.2,33,87.1,35.3z"></path>
                          <path fill="#0275d8" stroke="#000000" d="M82.8,50.1c0-3.4-0.5-6.8-1.6-10c-0.2-0.8-0.4-1.5-0.3-2.3c0.1-0.8,0.4-1.6,0.7-2.4c0.7-1.5,1.9-3.1,3.7-4l0,0 c1.8-0.9,3.7-1.1,5.6-0.3c0.9,0.4,1.7,1,2.4,1.8c0.7,0.8,1.3,1.7,1.7,2.8c1.5,4.6,2.2,9.5,2.3,14.4"></path>
                          <path fill="#eeeeee" d="M86.3,50.2l0-0.9l-0.1-0.9l-0.1-1.9c0-0.9,0.2-1.7,0.7-2.3c0.5-0.7,1.3-1.2,2.3-1.4l0.3,0 c0.9-0.2,1.9,0,2.6,0.6c0.7,0.5,1.3,1.4,1.4,2.4l0.2,2.2l0.1,1.1l0,1.1"></path>
                          <path fill="#d86502" d="M93.2,34.6c0.1,0.4-0.3,0.8-0.9,1c-0.6,0.2-1.2,0.1-1.4-0.2c-0.1-0.3,0.3-0.8,0.9-1 C92.4,34.2,93,34.3,93.2,34.6z"></path>
                          <path fill="#d86502" d="M81.9,38.7c0.1,0.3,0.7,0.3,1.3,0.1c0.6-0.2,1-0.6,0.9-0.9c-0.1-0.3-0.7-0.3-1.3-0.1 C82.2,38,81.8,38.4,81.9,38.7z"></path>
                          <path fill="#000000" d="M88.5,36.8c0.1,0.3-0.2,0.7-0.6,0.8c-0.5,0.2-0.9,0-1.1-0.3c-0.1-0.3,0.2-0.7,0.6-0.8C87.9,36.3,88.4,36.4,88.5,36.8z"></path>
                          <path stroke="#000000" d="M85.9,38.9c0.2,0.6,0.8,0.9,1.4,0.7c0.6-0.2,0.9-0.9,0.6-2.1c0.3,1.2,1,1.7,1.6,1.5c0.6-0.2,0.9-0.8,0.8-1.4"></path>
                          <path fill="#0275d8" stroke="#000000" d="M86.8,42.3l0.4,2.2c0.1,0.4,0.1,0.7,0.2,1.1l0.1,1.1c0.1,1.2-0.9,2.3-2.2,2.3c-1.3,0-2.5-0.8-2.5-1.9l-0.1-1 c0-0.3-0.1-0.6-0.2-1l-0.3-1.9"></path>
                          <path fill="#0275d8" stroke="#000000" d="M96.2,40.3l0.5,2.7c0.1,0.5,0.2,0.9,0.2,1.4l0.1,1.4c0.1,1.5-0.9,2.8-2.2,2.9h0c-1.3,0-2.5-1.1-2.6-2.4 L92.1,45c0-0.4-0.1-0.8-0.2-1.2l-0.4-2.5"></path>
                          <path fill="#000000" d="M91.1,34.1c0.3,0.7,0,1.4-0.7,1.6c-0.6,0.2-1.3-0.1-1.6-0.7c-0.2-0.6,0-1.4,0.7-1.6C90.1,33.1,90.8,33.5,91.1,34.1z"></path>
                          <path fill="#000000" d="M85.5,36.3c0.2,0.6-0.1,1.2-0.7,1.5c-0.6,0.2-1.3,0-1.5-0.6C83,36.7,83.4,36,84,35.8C84.6,35.5,85.3,35.7,85.5,36.3z"></path>
                        
                        </g>
                        </svg>&nbsp;Calibration</h4><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body" style="padding: 25px;">
                    <div style="border-bottom-color: var(--bs-orange);box-shadow: 3px 10px 17px 6px var(--bs-gray-200);border-radius: 10px;padding: 15px 15px;">
                        <h6 id="indicCalibButton" style="color: var(--bs-orange);border-radius: 5px;border-bottom-width: 2px;border-bottom-style: none;padding: 5px;box-shadow: 1px 1px 1px 1px var(--bs-gray-200);margin-bottom: 30px;">Please put the sensor in the 7.0 pH solution</h6>
                        <div id="iconCalibrate" class="text-center" style="display:none">                        
                            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto; shape-rendering: auto;" width="50px" height="50px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                            <g transform="translate(20 50)">
                            <circle cx="0" cy="0" r="6" fill="#0275d8">
                              <animateTransform attributeName="transform" type="scale" begin="-0.3712871287128713s" calcMode="spline" keySplines="0.3 0 0.7 1;0.3 0 0.7 1" values="0;1;0" keyTimes="0;0.5;1" dur="0.9900990099009901s" repeatCount="indefinite"></animateTransform>
                            </circle>
                            </g><g transform="translate(40 50)">
                            <circle cx="0" cy="0" r="6" fill="#d002d8">
                              <animateTransform attributeName="transform" type="scale" begin="-0.24752475247524752s" calcMode="spline" keySplines="0.3 0 0.7 1;0.3 0 0.7 1" values="0;1;0" keyTimes="0;0.5;1" dur="0.9900990099009901s" repeatCount="indefinite"></animateTransform>
                            </circle>
                            </g><g transform="translate(60 50)">
                            <circle cx="0" cy="0" r="6" fill="#d86502">
                              <animateTransform attributeName="transform" type="scale" begin="-0.12376237623762376s" calcMode="spline" keySplines="0.3 0 0.7 1;0.3 0 0.7 1" values="0;1;0" keyTimes="0;0.5;1" dur="0.9900990099009901s" repeatCount="indefinite"></animateTransform>
                            </circle>
                            </g><g transform="translate(80 50)">
                            <circle cx="0" cy="0" r="6" fill="#0ad802">
                              <animateTransform attributeName="transform" type="scale" begin="0s" calcMode="spline" keySplines="0.3 0 0.7 1;0.3 0 0.7 1" values="0;1;0" keyTimes="0;0.5;1" dur="0.9900990099009901s" repeatCount="indefinite"></animateTransform>
                            </circle>
                            </g>
                            <!-- [ldio] generated by https://loading.io/ --></svg>
                        </div>
                        <div class="text-center"><a id="calibrateButton" class="btn btn-light btn-sm" role="button">Calibrate</a></div>
                    </div>
                </div>
                <div class="modal-footer"><button id="endCalibration" class="btn btn-light btn-sm" type="button" data-bs-dismiss="modal">Close</button></div>
            </div>
        </div>
    </div>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/bs-init.js"></script>
    <script src="assets/js/theme.js"></script>
    <script src="assets/js/index/script.js"></script>
</body>

</html>
