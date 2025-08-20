# ADR 2 – Machine d’état explicite pour la saga

## TITRE

Machine d’état explicite pour la saga

## CONTEXT

La saga suit un enchaînement d’états (INIT → RESERVE_STOCK → CHARGE_PAYMENT → CREATE_SHIPMENT → DONE) ponctué de conditions et d’échecs potentiels, nécessitant des transitions de compensation (ex.: release stock, refund). Un modèle implicite rend le comportement difficile à auditer et à tester.

## DECISION

Modéliser la saga à l’aide d’une machine d’état explicite (états, événements, gardes, actions). Les transitions sont persistées et journalisées. Le modèle d’état devient artefact contractuel et sert d’entrée aux tests automatisés. Les compensations sont des transitions dédiées et auditées.

## CONSEQUENCES

Avantages

- Comportement explicite, traçable et testable.
- Chemins d’échec/compensation gérés de façon systématique.
- Support naturel pour la reprise après incident (re-hydratation d’état).

Inconvénients / risques

- Courbe d’apprentissage et surcoût de modélisation.
- Risque de divergence entre modèle et implémentation si la gouvernance est faible.

## COMPLIANCE

- Diagrammes d’état et séquence versionnés (voir UML).
- Tests unitaires et scénarios d’intégration couvrant transitions heureuses et d’échec.
- Règles de nommage et de version des états/événements.
- Observabilité: logs structurés par transition et corrélation par ID de saga.
