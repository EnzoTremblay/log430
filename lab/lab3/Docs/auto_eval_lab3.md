# Auto-évaluation – Laboratoire 3

**Nom : Simon Tremblay**
**Code permanent :** TRES01119908
**Cours : LOG430 – Architecture Logicielle**
**Session Été 2025**

---

## Informations générales

- **URL du dépôt GitHub/GitLab :** https://github.com/SimonTremblay/log430
- **Langage utilisé :** Python
- **Framework utilisé :** Flask, FastAPI
- **Outils de tests :** Pytest, Postman

---

## 1. Autoévaluation par section

### 1.1 Structuration et REST API

| Éléments                                                                                       | Oui | Non | Commentaire / Justification                                                                                                    |
| ------------------------------------------------------------------------------------------------ | :-: | :-: | ------------------------------------------------------------------------------------------------------------------------------ |
| Les routes REST sont bien définies et respectent les conventions REST                           |  X  |    | Les routes suivent la nomenclature REST, sans verbes, versionnées (/api/v1/...), et respectent la séparation des ressources. |
| L’architecture suit un modèle MVC ou hexagonal (ou une autre architecture qui sera justifiée) |  X  |    | Architecture MVC respectée, logique métier isolée dans des services, contrôleurs REST distincts.                           |
| Les URIs sont bien structurées (ex : /api/v1/resource)                                          |  X  |    | Les URIs sont cohérentes, orientées ressource, et versionnées.                                                              |
| La couche API est clairement séparée de la logique métier                                     |  X  |    | Séparation stricte entre API et logique métier, facilitant la maintenance et l’évolution.                                  |

### 1.2 Documentation des API

| Éléments                                              | Oui | Non | Commentaire / Justification                                                     |
| ------------------------------------------------------- | :-: | :-: | ------------------------------------------------------------------------------- |
| La documentation Swagger (OpenAPI) est présente        |  X  |    | Documentation Swagger complète, fichier OpenAPI fourni, endpoints détaillés. |
| Les méthodes, statuts, entrées/sorties sont décrites |  X  |    | Toutes les méthodes, statuts et formats sont documentés dans Swagger.         |
| Swagger UI ou Redoc est intégré                       |  X  |    | Swagger UI intégré pour la visualisation et le test des endpoints.            |
| Des exemples de requêtes/réponses sont fournis        |  X  |    | Exemples inclus dans la documentation Swagger et README.                        |

### 1.3 Sécurité et accessibilité

| Éléments                                                               | Oui | Non | Commentaire / Justification                                                 |
| ------------------------------------------------------------------------ | :-: | :-: | --------------------------------------------------------------------------- |
| CORS est configuré correctement                                         |  X  |    | CORS activé pour permettre les appels externes.                            |
| Une authentification est implémentée (token statique, Basic Auth, JWT) |  X  |    | Authentification basique (token ou Basic Auth) sur les endpoints sensibles. |
| Les endpoints sensibles sont protégés                                  |  X  |    | Les endpoints critiques nécessitent une authentification.                  |

### 1.4 Tests et validation

| Éléments                                                   | Oui | Non | Commentaire / Justification                                  |
| ------------------------------------------------------------ | :-: | :-: | ------------------------------------------------------------ |
| Une collection Postman ou équivalente est fournie           |  X  |    | Collection Postman fournie pour tester l’API.               |
| Des tests automatisés (JUnit, MockMVC, etc.) sont présents |  X  |    | Tests automatisés avec Pytest sur les endpoints principaux. |
| Les tests sont intégrés à la CI/CD                        |  X  |    | Pipeline CI/CD déclenche les tests à chaque commit.        |

### 1.5 Déploiement et exécution

| Éléments                                                    | Oui | Non | Commentaire / Justification                                         |
| ------------------------------------------------------------- | :-: | :-: | ------------------------------------------------------------------- |
| L’API est conteneurisée avec Docker                         |  X  |    | Dockerfile et docker-compose fournis pour déploiement rapide.      |
| Les instructions d’exécution sont claires dans le README.md |  X  |    | README détaillé avec toutes les étapes d’exécution et de test. |
| L’API est fonctionnelle en local ou via conteneur            |  X  |    | API testée et fonctionnelle en local et via Docker.                |

### 1.6 Bonnes pratiques REST

| Éléments                                               | Oui | Non | Commentaire / Justification                                               |
| -------------------------------------------------------- | :-: | :-: | ------------------------------------------------------------------------- |
| Respect des verbes HTTP (GET, POST, PUT, DELETE, PATCH)  |  X  |    | Utilisation appropriée des verbes HTTP pour chaque action.               |
| Utilisation de codes HTTP standard (200, 201, 400, etc.) |  X  |    | Codes de statut HTTP explicites et conformes aux standards.               |
| Pagination, tri et filtrage implémentés si pertinent   |  X  |    | Pagination, tri et filtrage disponibles sur les collections volumineuses. |
| Messages d’erreur structurés et utiles                 |  X  |    | Messages d’erreur normalisés, formatés en JSON, avec détails utiles.  |

---

## 2. Réflexion personnelle

1. **Quelles sont les principales difficultés rencontrées lors de l’exposition de l’API RESTful ?**

   - Respect strict des conventions REST et de la cohérence des URIs
   - Séparation claire des couches métier/API
   - Sécurisation des endpoints et gestion des erreurs
2. **Qu’avez-vous appris en matière de bonnes pratiques REST ?**

   - Importance de la structure des URIs et du versionnage
   - Utilisation des bons verbes HTTP et codes de statut
   - Documentation exhaustive et exemples pour faciliter l’intégration
3. **Quels choix techniques avez-vous faits pour la documentation, les tests et la sécurité ?**

   - Swagger/OpenAPI pour la documentation
   - Pytest et Postman pour les tests
   - CORS et authentification basique pour la sécurité
4. **Que souhaiteriez-vous améliorer dans un futur projet API ?**

   - Ajouter des tests de charge et de performance
   - Renforcer la gestion des erreurs et la sécurité
   - Enrichir les cas d’usage métier et la documentation interactive
