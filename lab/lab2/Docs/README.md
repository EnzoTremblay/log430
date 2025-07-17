# README – Laboratoire 2

## Instructions de déploiement

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/EnzoTremblay/log430.git
   ```
2. Se placer dans le dossier du projet :
   ```bash
   cd log430
   ```
3. Lancer les services avec Docker Compose :
   ```bash
   docker-compose up --build
   ```
4. Accéder au tableau de bord d’observabilité (Grafana) :
   - Ouvrir [http://localhost:3000](http://localhost:3000) dans le navigateur.
   - Utiliser les identifiants par défaut (admin/admin).

## Structure du projet
- `app.py` : Application principale
- `test_app.py` : Tests unitaires
- `Dockerfile` et `docker-compose.yml` : Conteneurisation et orchestration
- `Docs/` : Documentation technique (ADR, UML, rapport)
- `lab/` : Dossiers des laboratoires

## Liens utiles
- [Dépôt GitHub principal](https://github.com/EnzoTremblay/log430)
- Dashboards Grafana : [http://localhost:3000](http://localhost:3000)
