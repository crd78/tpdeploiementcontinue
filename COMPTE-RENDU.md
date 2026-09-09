# Compte-rendu — GitHub Actions

## Principe

GitHub Actions est un mécanisme de pipeline qui exécute automatiquement des tâches sur un runner hébergé par GitHub. Il peut lancer des tests, contrôler la qualité du code, produire des artefacts ou déclencher un déploiement.

Le fichier de configuration se trouve dans `.github/workflows/` et est écrit en YAML.

## `uses:`

Une étape `uses:` réutilise une action existante publiée dans un dépôt GitHub ou une action locale. Par exemple, `actions/checkout@v4` télécharge le contenu du dépôt dans le runner. Cela évite de réécrire cette logique dans une commande shell. Le suffixe `@v4` fixe la version majeure utilisée.

## Déclencheurs

`on: [push]` signifie que le workflow est lancé lorsqu'un push est effectué sur une branche.

Les déclencheurs courants sont :

- `push` : push vers une ou plusieurs branches ;
- `pull_request` : ouverture ou mise à jour d'une pull request ;
- `workflow_dispatch` : lancement manuel depuis l'onglet Actions ;
- `schedule` : lancement selon une expression cron ;
- `workflow_call` : appel depuis un autre workflow ;
- `release` : publication ou modification d'une release ;
- `issues` et `issue_comment` : événements liés aux issues ;
- `workflow_run` : fin d'un autre workflow.

Le workflow de ce dépôt accepte `push`, `workflow_dispatch` et `schedule`.

GitHub ne garantit pas les planifications plus fréquentes que toutes les cinq minutes ; le dépôt utilise donc `*/5 * * * *`.

## Checkout et exécution Python

Sans `actions/checkout@v4`, le runner démarre sans les fichiers du dépôt. L'étape checkout récupère le code, puis `job.py` peut être exécuté avec Python.

Le script affiche `coucou 2` et lit le secret `SECRET_API_TOKEN` via une variable d'environnement.

## Fichier et artefact

Le workflow crée `pipeline-output.txt`. Un runner étant éphémère, ce fichier disparaît à la fin du job s'il n'est pas conservé.

`actions/upload-artifact@v4` l'enregistre comme artefact téléchargeable depuis la page de l'exécution. En production, un artefact peut être un rapport de tests, un binaire compilé, un paquet, une image exportée ou des journaux de diagnostic.

## Secrets

Le secret `SECRET_API_TOKEN` doit être créé dans les Settings du dépôt avec la valeur demandée par l'exercice. Il est injecté dans le job avec :

```yaml
env:
  SECRET_API_TOKEN: ${{ secrets.SECRET_API_TOKEN }}
```

Il ne faut jamais écrire la valeur du secret en clair dans le dépôt ou les logs. Le script vérifie uniquement sa présence et affiche une confirmation masquée.
