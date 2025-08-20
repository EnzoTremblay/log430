# ADR 1 – Orchestration centralisée de la saga de commande

## TITRE

Orchestration centralisée de la saga de commande

## CONTEXT

Le processus « commande » traverse plusieurs services (Stock, Paiement, Expédition) qui peuvent échouer de façon indépendante. Nous devons garantir la cohérence de bout en bout, déclencher des compensations en cas d’échec partiel, rendre le flux observable (traces, métriques), et limiter le couplage direct entre services. L’absence d’un contrôle explicite complique le raisonnement sur les échecs et la conformité.

## DECISION

Introduire un service d’orchestration dédié qui pilote la progression de la saga (réserver stock → charger paiement → créer expédition), évalue les conditions de réussite/échec et déclenche les actions de compensation documentées. L’orchestrateur persiste l’état d’avancement et journalise chaque transition. Les interactions avec les services métiers passent par des interfaces claires (API/contrats), afin de conserver un couplage faible et la possibilité de tests isolés.

## CONSEQUENCES

Avantages

- Visibilité centralisée du flux métier et des transitions.
- Gestion déterministe des erreurs et des compensations.
- Point unique pour appliquer règles de conformité et observabilité.

Inconvénients / risques

- Point de dépendance supplémentaire (disponibilité/HA requises).
- Risque de couplage à l’orchestrateur s’il n’y a pas de contrats explicites.
- Complexité de persistance d’état et de reprise sur incident.

## COMPLIANCE

- Contrats d’API versionnés entre Orchestrateur et services (Stock/Paiement/Expédition).
- Modèle d’état et scénarios de compensation formalisés et conservés sous contrôle de version (voir UML).
- Tests automatisés couvrant les chemins heureux et d’échec/compensation.
- Journalisation structurée des transitions + métriques (taux de succès, temps de compensation).
- Revue d’architecture obligatoire pour tout changement impactant le flux.
