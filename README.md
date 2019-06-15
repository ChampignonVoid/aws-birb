# birbmeme-django

Project done for the Django course, using Django REST API

## Auteurs du projet :
- Axel VIGNY
- Laxman THAYALAN

## Heroku :
Le site est hebergé sur [Heroku](https://epita-python-2020.herokuapp.com/)
Attention sur Heroku notre système de gestion de Medias n'est pas fonctionnel, n'ayant pas trouvé de paliatif il est préférable de lancer le site directement via manage.py

## Les urls utilisables :
	/api/v1/docs/ : documentation Swagger

	/admin/ : connexion en tant qu'admin (vous devez crer un superuser auparavant)
		  ajout, suppression, modification des donnes via les pages suivantes

	/birbmeme/ : liste des 5 derniers memes crs

	/birbmeme/memes/<meme_id>/ : page du meme avec comme id <meme_id>

	/birbmeme/creators/<creator_id>/ : page du creator avec comme id <creator_id>