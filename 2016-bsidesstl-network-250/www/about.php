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
				<table>
					<tr>
						<td>Address</td>
						<td>1337 First Avenue</td>
					</tr>
					<tr>
						<td>Description</td>
						<td>Paula O's Pancake house, The best restaurant in all of Cyberville! We serve pancakes, and that's it! We are the only restaurant in all of Cyberville! Opinions are irrelevant!</td>
					</tr>
					<tr>
						<td>Mission</td>
						<td>To serve pancakes</td>
					</tr>
					<tr>
						<td>Awards</td>
						<td>
							<ul>
								<li>Number 1 best place to eat in all of Cyberville</li>
								<li>Best pancakes in all of Cyberville (awarded by the mayor)</li>
							</ul>
						</td>
					</tr>
					<tr>
						<td>Products</td>
						<td>
							<ul>
								<li>Pancakes</li>
								<li>Maple Syrup</li>
							</ul>
						</td>
					</tr>
				</table>
			</div>
		</div>
	</div>
</body>
</html>