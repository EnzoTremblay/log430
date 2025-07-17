
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

## Licence
Projet sous licence MIT.
