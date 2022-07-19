## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Déploiement

#### Récapitulatif

- Le déploiement du site sur Heroku se fait via CircleCI.
- Lorsque l'application est poussée sur la branche main du registre GitHub, CircleCI lance les tests d'intégration, verifie le linter puis crée et pousse une image docker taguée sur un registre public Docker Hub.
- Si aucune erreur n'est détectée, CircleCI déploie alors l'application sur Heroku.
- Lorsque l'application est poussée sur une autre branche que la branche main du registre GitHub, CircleCI lance uniquement les tests et la vérification du linter.
- La surveillance de l’application et le suivi des erreurs sont assurés par Sentry.

#### Configurations

- Si nécessaire, créez un compte CircleCI, Heroku, Docker Hub et Sentry.

- Configuration Sentry:
  * Créer un projet pour django puis copier la clé `dsn` générée dans le fichier `.env` situé à la racine du code source de l'application (constante : SENTRY_DSN).


- Configuration Heroku:
  * Créer une app avec un nom valide puis dans le menu `settings/Config Vars` ajouter les variables d'environement: 
    - DJANGO_ALLOWED_HOSTS = nom-de-app.herokuapp.com
    - DJANGO_DEBUG = False
    - DJANGO_SECRET_KEY = (exemple de générateur de clé : `https://djecrety.ir/`)
    - SENTRY_DSN = clé dsn 


- Configuration CircleCI:
  * Après avoir créé un registre GitHub au nom du projet, configurer CircleCI en suivant les instructions : `https://circleci.com/docs/getting-started`
  * Dans `Project Settings` selectionner le menu `Environment Variables` puis ajouter les variables :
    - DJANGO_ALLOWED_HOSTS = localhost
    - DJANGO_DEBUG = True
    - DJANGO_SECRET_KEY = voir .env
    - DOCKERHUB_PASSWORD 
    - DOCKERHUB_USERNAME
    - HEROKU_API_KEY = (menu `accout settings`)
    - HEROKU_APP_NAME
    - SENTRY_DSN
  * Dans le fichier `config.yml`, au niveau de `build-and-push-to-dockerhub` dans `run` modifier les lignes:
    - `docker build -t nom_compte_docker/nom_du_depot:$TAG .`
    - `docker push nom_compte_docker/nom_depot:$TAG`
