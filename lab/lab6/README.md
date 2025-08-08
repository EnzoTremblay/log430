# Lab 6 – Saga orchestrée et machine d’état

Voir `Docs/README.md` pour les objectifs et l’exécution.

## Structure
- `src/` Code de la saga orchestrée (machine d’état)
- `tests/` Tests unitaires (pytest)
- `Docs/` ADR, UML, rapport
- `suivi.md` Journal de suivi

## Exécution (PowerShell)
- python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r lab/lab6/requirements.txt
- pytest lab/lab6/tests -q

## Génération des diagrammes UML
- Option Docker (sans installation Java/PlantUML) depuis la racine du repo:
  - docker run --rm -v ${PWD}:/workspace plantuml/plantuml -tpng lab/lab6/Docs/UML/*.puml
