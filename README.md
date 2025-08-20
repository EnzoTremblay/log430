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

### 1. Exécution locale
```bash
python3 app.py
```

### 2. Tests unitaires
```bash
pip install pytest
pytest
```

### 3. Docker & Docker Compose
```bash
docker build -t log430-app .
docker-compose up
```

## CI/CD
Un pipeline GitHub Actions peut être configuré pour :
- Exécuter les tests
- Construire et publier les images Docker

## Lab 6 – Proposition (sans implémentation)
- Docs: `lab/lab6/Docs/`
- Code et tests retirés (proposition documentaire uniquement)
- Diagrammes PlantUML et ADR inclus

## Licence
Projet sous licence MIT.

## Exécution des labs et Docker Compose

### Docker Compose (Labs 2, 3, 5 + gateway)
- Fichier: `docker-compose.labs.yml`
- Démarrer:
  - docker compose -f docker-compose.labs.yml up --build
- Services exposés:
  - Lab 2 API: http://localhost:5202
  - Lab 3 API: http://localhost:5203
  - Lab 5 services: produits:5001, ventes:5002, stock:5003, clients:5004, panier:5005, commande:5006
  - API Gateway KrakenD: http://localhost:8080

### Par labo
- Lab 1: documentation uniquement (voir `lab/lab1`)
- Lab 2: API Flask (mémoire)
  - Local: python lab/lab2/src/api.py
  - Docker: http://localhost:5202
  - Endpoints: /api/v1/stores/<id>/stock, /api/v1/report, /api/v1/products/<id> [PUT], /api/v1/dashboard
- Lab 3: API Flask (adapte `app.py`)
  - Local: python lab/lab3/api.py
  - Docker: http://localhost:5203
  - Endpoints identiques à Lab 2
- Lab 4: démonstration de cache
  - Tests: .\run_tests.ps1 (section Lab 4)
- Lab 5: microservices + API Gateway
  - Docker Compose (voir ci-dessus) puis appels via http://localhost:8080 selon `lab/lab5/gateway/krakend.json`
- Lab 6: orchestrateur de saga (code minimal + docs)
  - Tests: & "C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Python37_64\\python.exe" -m unittest -v lab.lab6.tests.test_saga

### Lancer tous les tests
- PowerShell: .\run_tests.ps1
