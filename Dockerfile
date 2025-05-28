# Utiliser une image Python légère comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY app.py /app/app.py
COPY test_app.py /app/test_app.py

# Installer pytest pour les tests
RUN pip install pytest

# Commande par défaut pour exécuter l'application
CMD ["python", "app.py"]
