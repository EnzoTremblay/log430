# Projet LOG430 – Architecture Logicielle

## Description
Ce dépôt regroupe tous les laboratoires du cours LOG430, chacun avec son code, sa documentation, ses rapports, ses suivis et ses fiches d’auto-évaluation. Le projet illustre la progression vers une architecture microservices, l’intégration d’API RESTful, la gestion du cache, le load balancing, l’observabilité, et l’orchestration via API Gateway.

## Structure du Projet
```
log430/
├── app.py                  # Application principale
├── test_app.py             # Tests unitaires globaux
├── Dockerfile              # Conteneurisation de l’app principale
├── docker-compose.yml      # Orchestration multi-services
├── README.md               # Présent document
├── pdf_txt/                # Exigences et auto-évaluations (.txt)
├── lab/
│   ├── lab0/ … lab7/       # Dossiers de chaque laboratoire
│   │   ├── Docs/           # Documentation, ADR, UML, rapports
│   │   ├── suivi.md        # Journal de suivi des changements
│   │   ├── rapport.md      # Rapport du labo
│   │   ├── README.md       # Instructions spécifiques au labo
│   │   └── [code, tests]   # Implémentations et tests
│   └── …
└── .github/workflows/ci.yml # Pipeline CI/CD (si applicable)
```

## Livrables et Remise
- Chaque labo contient :
  - Code source et tests
  - Documentation (README, rapport, ADR, UML)
  - Fiche d’auto-évaluation (.txt)
  - Journal de suivi (suivi.md)
- Tous les fichiers .txt sont conservés pour la correction.
- Les tags Git marquent chaque étape/labo pour la traçabilité.

### Pour la remise :
1. Zippez le dossier `lab/` et le dossier `pdf_txt/`.
2. Fournissez le lien GitHub du dépôt.
3. Vérifiez que tous les fichiers sont bien poussés et versionnés.

## Installation et Utilisation

### 1) Exécution locale des labs (Windows PowerShell)
- Démarrer les services principaux (Lab 2, Lab 3, Lab 5):
  - PowerShell: `./start_labs.ps1`
- Arrêter et libérer les ports: 
  - PowerShell: `./stop_labs.ps1`

Notes:
- Lab 3 utilise `PYTHONPATH` pour les imports lorsque lancé directement; le script s’en occupe.
- Tous les services Flask tournent en mode dev pour démonstration.

### 2) Tests unitaires
- Lancer tous les tests (Labs 2 → 6):
  - PowerShell: `./run_tests.ps1`

### 3) Tests de fumée (HTTP) sur les services démarrés
- Après `start_labs.ps1`, valider les endpoints:
  - PowerShell: `./smoke_tests.ps1`

### 4) Docker & Docker Compose (optionnel)
- Stack prête pour Labs 2, 3, 5 + gateway KrakenD.
- Démarrer:
  - PowerShell: `docker compose -f docker-compose.labs.yml up --build`
- Services exposés:
  - Lab 2 API: http://localhost:5202
  - Lab 3 API: http://localhost:5203
  - Lab 5 services: produits:5001, ventes:5002, stock:5003, clients:5004, panier:5005, commande:5006
  - API Gateway KrakenD: http://localhost:8080

## CI/CD
Un pipeline GitHub Actions peut être configuré pour :
- Exécuter les tests
- Construire et publier les images Docker

## Lab 6 – Proposition (avec code minimal)
- Docs: `lab/lab6/Docs/`
- Code minimal d’orchestration de saga + tests unitaires: `lab/lab6/src/`, `lab/lab6/tests/`
- Diagrammes PlantUML et ADR inclus

## Licence
Projet sous licence MIT.

## Exécution des labs et Docker Compose

### Docker Compose (Labs 2, 3, 5 + gateway)
- Fichier: `docker-compose.labs.yml`
- Démarrer:
  - PowerShell: `docker compose -f docker-compose.labs.yml up --build`
- Services exposés:
  - Lab 2 API: http://localhost:5202
  - Lab 3 API: http://localhost:5203
  - Lab 5 services: produits:5001, ventes:5002, stock:5003, clients:5004, panier:5005, commande:5006
  - API Gateway KrakenD: http://localhost:8080

### Par labo
- Lab 1: documentation uniquement (voir `lab/lab1`)
- Lab 2: API Flask (mémoire)
  - Local: `python lab/lab2/src/api.py` ou `./start_labs.ps1`
  - Docker: http://localhost:5202
  - Endpoints: /api/v1/stores/<id>/stock, /api/v1/report, /api/v1/products/<id> [PUT], /api/v1/dashboard
- Lab 3: API Flask (adapte `app.py`)
  - Local: `python lab/lab3/api.py` (nécessite PYTHONPATH) ou `./start_labs.ps1`
  - Docker: http://localhost:5203
  - Endpoints identiques à Lab 2
- Lab 4: démonstration de cache
  - Tests: .\run_tests.ps1 (section Lab 4)
- Lab 5: microservices + API Gateway
  - Docker Compose (voir ci-dessus) puis appels via http://localhost:8080 selon `lab/lab5/gateway/krakend.json`
- Lab 6: orchestrateur de saga (code minimal + docs)
  - Tests: `./run_tests.ps1` (section Lab 6)

### Postman
- Collection et environnement fournis:
  - `tools/postman/Log430.postman_collection.json`
  - `tools/postman/Log430.postman_environment.json`
- Importer dans Postman et sélectionner l’environnement « LOG430 Local ».
