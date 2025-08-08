# ADR 1 – Orchestration centralisée de la Saga

## Contexte
Le processus de commande implique plusieurs services (stock, paiement, expédition) avec des dépendances et des échecs possibles.

## Décision
Mettre en place une saga orchestrée avec un orchestrateur central qui pilote la progression et déclenche les compensations si nécessaire.

## Conséquences
- Visibilité claire du flux métier.
- Gestion déterministe des erreurs.
- Couplage accru avec l’orchestrateur (à limiter via interfaces).
