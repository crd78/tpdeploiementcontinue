# Exercice Docker — COPY et volumes

## COPY dans une image

Le système de fichiers d'une image ou d'un conteneur est isolé de l'hôte. `COPY` transfère un fichier du contexte de build vers l'image. Construire avec `docker build -f Dockerfile.copy-demo -t copy-demo .`, puis vérifier avec `docker run --rm copy-demo ls -la` et `docker run --rm copy-demo python3 app-copy.py`.

## MySQL sans volume

Lancer MySQL avec `docker run -d --name mysql-no-volume -p 3307:3306 -e MYSQL_ROOT_PASSWORD=example mysql:8.4`, créer la base `test` et la table `customer`, puis supprimer le conteneur. Après recréation, les données ont disparu.

## MySQL avec volume

Créer `mysql-data-demo` avec `docker volume create`, puis lancer MySQL avec `-v mysql-data-demo:/var/lib/mysql`. Après suppression et recréation du conteneur avec le même volume, la base `test` existe toujours : les données résident dans le volume. `docker volume ls` permet de vérifier le volume.

Le `compose.yml` utilise déjà un volume nommé `mysql-data`.
