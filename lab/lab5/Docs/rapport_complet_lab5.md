

# Rapport de laboratoire – Labo 5

## Cours : LOG430 – Architecture Logicielle
Session : Été 2025
Étudiant : Simon Tremblay

---

## 1. Objectifs
Ce laboratoire marque le passage à une architecture microservices, une étape clé pour la scalabilité et la modularité du système multi-magasins. Le projet a été décomposé en plusieurs services indépendants, chacun dédié à un domaine métier spécifique (produits, ventes, stock, clients, panier, commande). Cette approche permet de mieux répartir la charge, d’isoler les responsabilités et de faciliter l’évolution du système.

## 2. Réalisation
L’intégration d’un API Gateway (KrakenD) joue un rôle central dans l’orchestration des appels entre les microservices. Le Gateway gère la répartition des requêtes, la sécurité (CORS, authentification), et offre une interface unifiée pour les clients externes. La configuration dynamique des routes et le logging permettent de suivre précisément les flux et d’anticiper les problèmes potentiels.

L’orchestration multi-conteneurs via Docker Compose simplifie le déploiement et la gestion des services. Chaque microservice peut être développé, testé et mis à jour indépendamment, ce qui accélère les cycles de développement et réduit les risques d’erreur globale.

Le monitoring et l’observabilité sont maintenus grâce à Prometheus et Grafana, qui collectent et visualisent les métriques de chaque service. Cette supervision fine permet d’identifier rapidement les goulots d’étranglement, d’optimiser les performances et d’assurer la disponibilité du système.

La documentation technique inclut un rapport détaillé, un README d’utilisation et des diagrammes UML pour illustrer l’architecture et les séquences d’interaction. Ces éléments facilitent la compréhension du projet et son appropriation par de nouveaux développeurs ou intervenants.

## 3. Livrables
Les livrables comprennent le code source des microservices, la configuration de l’API Gateway, le Docker Compose multi-services, le rapport technique, le README et les diagrammes UML. L’ensemble est conçu pour être facilement déployé et testé dans différents environnements.

## 4. Points forts et axes d’amélioration
Parmi les points forts, on relève la modularité de l’architecture, la robustesse du Gateway et la qualité du monitoring. Les axes d’amélioration portent sur la gestion des erreurs inter-services, l’ajout de tests de charge multi-services et l’enrichissement de la documentation du Gateway pour une supervision optimale.

## 5. Instructions d’exécution
Pour exécuter et tester le projet, il suffit de suivre les instructions détaillées dans le README du labo 5, qui accompagne l’utilisateur dans toutes les étapes du déploiement et de la validation des services.

---

*rédigé avec l'aide de Chat GPT-4.1, une copie de mes requêtes peut être fournie au besoin*
