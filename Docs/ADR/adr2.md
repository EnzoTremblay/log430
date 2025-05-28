# ADR 2: Stratégie de persistance

## Contexte
Le système nécessite une base de données fiable pour gérer les transactions et la cohérence des données.

## Décision
Nous avons choisi PostgreSQL comme base de données relationnelle et SQLAlchemy comme ORM pour abstraire la couche de persistance.

## Conséquences
- Gestion robuste des transactions.
- Cohérence des données garantie.
- Flexibilité pour évoluer vers des architectures plus complexes.
