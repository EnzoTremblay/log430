# ADR 1 – Choix d’un bus d’événements (Kafka/Redpanda)

## Contexte
Le système doit réagir aux changements (commandes, paiements, stocks) sans couplage fort entre services.

## Décision
Introduire un bus d’événements compatible Kafka (Kafka/Redpanda) pour transporter des Domain Events. Utiliser des topics versionnés par contexte.

## Conséquences
- Découplage producteurs/consommateurs
- Scalabilité par partitionnement
- Besoin d’observabilité et gouvernance des schémas (Schema Registry)
