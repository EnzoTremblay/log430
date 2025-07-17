# README – Laboratoire 5

## Instructions d’exécution

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/EnzoTremblay/log430.git
   ```
2. Se placer dans le dossier du projet :
   ```bash
   cd log430
   ```
3. Lancer les microservices et l’API Gateway avec Docker Compose :
   ```bash
   docker-compose up --build
   ```
4. Lancer les scripts de test de charge (exemple avec k6) :
   ```bash
   k6 run test_charge.js
   ```
5. Accéder au dashboard Grafana :
   - Ouvrir [http://localhost:3000](http://localhost:3000)

## Structure du projet
- `services/` : Microservices (produits, ventes, stock, clients, panier, commande)
- `gateway/` : API Gateway (Kong/KrakenD)
- `test_charge.js` : Script de test de charge (k6)
- `Docs/` : Documentation technique, suivi, rapport
- `lab/` : Dossiers des laboratoires

## Liens utiles
- [Dépôt GitHub principal](https://github.com/EnzoTremblay/log430)
- Grafana : [http://localhost:3000](http://localhost:3000)
