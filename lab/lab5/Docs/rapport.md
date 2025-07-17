# Rapport – Laboratoire 5 (Arc42)

## 1. Objectif
Faire évoluer le système multi-magasins vers une architecture microservices avec API Gateway et observabilité.

## 2. Changements apportés
- Découpage en microservices : produits, ventes, stock, clients, panier, commande
- Mise en place d’une API Gateway (Kong/KrakenD)
- Load balancing et sécurisation des accès
- Documentation technique, rapport Arc42, ADR
- Tests de charge et observabilité (Grafana, Prometheus)

## 3. Architecture
- Microservices déployés dans des conteneurs Docker
- API Gateway configurée pour le routage, la sécurité et le monitoring
- Load balancing entre instances de microservices

## 4. Documentation technique
- Fichier Swagger/OpenAPI mis à jour
- Scripts de test de charge
- Tableaux comparatifs et graphiques Grafana
- Instructions d’exécution

## 5. CI/CD
- Pipeline mis à jour pour inclure les tests de charge et la collecte de métriques

## 6. Comparaison des architectures
- Tests de charge sur API directe vs API Gateway
- Analyse des performances et de la résilience

## 7. Instructions
Voir README.md pour l’exécution et la visualisation Grafana.
