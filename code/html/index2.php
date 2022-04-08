<html>

<head>
        <title>Test Interface BDD</title>
        <meta charset ="UTF-8">
        <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
</head>

<body>
        <h1>Base De Donnee Rob</h1>
	<div id="tableau">
        <table id="customers">
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
        </body>

		<table id="tabGraphique">
        <tr><td>
        <div id="graphique">
                <canvas id="firstChart"></canvas>
        </div></td><td>
        <div id="graphique">
                <canvas id="secondChart"></canvas>
        </div></td>
        </tr>
</table>
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

</script>


<style>

html {
 background-color: #FBFDFF;
 font-family: Arial, Helvetica, sans-serif;
 padding:10px 30px 0px 30px;
}

h1 {
 padding-left: 30px;
}

#tableau {
  overflow:scroll;
  height: 40%;
}

#tabGraphique {
  width : 90%;
}

#graphique {
  margin-top: 20px;
  padding: 10px;
}

#customers {
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px none #ddd;
  padding: 8px;
  border-collapse: collapse;
}

#customers #midCollumn{
  border-left:1px solid #f2f2f2;
  border-right:1px solid #f2f2f2;
}

#customers tr:nth-child(even){background-color: #D0E2FC;}

#customers tr:hover {background-color: #FFE9C7;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
