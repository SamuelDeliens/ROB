
<html>
<head>
    <title>Test Base de donnée</title>
</head>
<body>
<h1>jihad</h1>
<table>
        <tr>
                <th>id</th>
                <th>date</th>
                <th>pH</th>
        </tr>

<?php
        $host= 'localhost';
        $dbname= 'Rob';
        $username= 'root';
        $password= 'pi';
        $dsn ="mysql:host=".$host.";dbname=".$dbname;

        $sql= "SELECT * FROM capteur";


        $pdo= new PDO($dsn, $username, $password);

        $stmt = $pdo->prepare($sql);
	$stmt->execute();
	$reponse=$stmt->fetchAll();

		foreach ($reponse as $row){
?>
	<tr>
			<th><?php echo $row['id'];?></th>
			 <th><?php echo $row['date'];?></th>
			 <th><?php echo $row['pH'];?></th>
		</tr>
<?php
}
        $pdo=null;
?>
<div>
 <canvas id="myChart"></>
<script>
	var reponse=<?php echo json_encode($reponse);?>;
	console.log(reponse);

</script>
</table>
</body>
</html>
