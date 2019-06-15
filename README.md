# birbmeme-django

Project done for the Django course, using Django REST API

## Auteurs du projet :
- Axel VIGNY
- Laxman THAYALAN

## Heroku :
Le site est hebergé sur [Heroku](https://epita-python-2020.herokuapp.com/)
Attention sur Heroku notre système de gestion de Medias n'est pas fonctionnel (utilisation du service S3 requis), n'ayant pas trouvé de paliatif il est préférable de lancer le site directement via manage.py


## Documentation
La documentation se trouve sur ce [site](https://epita-python-2020.herokuapp.com/api/v1/docs/). Malheureusement, elle est incomplète.

## Les urls utilisables :
	/api/v1/docs/ : documentation Swagger

	api/v1/admin/ : connexion en tant qu'admin (vous devez crer un superuser auparavant)
		  ajout, suppression, modification des donnes via les pages suivantes

    /api/v1/accounts/signUp : permet de s'inscrire en tant qu'utilisateur normal
    
    /api/v1/accounts/<creator_id> : permet d'afficher le profil d'un utilisateur ayant pour id <creator_id>. (fonctionnalité partiellement réalisée)
    
	/api/v1/memes/ : liste des 25 derniers memes créés

	/api/v1/memes/<meme_id>/ : page du meme n°<meme_id>

	/api/v1/birbmeme/<meme_id>/eval : permet de noter le meme n°<meme_id>
	