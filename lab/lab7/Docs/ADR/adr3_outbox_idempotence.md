# ADR 3 – Outbox, Idempotence, DLQ

## Contexte
Garantir la fiabilité et l’exactement-une-fois est difficile dans un système distribué.

## Décision
Adopter le pattern Outbox pour publier les événements transactionnellement, utiliser des clés idempotentes et une Dead Letter Queue (DLQ).

## Conséquences
- Publication fiable
- Rejeu contrôlé
- Opérations supplémentaires (nettoyage outbox/DLQ)
