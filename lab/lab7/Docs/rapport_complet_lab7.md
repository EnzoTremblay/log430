# Rapport complet – Lab 7 : Proposition d’architecture événementielle

## 1. Contexte et objectifs

Je propose l’évolution du système (Lab 5/6) vers une architecture événementielle. L’objectif est de découpler les services, fiabiliser les échanges et permettre une meilleure scalabilité.

## 2. Changements proposés

- Introduction d’un bus d’événements (Kafka/Redpanda) et d’un Schema Registry.
- Passage d’une saga orchestrée (Lab 6) à une saga chorégraphiée par événements.
- Adoption du pattern Outbox dans chaque service pour la publication fiable.
- Idempotence côté consommateurs et mise en place d’une DLQ.
- Versionnement des sujets (topics) et gouvernance des schémas.
- Traces distribuées (OpenTelemetry) pour corréler les événements.
- Ajustement des services existants pour publier/consommer des Domain Events (OrderCreated, PaymentAuthorized, StockReserved, etc.).

## 3. Impacts sur l’existant

- Services Commande, Paiement, Stock deviennent producteurs/consommateurs.
- Les intégrations REST via Gateway restent pour les frontaux; la logique inter-services migre vers événements.
- Les tests d’intégration nécessitent un broker local (docker-compose pour Kafka/Redpanda) et des tests d’idempotence.
- Observabilité enrichie (metrics + traces d’événements).

## 4. Diagrammes (UML 4+1)

### 4.1 Déploiement

Voir `Docs/UML/deployment_evenementiel.puml`.

```plantuml
@startuml deployment_evenementiel
!theme spacelab
node "Cluster Docker" {
  node "Gateway (KrakenD)" {
    component "API Gateway" as APIGW
  }
  node "Services" {
    component "Service Commande" as S_CMD
    component "Service Paiement" as S_PAY
    component "Service Stock" as S_STK
    component "Service Comptes" as S_ACC
  }
  node "Messaging" {
    component "Kafka/Redpanda" as BUS
    component "Schema Registry" as REG
  }
  database "DB Commande" as DB_CMD
  database "DB Paiement" as DB_PAY
  database "DB Stock" as DB_STK
}

S_CMD --> BUS
S_PAY --> BUS
S_STK --> BUS
APIGW --> S_CMD
S_CMD --> DB_CMD
S_PAY --> DB_PAY
S_STK --> DB_STK
@enduml
```

### 4.2 Séquence (commande par événements)

Voir `Docs/UML/sequence_commande_evenements.puml`.

```plantuml
@startuml sequence_commande_evenements
!theme spacelab
actor Client
participant Gateway
participant "Service Commande" as COM
participant "Kafka" as BUS
participant "Service Paiement" as PAY
participant "Service Stock" as STOCK
Client -> Gateway : POST /commande
Gateway -> COM : createOrder()
COM -> BUS : OrderCreated
PAY -> BUS : PaymentAuthorized
BUS -> STOCK : ReserveStock
STOCK -> BUS : StockReserved
BUS -> COM : OrderConfirmed
COM -> Gateway : 201 Created
note over BUS,COM : Les échecs publient PaymentFailed/StockNotReserved
@enduml
```

### 4.3 Classes (Domain Events)

Voir `Docs/UML/classes_domain_events.puml`.

```plantuml
@startuml classes_domain_events
!theme spacelab
class OrderCreated {
  +orderId: UUID
  +customerId: UUID
  +items: List<Item>
  +total: Money
}
class PaymentAuthorized {
  +orderId: UUID
  +paymentId: UUID
}
class PaymentFailed {
  +orderId: UUID
  +reason: String
}
class StockReserved {
  +orderId: UUID
  +reservations: Map<Sku,Qty>
}
class StockNotReserved {
  +orderId: UUID
  +reason: String
}
class OrderConfirmed {
  +orderId: UUID
}
class Item {
  +sku: String
  +qty: int
  +price: Money
}
class Money {
  +amount: decimal
  +currency: String
}

OrderCreated "1" *-- "many" Item
OrderConfirmed ..> OrderCreated
PaymentAuthorized ..> OrderCreated
PaymentFailed ..> OrderCreated
StockReserved ..> OrderCreated
StockNotReserved ..> OrderCreated
@enduml
```

### 4.4 Cas d’utilisation

Voir `Docs/UML/usecase_evenementiel.puml`.

```plantuml
@startuml usecase_evenementiel
!theme spacelab
actor Client
actor Admin
(Client) --> (Passer une commande)
(Client) --> (Payer une commande)
(Client) --> (Consulter le statut)
(Admin) --> (Superviser les événements)
(Admin) --> (Rejouer depuis DLQ)
@enduml
```

## 5. Plan d’adoption

- Étape 1: Ajouter Kafka/Redpanda + Schema Registry via docker-compose.
- Étape 2: Implémenter Outbox dans Service Commande, publier OrderCreated.
- Étape 3: Adapter Paiement et Stock comme consommateurs/producteurs.
- Étape 4: Ajouter idempotence et DLQ; inclure tests d’intégration.
- Étape 5: Activer traces distribuées (OpenTelemetry) et dashboards.

---

Document rédigé avec l’aide de GitHub Copilot.
