# Rapport – Laboratoire 4

## 1. Objectif
Optimiser les performances du système multi-magasins via le load balancing, le caching, les tests de charge et l’observabilité.

## 2. Changements apportés
- Ajout de scripts de test de charge (k6, JMeter)
- Ajout d’un load balancer (NGINX/Docker Compose)
- Mise en place du cache sur les endpoints critiques
- Ajout de métriques Prometheus et dashboards Grafana
- Documentation des résultats et comparatifs

## 3. Tests et résultats
- Test de charge initial : latence, trafic, erreurs, saturation
- Ajout du load balancer : comparaison des performances selon N instances
- Mise en cache : réduction de la latence et de la charge DB
- Résilience : tolérance aux pannes

## 4. Documentation technique
- Scripts de test de charge
- Configuration du cache et du load balancer
- Tableaux comparatifs et graphiques Grafana
- Instructions d’exécution

## 5. CI/CD
- Pipeline mis à jour pour inclure les tests de charge et la collecte de métriques

## 6. Instructions
Voir README.md pour l’exécution et la visualisation Grafana.
