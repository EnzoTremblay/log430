# Rapport – Laboratoire 2 (Arc42)

## 1. Résumé des Labs 0 et 1
- Lab 0 : Mise en place du dépôt, application minimale, CI/CD, conteneurisation.
- Lab 1 : Application 2-tiers, persistance avec SQLAlchemy, tests, documentation technique, ADR, UML.

## 2. Analyse et continuité
- Éléments à conserver : structure du dépôt, CI/CD, Docker, tests unitaires, documentation.
- Éléments à modifier : architecture pour multi-magasins, synchronisation des données, gestion centralisée.
- Nouvelles exigences : gestion simultanée de plusieurs magasins, consultation centralisée, synchronisation fiable, rapports consolidés, évolutivité web/mobile.
- Défis : cohérence des données, scalabilité, modularité, observabilité.
- Sous-domaines DDD : ventes en magasin, gestion logistique, supervision maison mère.

## 3. Proposition d’architecture
- Architecture orientée services (SOA), modules pour chaque magasin, centre logistique, maison mère.
- Communication via API REST et événements asynchrones.
- Justification via ADR (voir Docs/ADR1.md et Docs/ADR2.md).
- Diagrammes UML (4+1) : logique, processus, implémentation, déploiement, cas d’utilisation.

## 4. Exigences fonctionnelles (MoSCoW)
- Must have : rapport consolidé des ventes, consultation du stock central, tableau de bord, synchronisation des données.
- Should have : mise à jour des produits, approvisionnement magasin.
- Could have : alertes automatiques, interface web minimale.

## 5. Technologies choisies
- Python, SQLAlchemy, Docker, Docker Compose, Grafana, API REST, Event Sourcing.

## 6. Structure du projet et instructions d’exécution
- Voir README.md pour les détails.

## 7. CI/CD
- Pipeline GitHub Actions pour tests, build, déploiement Docker.
- Intégration des tests automatisés et vérification de la synchronisation.

## 8. Liens et livrables
- Dépôt GitHub : https://github.com/EnzoTremblay/log430
- Fichier .zip contenant le code source des Labs 0, 1 et 2.
