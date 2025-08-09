# Lab 7 – Proposition d’architecture événementielle

Ce dossier propose les changements pour passer à une architecture événementielle (Lab 7), sans implémentation complète du code.

- Docs: `Docs/` (rapport, ADR, UML)
- Objectif: décrire les événements, topics, producteurs/consommateurs, patterns (Outbox, idempotence, DLQ) et l’impact sur l’existant.
- Diagrammes: déploiement, séquence, classes (domain events), cas d’utilisation.

Rendu des diagrammes PlantUML (via Docker):
- docker run --rm -v ${PWD}:/workspace -w /workspace plantuml/plantuml -tpng lab/lab7/Docs/UML/*.puml
