# Application Hello World

## Description
Ceci est une application Python minimale qui affiche "Hello World" dans la console. Le projet est conteneurisé avec Docker, orchestré avec Docker Compose, et inclut un pipeline CI/CD configuré avec GitHub Actions.

## Structure du Projet
```
/home/log430
├── app.py                 # Fichier principal de l'application
├── test_app.py            # Tests unitaires pour l'application
├── Dockerfile             # Dockerfile pour conteneuriser l'application
├── docker-compose.yml     # Configuration Docker Compose
└── .github/workflows/ci.yml # Workflow GitHub Actions pour CI/CD
```

## Prérequis
- Python 3.10 ou supérieur
- Docker et Docker Compose
- Compte GitHub pour le pipeline CI/CD

## Installation et Utilisation

### 1. Exécuter l'Application Localement
```bash
python3 app.py
```

### 2. Exécuter les Tests Unitaires
Installer `pytest` si ce n'est pas déjà fait :
```bash
pip install pytest
```
Lancer les tests :
```bash
pytest
```

### 3. Construire et Exécuter avec Docker
Construire l'image Docker :
```bash
docker build -t hello-world-app .
```
Exécuter le conteneur :
```bash
docker run --rm hello-world-app
```

### 4. Orchestrer avec Docker Compose
Démarrer l'application avec Docker Compose :
```bash
docker-compose up
```

### 5. Pipeline CI/CD
Le workflow GitHub Actions est configuré pour :
- Exécuter les tests unitaires
- Construire l'image Docker
- Pousser l'image sur Docker Hub

Pour utiliser le pipeline :
1. Poussez votre code dans un dépôt GitHub.
2. Configurez les secrets dans le dépôt pour les identifiants Docker Hub :
   - `DOCKER_USERNAME` : Votre nom d'utilisateur Docker Hub
   - `DOCKER_PASSWORD` : Votre mot de passe Docker Hub

## Licence
Ce projet est sous licence MIT.
