# README – Laboratoire 3

## Instructions d’exécution

1. Installer les dépendances :
   ```bash
   pip install fastapi uvicorn pydantic
   ```
2. Lancer l’API RESTful :
   ```bash
   uvicorn lab.lab3.api.main:app --reload
   ```
3. Accéder à la documentation Swagger UI :
   - Ouvrir [http://localhost:8000/docs](http://localhost:8000/docs)
   - Token d’authentification : `secret-token`

## Endpoints principaux
- `GET /api/v1/rapport` : Rapport consolidé des ventes
- `GET /api/v1/magasins/{magasin_id}/stock` : Stock d’un magasin
- `GET /api/v1/dashboard` : Tableau de bord global
- `PUT /api/v1/produits/{produit_id}` : Mise à jour d’un produit

## Sécurité
- Authentification par token (paramètre `token` dans la requête)
- CORS activé pour tous les domaines

## Documentation technique
- Swagger (OpenAPI) : `lab/lab3/api/swagger.yaml`
- Exemples de requêtes disponibles dans Swagger UI

## Tests
- À compléter : tests automatisés des endpoints (pytest, requests)
- Intégration dans la CI/CD
