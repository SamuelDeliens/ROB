<?php
ini_set('display_errors','1');
ini_set('display_startup_errors','1');
error_reporting(E_ALL);
// Database settings
$db="Rob";
$dbhost="localhost";
$dbuser="root";
$dbpasswd="pi";
$pdo = new PDO('mysql:host='.$dbhost.';dbname='.$db.'', $dbuser, $dbpasswd);
$requete = $pdo->prepare("SELECT * FROM capteur");
$requete->execute();
$reponse = $requete->fetchAll();
$pdo = null;
?>

<html>
    <head>
        <title>Test Interface BDD</title>
        <meta charset ="UTF-8">
        <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
        <link rel="stylesheet" type="text/css" href="style.css"/>
    </head>

    <body>
	<div id="topPage">
		<button id="love" class="graphButton"><3</button>
		<h1>Base De Donnée de JiJi et Samsam</h1>
	</div>
        <div id="BDD">
            <div id="tableau">
                <table id="capteur">
                    <tr>
                        <td> id </td>
                        <td id="midCollumn"> date </td>
                        <td> pH </td>
                        <td> oxygen </td>
                        <td> conductivity </td>
                    </tr>
                    <tbody id="capteurDonnee"></tbody>
                </table>
            </div>

            <div id="divGraph" style="height:0px;">
                <div id="divButton">
                    <select id="firstChartO" class="graphButton">
                        <option value="pH">pH</option>
                        <option value="oxygen">oxygen</option>
                        <option value="conductivity">conductivity</option>
                    </select>
                    <button class="graphButton" id="graphInputSize">^</button>
                    <select id="secondChartO" class="graphButton">
                        <option value="pH">pH</option>
                        <option value="oxygen">oxygen</option>
                        <option value="conductivity">conductivity</option>
                    </select>
                </div>
                <table id="tabGraphique">
                    <tr>
                        <td>
                            <div id="graphique" class="graphique">
                                <canvas id="firstChart"></canvas>
                            </div>
                        </td>
                        <td>
                            <div id="graphique" class="graphique">
                                <canvas id="secondChart"></canvas>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>
        </div>

        <div id="loveDiv">
            <div class="background"></div>
            <div class="crop1"></div>
            <img class="crop2" src="https://i.ytimg.com/vi/vtwGk0A03CQ/maxresdefault.jpg">
        </div>
    </body>
</html>

<script src="script.js"></script>
<script>
    document.capteurValues = <?php echo json_encode($reponse); ?>;
    init();
</script>
<script src="graph.js"></script>
<script>
    var httpRequest;
    getValue();
    function getValue() {
        console.log("recherche");
        httpRequest = new XMLHttpRequest();
        if (!httpRequest) {
            alert('erreur Requette');
        }
        httpRequest.responseType = "json";
        httpRequest.open('GET', 'requete.php');
        httpRequest.send();
        httpRequest.onload = function() {
            if(httpRequest.readyState == 4 && httpRequest.status == 200) {
                document.capteurValues = httpRequest.response;
                console.log(document.capteurValues);
            }
            
        }
        checkChange();
        setTimeout(function() {getValue()}, 50);
    }
</script>
