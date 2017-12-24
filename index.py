#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi 

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="UTF-8">
	<title>Conquesty - Jeu Stratégie Spatiale</title>
	<link rel="stylesheet" type="text/css" href="/dist/css/main.css">
</head>
<body>
	<header>
		<div class="logo">
			Conquesty
		</div>

		<nav>
			<ul>
				<li><a href="">Planètes</a></li>
				<li><a href="">Flottes</a></li>
				<li><a href="">Galaxie</a></li>
				<li><a href="">Recherche</a></li>
				<li><a href="">Construction</a></li>
				<li><a href="">Alliance</a></li>
			</ul>
		</nav>

	</header>

	<div class="wrapper">
		<div class="left">
			<h1>Ressources</h1>
			<div class="ressources">
				<h2>Métal :</h2>
				<h2>Cristal :</h2>
				<h2>Gaz :</h2>
				<h2>Energie :</h2>
				
			</div>

			<h1>Planètes</h1>
			<div class="param">
				
			</div>
		</div>

		<div class="right">
		</div>


	</div>
</body>
</html>
"""

print(html)
