

# Rapport de laboratoire – Labo 4

## Cours : LOG430 – Architecture Logicielle
Session : Été 2025
Étudiant : Simon Tremblay

---

## 1. Objectifs
Ce laboratoire avait pour objectif d’optimiser les performances et la scalabilité du système multi-magasins en intégrant des mécanismes avancés de cache, de load balancing et d’observabilité.

## 2. Réalisation
L’architecture a été enrichie par l’ajout d’un cache (LRU ou Redis) sur les endpoints critiques, permettant de réduire la latence et la charge serveur. Un load balancer NGINX a été mis en place devant l’API pour répartir efficacement les requêtes et garantir la tolérance aux pannes.

L’observabilité du système a été renforcée grâce à l’intégration de Prometheus et Grafana. Les métriques API (nombre de requêtes, latence, taux d’erreur) sont exportées et visualisées dans des dashboards personnalisés, facilitant le suivi en temps réel et l’identification des goulots d’étranglement. Cette approche permet d’anticiper les problèmes de saturation et d’ajuster les ressources en conséquence.

Des tests de charge ont été réalisés à l’aide de k6 ou JMeter, avec des scénarios variés pour simuler des accès concurrents et des volumes importants de données. Les scripts de test inclus dans le projet permettent de reproduire ces conditions et de valider la robustesse de l’API sous contrainte. Les résultats sont documentés par des captures d’écran et des exports de données, illustrant l’impact des optimisations apportées.

La documentation technique détaille l’ensemble des choix d’architecture, les configurations des outils (NGINX, Prometheus, Grafana), ainsi que les étapes d’installation et d’exécution. Le README guide l’utilisateur pour déployer et tester le système dans différents environnements.

## 3. Livrables
Les livrables comprennent le code source et la configuration, les fichiers de configuration NGINX, Prometheus et Grafana, les scripts de test de charge, le rapport technique, le README et la grille d’auto-évaluation. L’ensemble est conçu pour faciliter le déploiement, la supervision et l’évolution du projet.

## 4. Points forts et axes d’amélioration
Parmi les points forts, on note la mise en cache efficace, le load balancing opérationnel et l’intégration du monitoring. Les axes d’amélioration concernent le développement d’un monitoring plus fin, la mise en place d’alertes automatisées et l’enrichissement de la documentation des métriques pour une supervision encore plus proactive.

## 5. Instructions d’exécution
Pour exécuter et tester le projet, il suffit de suivre les instructions détaillées dans le README du labo 4, qui accompagne l’utilisateur pas à pas.

---

*rédigé avec l'aide de Chat GPT-4.1, une copie de mes requêtes peut être fournie au besoin*
