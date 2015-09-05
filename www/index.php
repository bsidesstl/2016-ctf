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
						echo "<li><a href=\"menu.php?day=".strtolower(date('l')).".txt\">Menu</a></li>";
					?>
				</ul>
			</div>
			
			<div id="content">
				<img src="gallery.png"/>
			</div>
		</div>
	</div>
</body>
</html>