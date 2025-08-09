# ADR 2 – Saga chorégraphiée par événements

## Contexte
Les processus longue durée (commande) doivent rester résilients et découplés.

## Décision
Passer d’une saga orchestrée (Lab 6) à une saga chorégraphiée où chaque service réagit aux événements et publie les siens.

## Conséquences
- Moins de couplage à un orchestrateur central
- Complexité de la visibilité de bout en bout (nécessite trace distribuée)
- Gestion des échecs via événements de compensation
