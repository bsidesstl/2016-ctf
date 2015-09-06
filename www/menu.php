<!DOCTYPE html>
<html>
<head>
	<title>Paula O's Pancake House</title>
	<link href="main.css" rel="stylesheet"/>
</head>
<body>
	<div id="outer">
		<div id="inner">
			<div id="header">
				<img src="header.png"/>
			</div>

			<div id="navbar">
				<ul>
					<li><a href="index.php">Home</a></li>
					<li><a href="about.php">About</a></li>
					<?php 
						date_default_timezone_set('America/New_York');
						echo "<li><a href=\"menu.php?day=".strtolower(date('l')).".txt\">Menu</a></li>";
					?>
				</ul>
			</div>
			
			<div id="content">
				<!-- Load content for menu here -->
				<div id="menu">
					<?php 
						echo shell_exec("cat menus/default.txt");

						echo shell_exec("cat menus/".$_GET['day']);
					?>
				</div>
			</div>
		</div>
	</div>
</body>
</html>