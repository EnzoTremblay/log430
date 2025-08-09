# Lab 7 – Proposition d’architecture événementielle

Contenu:
- `rapport_complet_lab7.md` – Rapport narratif décrivant tous les changements proposés.
- `ADR/` – Décisions d’architecture (bus d’événements, chorégraphie, schémas).
- `UML/` – Diagrammes PlantUML (déploiement, séquence, classes, cas d’utilisation).

Générer les PNG:
- docker run --rm -v ${PWD}:/workspace -w /workspace plantuml/plantuml -tpng lab/lab7/Docs/UML/*.puml
