# Rapport – Laboratoire 3

## 1. Objectif
Exposer les fonctionnalités du système multi-magasins via une API RESTful, documentée et sécurisée.

## 2. Changements apportés
- Ajout d’une couche API RESTful (Flask/FastAPI)
- Séparation des couches métier et présentation
- Documentation Swagger/OpenAPI
- Sécurisation (CORS, authentification basique)
- Tests d’API et intégration CI/CD

## 3. Endpoints principaux
- GET /api/v1/stores/{id}/stock : consulter le stock d’un magasin
- GET /api/v1/report : générer un rapport consolidé des ventes
- PUT /api/v1/products/{id} : mettre à jour un produit
- GET /api/v1/dashboard : visualiser les performances globales

## 4. Documentation technique
- Swagger/OpenAPI pour la description des endpoints
- Exemples de requêtes/réponses
- Screenshots Swagger/Postman
- Vue mise à jour du modèle 4+1

## 5. CI/CD
- Pipeline mis à jour pour inclure les tests d’API

## 6. Instructions
Voir README.md pour l’exécution et la documentation Swagger.
