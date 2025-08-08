# UML – Lab 6

## Fichiers
- `saga_state_machine.puml` – Diagramme d’état de la saga
- `sequence_success_commande.puml` – Diagramme de séquence (succès)

## Générer les images PNG
- Via Docker (recommandé):
  - docker run --rm -v ${PWD}:/workspace -w /workspace plantuml/plantuml -tpng lab/lab6/Docs/UML/*.puml
- Via PlantUML local:
  - plantuml -tpng lab/lab6/Docs/UML/*.puml

Les PNG seront générés dans le même dossier.
