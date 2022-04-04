<html>

<head>
        <title>Test Interface BDD</title>
        <meta charset ="UTF-8">
        <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
        <link rel="stylesheet" type="text/css" href="style.css"/>
        <script src="script.js"></script>
</head>

<body>
        <button id="love" class="graphButton"><3</button>
        <div id="BDD">
        <h1>Base De Donnée de JiJi et Samsam</h1>
        <div id="tableau">
        <table id="capteur">
                <tr>
                        <td> id </td>
                        <td id="midCollumn"> date </td>
                        <td> pH </td>
                </tr>

<?php
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

foreach ($reponse as $ligne) {
?>

                <tr>
                                <td> <?php echo $ligne['id']; ?> </td>
                                <td id="midCollumn"> <?php echo $ligne['date']; ?> </td>
                                <td> <?php echo $ligne['pH']; ?> </td>
                </tr>

<?php
}
?>

        </table>
        </div>

<div id="divGraph">
        <button class="graphButton" id="graphInputSize">v</button>
        <table id="tabGraphique">
                <tr><td>
                        <div id="graphique">
                                <canvas id="firstChart"></canvas>
                        </div></td><td>
                        <div id="graphique">
                                <canvas id="secondChart"></canvas>
                        </div>
                </td></tr>
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

<script>
        var capteurValues = <?php echo json_encode($reponse); ?>;
        nbPoint = capteurValues.length;

        const date = [];
    const pH = [];
        const pHlabel = [0,1,2,3,4,5,6,7,8,9,10,11,12];
        const nbpH = [0,0,0,0,0,0,0,0,0,0,0,0];
        for(mesure of capteurValues) {
        date.push(mesure.date);
        pH.push(mesure.pH);
                nbpH[Math.round(mesure.pH)]++;
    }

        // ---------------------------------------- //
        const data = {
        labels:date,
        datasets: [{
            label: 'pH function of time',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: pH,
        }]
    };
    const config = {
        type: 'line',
        data: data,
        options: {}
    };

        const myChart1 = new Chart(
        document.getElementById("firstChart"),
        config
    );
        // ---------------------------------------- //
        const data2 = {
        labels:pHlabel,
        datasets: [{
            label: 'nb of pH',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: nbpH,
                        tension: 0.1,
        }]
    };
    const config2 = {
        type: 'bar',
        data: data2,
        options: {
                        scales: {
                                y: {
                                        beginAtZero: true
                                }
                        }
                },
    };

        const myChart2 = new Chart(
        document.getElementById("secondChart"),
        config2
    );

var buttonSize = document.getElementById("graphInputSize");
buttonSize.addEventListener("click", function() {
  var graphPanel = document.getElementById("divGraph");
  var tableau = document.getElementById("tableau");
  if (graphPanel.style.height != "0px") {
     graphPanel.animate([
       { height: '330px' },
       { height: '0px' },
     ], {
       duration: 300,
       iteration: 1
     });
     graphPanel.style.height = "0px";
     tableau.animate([
       { height: '40%' },
       { height: '70%' },
     ], {
       duration: 300,
       iteration: 1
     });
     tableau.style.height = "70%";
  } else {
    graphPanel.animate([
       { height: '0px' },
       { height: '330px' },
     ], {
       duration: 300,
       iteration: 1
     });
     graphPanel.style.height = "330px";
     tableau.animate([
       { height: '70%' },
       { height: '40%' },
     ], {
       duration: 300,
       iteration: 1
     });
     tableau.style.height = "40%";
  }
});

var buttonLove = document.getElementById("love");
buttonLove.addEventListener("click", function() {
  var div1 = document.getElementById("BDD");
  var div2 = document.getElementById("loveDiv");

  if (div1.style.display == "none") {
     div1.style.display = "block";
     div2.style.display = "none";
  } else {
     div1.style.display = "none";
     div2.style.display = "block";
  }
});

window.onload = function() {
  var div1 = document.getElementById("BDD");
  var div2 = document.getElementById("loveDiv");

  div1.style.display = "block";
  div2.style.display = "none";
}


</script>
