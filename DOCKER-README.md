Lancer `pip install -r requirements.txt` puis `python app.py` pour tester Flask sans conteneur.

Construire l'image avec `docker build -t flask-demo .`, puis `docker run -d --name flask-demo -p 5000:5000 flask-demo`. `-p` publie le port, `-d` détache le processus et `docker logs flask-demo` affiche les requêtes.

Créer le réseau avec `docker network create exonet`, démarrer MySQL avec `--network exonet`, puis utiliser `Dockerfile.mysql-client` et `mysql -h mysql-demo -uroot -pexample --protocol=tcp`.

Lancer le mini-projet avec `docker compose -f compose.yml up -d --build`, puis ouvrir http://localhost:5000/. Le service web joint MySQL par le DNS `mysql` sur le réseau user-defined bridge `exonet`.

Le bridge par défaut fournit une connectivité IP basique ; un user-defined bridge ajoute le DNS par nom et une isolation configurable ; host partage la pile réseau de l'hôte et réduit l'isolation.
