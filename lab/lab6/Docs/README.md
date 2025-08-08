# Lab 6 – Implémentation d’une Saga Orchestrée et Gestion de la Machine d’État

## Objectifs
- Implémenter une saga orchestrée pour le processus de commande.
- Gérer les transitions via une machine d’état (bibliothèque `transitions`).
- Couvrir les chemins de succès et d’échec avec compensation.
- Fournir les tests automatisés et la documentation (ADR, UML, rapport).

## Structure
- `src/saga/orchestrator.py` : Orchestrateur de la saga.
- `tests/test_orchestrator.py` : Tests unitaires pytest.
- `Docs/ADR/` : Décisions d’architecture.
- `Docs/UML/` : Diagrammes UML (état, séquence).
- `Docs/rapport_complet_lab6.md` : Rapport narratif complet.

## Exécution locale
1. Créer l’environnement et installer les dépendances:
   - Windows PowerShell:
     - python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r lab/lab6/requirements.txt
2. Lancer les tests:
   - pytest lab/lab6/tests -q

## Livrables
- Code de la saga et tests passants.
- Diagrammes UML de l’état et de séquence de la saga.
- ADRs justifiant les choix.
- Rapport narratif.
