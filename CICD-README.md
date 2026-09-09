# CI/CD ClientHub

Le workflow `.github/workflows/ci-cd.yml` se déclenche sur chaque push vers `main`.

1. `unit-tests` installe les dépendances et lance les tests unitaires.
2. `e2e-tests` dépend du premier job et vérifie `/health` et `/clients` via HTTP.
3. `build-push` dépend des deux tests, construit l'image et la publie sur Docker Hub avec `latest` et `sha-<commit>`.
4. `deploy` dépend du build, se connecte en SSH à la VM Azure, récupère l'image, recrée idempotemment `myapp` et `myapp-db`, puis vérifie `/health`.

Les jobs `needs` empêchent le build et le déploiement si un test échoue. Les noms fixes et `docker rm -f ... || true` rendent le déploiement idempotent.

Secrets à configurer dans Settings → Secrets and variables → Actions : `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `AZURE_VM_HOST`, `AZURE_VM_USER`, `AZURE_VM_SSH_KEY`, `MYSQL_ROOT_PASSWORD`. Aucun secret réel ne doit être commité. La VM doit avoir Docker et `curl`, et autoriser TCP 80 dans son NSG Azure.
