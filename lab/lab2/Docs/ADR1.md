# ADR 1 : Architecture multi-magasins

## Contexte
L’entreprise doit gérer plusieurs magasins, un centre logistique et une maison mère. La solution doit permettre la synchronisation des stocks et des transactions entre tous les points.

## Décision
Adoption d’une architecture orientée services (SOA) avec une base centrale et des modules pour chaque magasin, le centre logistique et la maison mère. Chaque module communique via des API REST.

## Conséquences
- Scalabilité accrue pour ajouter de nouveaux magasins.
- Synchronisation facilitée des données.
- Possibilité d’évolution vers une interface web ou mobile.
