# Auto-évaluation – Laboratoire 4

**Nom : Simon Tremblay**
**Code permanent :** TRES01119908
**Cours : LOG430 – Architecture Logicielle**
**Session Été 2025**

---

## Informations générales

- **URL du dépôt GitHub/GitLab :** https://github.com/SimonTremblay/log430
- **Outil de test de charge utilisé :** k6
- **Outil(s) de monitoring utilisé(s) :** Prometheus, Grafana
- **Outil de load balancing :** NGINX
- **Mécanisme de cache implémenté :** LRU cache local

---

## 1. Évaluation technique par composant

### 1.1 Instrumentation et observabilité initiale

| Critère                                                                                     | Oui | Non | Commentaire / Justification                                     |
| -------------------------------------------------------------------------------------------- | :-: | :-: | --------------------------------------------------------------- |
| Des logs structurés ont été intégrés à l’application                                  |  X  |    | Logs structurés ajoutés pour tracer les requêtes et erreurs. |
| Un endpoint de métriques est exposé (Prometheus, Actuator, etc.)                           |  X  |    | Endpoint Prometheus exposé pour la collecte des métriques.    |
| Les métriques de base sont correctement collectées (requêtes, erreurs, temps de réponse) |  X  |    | Métriques de base collectées et visualisées dans Grafana.    |
| Les logs permettent de tracer les requêtes de bout en bout                                  |  X  |    | Les logs permettent une traçabilité complète des requêtes.  |

### 1.2 Monitoring et visualisation (Grafana)

| Critère                                                                                                                                                   | Oui | Non | Commentaire / Justification                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | :-: | :-: | ----------------------------------------------------------------------- |
| Un serveur de visualisation des métriques a-t-il été déployé et connecté à une source de collecte de données pour faciliter le suivi du système ? |  X  |    | Grafana déployé et connecté à Prometheus pour le suivi du système. |
| Un ou plusieurs dashboards ont été configurés à l’aide de templates existants ou personnalisés                                                       |  X  |    | Dashboards Grafana configurés pour visualiser les indicateurs clés.   |
| Les 4 Golden Signals sont représentés visuellement                                                                                                       |  X  |    | Les 4 Golden Signals sont présents dans les dashboards Grafana.        |
| Les résultats des tests sont documentés (captures, exports de données, analyses)                                                                        |  X  |    | Captures et exports des résultats de tests inclus dans le rapport.     |

### 1.3 Test de charge initial (baseline)

| Critère                                                                                       | Oui | Non | Commentaire / Justification                                           |
| ---------------------------------------------------------------------------------------------- | :-: | :-: | --------------------------------------------------------------------- |
| Des scénarios de test pertinents ont été définis (lecture/écriture, simultanéité, etc.) |  X  |    | Scénarios de test variés pour lecture, écriture et simultanéité. |
| Des données réalistes ou représentatives ont été injectées                               |  X  |    | Données représentatives utilisées pour les tests de charge.        |
| Les métriques de performances ont été collectées en condition de charge                    |  X  |    | Métriques collectées et analysées sous charge.                     |
| Une analyse de la saturation ou des goulots d’étranglement a été menée                    |  X  |    | Analyse des goulots d’étranglement réalisée et documentée.       |

### 1.4 Load Balancing

| Critère                                                                         | Oui | Non | Commentaire / Justification                                   |
| -------------------------------------------------------------------------------- | :-: | :-: | ------------------------------------------------------------- |
| Un répartiteur de charge a été mis en place (NGINX, HAProxy, etc.)            |  X  |    | NGINX configuré comme répartiteur de charge.                |
| Plusieurs instances de service ont été déployées derrière le répartiteur   |  X  |    | Plusieurs instances déployées derrière NGINX.              |
| Les tests de charge ont été répétés avec load balancing activé             |  X  |    | Tests de charge réalisés avec load balancing activé.       |
| Les métriques avant/après ont été comparées rigoureusement                  |  X  |    | Comparatif des métriques avant/après load balancing inclus. |
| Un comportement de tolérance aux pannes a été testé (arrêt d’une instance) |  X  |    | Tolérance aux pannes testée en arrêtant une instance.      |

### 1.5 Caching applicatif

| Critère                                                                             | Oui | Non | Commentaire / Justification                                       |
| ------------------------------------------------------------------------------------ | :-: | :-: | ----------------------------------------------------------------- |
| Les endpoints critiques ont été identifiés (latence élevée ou forte fréquence) |  X  |    | Endpoints critiques identifiés et optimisés.                    |
| Un mécanisme de cache a été ajouté (ex : @Cacheable, Redis...)                   |  X  |    | Cache LRU ajouté sur les endpoints à forte latence.             |
| Des règles d’expiration, d’invalidation ou de cohérence ont été définies      |  X  |    | Règles d’expiration et d’invalidation définies pour le cache. |
| L’impact du cache a été mesuré en termes de latence et de charge serveur         |  X  |    | Impact du cache mesuré et documenté dans le rapport.            |

---

## 2. Réflexion personnelle approfondie

1. **Instrumentation :** Quelle stratégie avez-vous adoptée pour instrumenter votre système ? Quels types de métriques vous ont semblé les plus révélateurs ?
   - Ajout de logs structurés et exposition d’un endpoint de métriques Prometheus pour suivre les requêtes, erreurs et temps de réponse. Latence, taux d’erreur, saturation, trafic (Golden Signals) sont les plus révélateurs.
2. **Monitoring :** Dans quelle mesure l’utilisation de visualisations (par exemple via Grafana) peut-elle aider à identifier des faiblesses ou des comportements inattendus ?
   - Grafana permet d’identifier rapidement les pics de latence, les erreurs et les saturations, facilitant le diagnostic et l’optimisation.
3. **Load Balancing :** Quelles sont les limites d’une simple répartition de charge dans le contexte de votre architecture ? Quelles optimisations complémentaires envisageriez-vous ?
   - Load balancing simple ne gère pas la persistance de session ni la répartition intelligente selon la charge réelle. Optimisations : sticky sessions, balancing dynamique, monitoring avancé.
4. **Caching :** Quels ont été les bénéfices mesurés du cache ? Quels risques potentiels avez-vous identifiés (cohérence, obsolescence, etc.) ?
   - Réduction de la latence et de la charge serveur. Risques : incohérence des données, obsolescence du cache, invalidation complexe.
5. **Approche séquentielle :** En comparant chaque étape (baseline, balancing, cache), laquelle a eu l’effet le plus significatif sur les performances ? Pourquoi ?
   - Le cache a eu l’impact le plus fort sur la latence, suivi du load balancing pour la scalabilité.
6. **Professionnalisation :** Quelles compétences ou outils appris dans ce laboratoire pensez-vous réutiliser dans un projet réel en entreprise ?
   - Monitoring avec Prometheus/Grafana, tests de charge, configuration NGINX, gestion du cache, analyse de performance.

---

> [1] https://sre.google/sre-book/monitoring-distributed-systems/
