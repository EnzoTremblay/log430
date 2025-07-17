# ADR 2 : Synchronisation et cohérence des données

## Contexte
La cohérence des stocks et des transactions entre magasins et maison mère est critique.

## Décision
Utilisation d’un système de synchronisation basé sur des événements (Event Sourcing) pour garantir la cohérence et la traçabilité des opérations. Les mises à jour sont propagées via des messages asynchrones.

## Conséquences
- Fiabilité accrue de la synchronisation.
- Historique complet des opérations.
- Facilité d’intégration de nouveaux modules (magasins, logistique).
