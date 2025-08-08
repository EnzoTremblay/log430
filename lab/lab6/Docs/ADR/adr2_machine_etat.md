# ADR 2 – Machine d’état pour la saga

## Contexte
La saga comporte des états et transitions explicites (réserver stock, charger paiement, créer expédition, compenser, etc.).

## Décision
Utiliser une machine d’état (librairie `transitions`) pour modéliser les états, gardes, et actions.

## Conséquences
- Modèle explicite et testable.
- Chemins d’échec/compensation gérés proprement.
- Dépendance à une librairie tierce.
