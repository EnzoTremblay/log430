# Rapport complet – Laboratoire 6 : Proposition de saga orchestrée et machine d’état

## 1. Contexte et objectifs
Je propose l’introduction d’une saga orchestrée pour le processus de commande (réservation de stock, paiement, expédition) afin d’assurer cohérence et compensations.

## 2. Décisions d’architecture (ADR)
- ADR 1 : Orchestration centralisée – un orchestrateur pilote le flux et déclenche les compensations.
- ADR 2 : Machine d’état – modéliser explicitement états, transitions, gardes et actions.

## 3. Conception (UML 4+1)
- Vue Processus : étapes RESERVE_STOCK → CHARGE_PAYMENT → CREATE_SHIPMENT avec chemins d’échec.
- Vue Implémentation (conceptuelle) : l’orchestrateur encapsule le contrôle; services externes réels restent découplés.

### 3.1 Déploiement
Voir `Docs/UML/deployment_orchestrateur.puml`.

![Déploiement orchestrateur](UML/deployment_orchestrateur.png)

```plantuml
@startuml deployment_orchestrateur
!theme spacelab
node "Cluster Docker" {
  node "API Gateway (KrakenD)" {
    component "Gateway" as GW
  }
  node "Orchestrateur" {
    component "Order Orchestrator" as ORCH
    database "Saga Store" as SAGA_DB
  }
  node "Services" {
    component "Stock Service" as STK
    component "Payment Service" as PAY
    component "Shipping Service" as SHIP
  }
  database "DB Stock" as DB_STK
  database "DB Payment" as DB_PAY
  database "DB Shipping" as DB_SHIP
}
GW --> ORCH
ORCH --> STK
ORCH --> PAY
ORCH --> SHIP
STK --> DB_STK
PAY --> DB_PAY
SHIP --> DB_SHIP
ORCH --> SAGA_DB
@enduml
```

### 3.2 Séquence
Voir `Docs/UML/sequence_saga_orchestrateur.puml`.

![Séquence orchestrateur](UML/sequence_saga_orchestrateur.png)

```plantuml
@startuml sequence_saga_orchestrateur
!theme spacelab
actor Client
participant Gateway as GW
participant Orchestrateur as ORCH
participant "Stock Service" as STK
participant "Payment Service" as PAY
participant "Shipping Service" as SHIP

Client -> GW : POST /commande
GW -> ORCH : startOrder()
ORCH -> STK : reserver()
STK --> ORCH : ok
ORCH -> PAY : charger()
alt paiement ok
  PAY --> ORCH : ok
  ORCH -> SHIP : creer()
  SHIP --> ORCH : ok
  ORCH --> GW : 201 Created
else paiement échec
  PAY --> ORCH : fail(reason)
  ORCH -> STK : compenserReservation()
  ORCH --> GW : 409 Conflict
end
@enduml
```

### 3.3 Classes
Voir `Docs/UML/classes_saga_orchestrateur.puml`.

![Classes orchestrateur](UML/classes_saga_orchestrateur.png)

```plantuml
@startuml classes_saga_orchestrateur
!theme spacelab
class OrderOrchestrator {
  +startOrder(cmd: CreateOrder)
  +onStockReserved()
  +onPaymentCharged()
  +onShipmentCreated()
  -compensateStock()
  -refundPayment()
  -state: SagaState
}
class SagaState {
  +current: State
  +transition(evt: Event)
}
class StockClient {
  +reserver(items)
  +compenserReservation()
}
class PaymentClient {
  +charger(total)
  +rembourser(paymentId)
}
class ShippingClient {
  +creer(expedition)
}

OrderOrchestrator --> SagaState
OrderOrchestrator ..> StockClient
OrderOrchestrator ..> PaymentClient
OrderOrchestrator ..> ShippingClient
@enduml
```

### 3.4 Cas d’utilisation
Voir `Docs/UML/usecase_orchestrateur.puml`.

![Cas d’utilisation orchestrateur](UML/usecase_orchestrateur.png)

```plantuml
@startuml usecase_orchestrateur
!theme spacelab
actor Client
actor Admin
(Client) --> (Passer une commande)
(Client) --> (Payer une commande)
(Client) --> (Suivre le statut de commande)
(Admin) --> (Superviser l'orchestrateur)
(Admin) --> (Rejouer une compensation)
@enduml
```

## 4. Impacts et plan d’adoption
- Introduire un orchestrateur (service dédié) et définir les interfaces avec Stock/Paiement/Expédition.
- Formaliser la machine d’état (états/transitions), journaliser chaque transition.
- Prévoir des actions de compensation documentées et testables.
- Étapes: (1) définir contrat API, (2) créer orchestrateur minimal, (3) brancher services, (4) tests d’échec/compensation, (5) observabilité.

---

Document narratif de proposition (aucune implémentation logicielle dans ce lab).
