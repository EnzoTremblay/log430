# Rapport complet – Laboratoire 6 : Proposition de saga orchestrée et machine d’état

## 1. Contexte et objectifs
Je propose l’introduction d’une saga orchestrée pour le processus de commande (réservation de stock, paiement, expédition) afin d’assurer cohérence et compensations.

## 2. Décisions d’architecture (ADR)
- ADR 1 : Orchestration centralisée – un orchestrateur pilote le flux et déclenche les compensations.
- ADR 2 : Machine d’état – modéliser explicitement états, transitions, gardes et actions.

## 3. Conception (UML 4+1)
- Vue Processus : étapes RESERVE_STOCK → CHARGE_PAYMENT → CREATE_SHIPMENT avec chemins d’échec.
- Vue Implémentation (conceptuelle) : l’orchestrateur encapsule le contrôle; services externes réels restent découplés.

### 3.1 Diagramme d’état

```plantuml
@startuml saga_state_machine
!theme spacelab
[*] --> INIT
INIT --> RESERVE_STOCK : start/reserve_stock
RESERVE_STOCK --> CHARGE_PAYMENT : next [ok]/charge_payment
RESERVE_STOCK --> FAILED : fail [ko]
CHARGE_PAYMENT --> CREATE_SHIPMENT : next [ok]/create_shipment
CHARGE_PAYMENT --> COMPENSATE_STOCK : fail [ko]/compensate_stock
CREATE_SHIPMENT --> COMPLETE : next [ok]
CREATE_SHIPMENT --> REFUND_PAYMENT : fail [ko]/refund_payment
REFUND_PAYMENT --> COMPENSATE_STOCK : finalize_fail/compensate_stock
COMPENSATE_STOCK --> FAILED : finalize
@enduml
```

### 3.2 Diagramme de séquence (succès)

```plantuml
@startuml sequence_success_commande
!theme spacelab
actor Client
participant Orchestrateur
participant Stock
participant Paiement
participant Expédition
Client -> Orchestrateur : passerCommande()
Orchestrateur -> Stock : reserver()
Stock --> Orchestrateur : ok
Orchestrateur -> Paiement : charger()
Paiement --> Orchestrateur : ok
Orchestrateur -> Expédition : creer()
Expédition --> Orchestrateur : ok
Orchestrateur --> Client : confirmation
@enduml
```

## 4. Impacts et plan d’adoption
- Introduire un orchestrateur (service dédié) et définir les interfaces avec Stock/Paiement/Expédition.
- Formaliser la machine d’état (états/transitions), journaliser chaque transition.
- Prévoir des actions de compensation documentées et testables.
- Étapes: (1) définir contrat API, (2) créer orchestrateur minimal, (3) brancher services, (4) tests d’échec/compensation, (5) observabilité.

---

Document narratif de proposition (aucune implémentation logicielle dans ce lab).
