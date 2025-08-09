# Auto-évaluation – Lab 7

Cette auto-évaluation suit les attentes du document de référence du Lab 7. Je n’ai pas livré d’implémentation exécutable, mais une proposition détaillée d’architecture événementielle.

## 1) Exigences et portée
- [x] Proposition d’architecture événementielle (bus, topics, producteurs/consommateurs)
- [x] Modélisation des Domain Events (OrderCreated, PaymentAuthorized, StockReserved, etc.)
- [x] Gestion des erreurs: DLQ, idempotence, rejouabilité
- [ ] Implémentation opérationnelle des services et du broker (non livrée dans ce lab)

## 2) Architecture et décisions
- [x] ADR: choix du bus (Kafka/Redpanda), saga chorégraphiée, outbox/idempotence
- [x] Gouvernance des schémas (Schema Registry) proposée

## 3) Diagrammes UML
- [x] Déploiement (services + broker + registry)
- [x] Séquence (commande par événements)
- [x] Classes (Domain Events)
- [x] Cas d’utilisation

## 4) Documentation
- [x] Rapport narratif complet
- [x] README (instructions de génération des PNG)

## 5) Code et tests
- [ ] Implémentation des producteurs/consommateurs et tests d’intégration

## 6) Démonstration
- [ ] Exécution locale avec docker-compose (broker/services) – non applicable ici

## Synthèse
Je n’ai pas été en mesure de compléter l’implémentation du code dans le cadre du Lab 7. En revanche, j’ai livré:
- une proposition exhaustive avec ADRs,
- des diagrammes UML (déploiement, séquence, classes, cas d’utilisation),
- un rapport narratif et un plan d’adoption.

Ces éléments structurent clairement l’implémentation à venir et réduisent les risques.
