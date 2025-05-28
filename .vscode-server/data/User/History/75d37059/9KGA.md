# Rapport – Laboratoire 1

## 1. Informations générales
- **URL du dépôt GitHub/GitLab** : [https://github.com/EnzoTremblay/log430](https://github.com/EnzoTremblay/log430)
- **Langage utilisé** : Python
- **Base de données utilisée** : SQLite
- **ORM utilisé** : SQLAlchemy ORM

## 2. Auto-évaluation par section

### 2.1 Structuration du dépôt
| Éléments | Oui | Non | Commentaire / Justification |
|----------|-----|-----|-----------------------------|
| Le fichier README.md est présent et complet | x | | Le fichier README.md inclut une description complète, la structure du projet, les prérequis, et les instructions d'installation. |
| Un fichier .gitignore pertinent est utilisé | x | | Le fichier `.gitignore` exclut les fichiers temporaires et les artefacts générés. |
| Le dépôt présente une structure claire et logique | x | | La structure du projet est bien organisée avec des répertoires dédiés pour la documentation et les tests. |

### 2.2 Application client
| Éléments | Oui | Non | Commentaire / Justification |
|----------|-----|-----|-----------------------------|
| Elle permet de rechercher, ajouter, consulter, retourner des produits | x | | Les fonctionnalités de recherche, ajout, et consultation sont implémentées via SQLAlchemy ORM. |
| L’interface est claire et fonctionnelle | x | | L'interface CLI est simple et intuitive. |

### 2.3 Persistance et ORM
| Éléments | Oui | Non | Commentaire / Justification |
|----------|-----|-----|-----------------------------|
| Un ORM est utilisé pour gérer la persistance | x | | SQLAlchemy ORM est utilisé pour abstraire la couche de persistance. |
| L’application accède correctement à la base de données | x | | Les opérations de lecture et écriture fonctionnent correctement. |
| Les opérations de lecture et d’écriture sont persistées | x | | Les données sont sauvegardées dans SQLite. |
| La base de données est cohérente après plusieurs opérations concurrentes | x | | Les transactions sont gérées correctement. |
| L’utilisation des indexes dans la base de données est bien appliquée et justifiée | x | | Des indexes sont ajoutés aux colonnes fréquemment interrogées (`nom`, `categorie`, `date`). |

### 2.4 Justifications et documentation
| Éléments | Oui | Non | Commentaire / Justification |
|----------|-----|-----|-----------------------------|
| Au moins deux décisions architecturales (ADR) sont rédigées | x | | Deux ADR sont présentes dans le répertoire `Docs/ADR`. |
| Les choix technologiques sont documentés | x | | Les choix technologiques sont expliqués dans les ADR et le README.md. |
| Les diagrammes UML sont présents (classes, séquence, déploiement) | x | | Les diagrammes UML sont disponibles dans `Docs/UML`. |
| Les diagrammes sont faits avec un outil de diagramme comme code (diagram as code), tel que PlantUML ou Mermaid | x | | Les diagrammes sont créés avec PlantUML. |
| La documentation est écrite en Markdown | x | | Tous les fichiers de documentation sont en Markdown. |
| La documentation suit un gabarit comme Arc42 | x | | La structure de la documentation est inspirée d'Arc42. |
| La documentation est organisée dans un répertoire dédié comme “docs” dans le répertoire du système | x | | La documentation est organisée dans le répertoire `Docs`. |

### 2.6 Conteneurisation et exécution
| Éléments | Oui | Non | Commentaire / Justification |
|----------|-----|-----|-----------------------------|
| L’application est conteneurisée avec un Dockerfile | x | | Le Dockerfile est présent et fonctionnel. |
| Cliente est conteneurisée | x | | Le service client est conteneurisé via Docker Compose. |
| La base de données instanciée manuellement | x | | La base de données peut être instanciée manuellement. |
| La base de données instanciée avec système d’orchestration (ex. Docker compose) | x | | La base de données est instanciée via Docker Compose. |
| Les instructions d’exécution sont présentes dans le README | x | | Les instructions d'exécution sont incluses dans le README.md. |

### 2.7 Intégration continue (CI/CD)
| Éléments | Oui | Non | Commentaire / Justification |
|----------|-----|-----|-----------------------------|
| Une pipeline CI/CD est configurée sur GitHub Actions ou GitLab CI | x | | Une pipeline CI/CD est configurée dans `.github/workflows/ci.yml`. |
| Le lint est fonctionnel | x | | Le lint est exécuté dans la pipeline CI/CD. |
| L’étape test unitaire est fonctionnelle | x | | Les tests unitaires sont exécutés via pytest. |
| L’étape build Docker est fonctionnelle | x | | L'image Docker est construite dans la pipeline. |
| L’image est publiée sur Docker Hub | x | | L'image est publiée sur Docker Hub sous `simontremblay99/magasin-app`. |

## 3. Réflexion personnelle
1. **Limites du style d’architecture client/serveur à 2 couches (2-tier)** :
   - Difficulté à évoluer vers des architectures distribuées.
   - Risque de surcharge du serveur en cas de forte demande.

2. **Limites du mécanisme de base de données utilisée** :
   - SQLite est limité en termes de concurrence et de scalabilité.
   - Tactiques pour améliorer la capacité de réponse :
     - Utilisation de caches.
     - Optimisation des requêtes.
     - Migration vers une base de données plus robuste comme PostgreSQL.

3. **Efforts techniques et risques liés à la migration vers une base NoSQL** :
   - Efforts :
     - Réécriture des requêtes.
     - Adaptation des modèles de données.
   - Risques :
     - Perte de cohérence transactionnelle.
     - Complexité accrue pour les relations complexes.

4. **Éléments posant le plus de difficulté** :
   - Configuration de la pipeline CI/CD.
   - Gestion des secrets dans le dépôt.

5. **Améliorations pour les prochains laboratoires** :
   - Automatisation accrue des tests.
   - Documentation plus détaillée des choix technologiques.