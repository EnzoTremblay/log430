# README – Laboratoire 3

## Instructions d’exécution

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/EnzoTremblay/log430.git
   ```
2. Se placer dans le dossier du projet :
   ```bash
   cd log430
   ```
3. Lancer l’API REST avec Docker Compose :
   ```bash
   docker-compose up --build
   ```
4. Accéder à la documentation Swagger UI :
   - Ouvrir [http://localhost:5000/docs](http://localhost:5000/docs) dans le navigateur.

## Structure du projet
- `app.py` : Application principale
- `api.py` : API RESTful (Flask/FastAPI)
- `test_api.py` : Tests d’API
- `Docs/` : Documentation technique (Swagger, exemples, suivi)
- `lab/` : Dossiers des laboratoires

## Liens utiles
- [Dépôt GitHub principal](https://github.com/EnzoTremblay/log430)
- Swagger UI : [http://localhost:5000/docs](http://localhost:5000/docs)
