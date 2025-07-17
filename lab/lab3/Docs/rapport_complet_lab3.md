

# Rapport de laboratoire – Labo 3

## Cours : LOG430 – Architecture Logicielle
Session : Été 2025
Étudiant : Simon Tremblay

---

## 1. Objectifs
Ce laboratoire avait pour objectif d’exposer les principales fonctionnalités métier d’un système multi-magasins à travers une API RESTful robuste et évolutive. L’enjeu était de garantir l’interopérabilité avec des clients externes, tout en assurant une séparation claire entre les couches métier, présentation et accès aux données.

## 2. Réalisation
L’architecture mise en place repose sur une couche API RESTful, structurée autour de routes cohérentes et versionnées (ex : `/api/v1/products`). Le format JSON est utilisé par défaut, et le Content Negotiation est supporté pour une meilleure flexibilité.

La documentation de l’API a été réalisée avec Swagger (OpenAPI 3.0), permettant de décrire précisément chaque endpoint, les méthodes HTTP, les statuts de réponse et des exemples de requêtes/réponses. L’intégration de Swagger UI facilite la visualisation et le test interactif de l’API, rendant la prise en main rapide pour tout développeur ou testeur.

La sécurité n’a pas été négligée : le CORS est activé pour permettre les appels depuis des clients distants, et une authentification basique protège les endpoints sensibles. Cette approche garantit que seules les requêtes autorisées peuvent accéder aux ressources critiques du système.

Les tests ont été pensés pour couvrir l’ensemble des fonctionnalités exposées. Une collection Postman est fournie pour valider manuellement les endpoints, tandis que des tests automatisés (Pytest) assurent la non-régression et la robustesse du code. L’intégration des tests dans le pipeline CI/CD permet de garantir la qualité à chaque modification du code.

Le respect des bonnes pratiques REST a guidé toute la conception : les URIs sont orientées ressource, les verbes HTTP sont utilisés à bon escient, et les codes de statut sont explicites. Les messages d’erreur sont normalisés pour faciliter le diagnostic côté client. Pour les collections volumineuses, la pagination, le filtrage et le tri sont implémentés, assurant des performances optimales et une expérience utilisateur fluide.

Plusieurs cas d’usage métier ont été couverts, dont la génération de rapports consolidés de ventes, la consultation du stock d’un magasin, la visualisation des performances globales et la mise à jour des informations produit. Ces scénarios illustrent la capacité du système à répondre aux besoins concrets d’une entreprise multi-magasins.

## 3. Livrables
Les livrables incluent le code source, la documentation Swagger, la collection Postman, le rapport technique, le README d’utilisation et la grille d’auto-évaluation. L’ensemble est organisé pour faciliter la prise en main, la maintenance et l’évolution future du projet.

## 4. Points forts et axes d’amélioration
Parmi les points forts, on note le respect des conventions REST, la documentation complète et accessible, ainsi que l’intégration de la sécurité et des tests. Les axes d’amélioration identifiés concernent l’enrichissement des cas d’usage, l’ajout de tests de charge et le renforcement de la gestion des erreurs pour une version finale encore plus robuste.

## 5. Instructions d’exécution
Pour exécuter et tester le projet, il suffit de suivre les instructions détaillées dans le README du labo 3, qui guide l’utilisateur pas à pas pour l’installation, l’exécution et la validation des endpoints.

---

*rédigé avec l'aide de Chat GPT-4.1, une copie de mes requêtes peut être fournie au besoin*
