# ClientHub — API Flask, MySQL et Nginx

Lancer avec `docker compose -f docker-compose.yml up -d --build`.

- Portail Nginx : http://localhost:8080/
- Santé API : http://localhost:5000/health
- Clients depuis MySQL : http://localhost:5000/clients
- Logs : `docker compose -f docker-compose.yml logs -f api`

Les trois services partagent le réseau `clienthub-network`. L'API joint MySQL via le nom DNS `db`. Le volume nommé `clienthub-mysql-data` conserve les données et `init.sql` crée/remplit la table `clients` au premier démarrage. Le dossier `site/` est monté en lecture seule dans `/usr/share/nginx/html`.
