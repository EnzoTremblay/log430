# Lab 6 – Proposition (sans implémentation)

## Objectifs
- Proposer une solution de saga orchestrée et machine d’état, sans code.
- Décrire les décisions d’architecture, les diagrammes et l’impact.

## Contenu
- `ADR/` décisions d’architecture (orchestration, machine d’état)
- `UML/` diagrammes (état, séquence)
- `rapport_complet_lab6.md` rapport narratif

## Remarques
- Le code source et les tests ont été retirés à la demande pour une proposition documentaire uniquement.

## Générer les PNG UML
- docker run --rm -v ${PWD}:/workspace -w /workspace plantuml/plantuml -tpng lab/lab6/Docs/UML/*.puml
