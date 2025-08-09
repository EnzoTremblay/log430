# Auto-évaluation – Lab 6

Cette auto-évaluation est remplie en fonction des attentes du document de référence du Lab 6. Comme demandé, je n’ai pas livré de code fonctionnel pour ce lab, mais une proposition complète des changements architecturaux (orchestration + machine d’état) avec la documentation et les diagrammes.

## 1) Exigences et portée
- [x] Proposition de solution pour gérer le processus de commande multi-étapes (réservation stock, paiement, expédition)
- [x] Gestion des échecs et compensations décrites
- [ ] Implémentation opérationnelle du flux de bout en bout (non livrée dans ce lab)

Commentaire: la portée se limite à une proposition détaillée et structurée, sans code.

## 2) Architecture et décisions
- [x] Saga orchestrée proposée (orchestrateur central, responsabilités, interfaces)
- [x] Machine d’état formalisée (états, transitions, gardes, actions)
- [x] ADR fournis et justifiés (orchestration, machine d’état)

Commentaire: les décisions clés sont argumentées et reliées aux risques/contraintes.

## 3) Diagrammes UML (modèle 4+1 ciblé)
- [x] Déploiement (orchestrateur + services + persistance de saga)
- [x] Séquence (scénario de succès + embranchements d’échec)
- [x] Classes (orchestrateur, clients de services, état)
- [x] Cas d’utilisation (vue utilisateur/admin)

Commentaire: les diagrams .puml sont fournis; les PNG peuvent être générés avec le script `Docs/UML/render_uml.ps1`.

## 4) Documentation
- [x] Rapport narratif complet (proposition) mis à jour
- [x] README/consignes (explication des livrables et génération des PNG)

Commentaire: la documentation rend explicites les impacts et le plan d’adoption.

## 5) Code et tests
- [ ] Implémentation de l’orchestrateur et intégration avec services
- [ ] Tests unitaires/integration (non applicables ici)

Commentaire: non livré par choix pédagogique pour se concentrer sur la proposition.

## 6) Démonstration et exécution
- [ ] Exécution locale/tests passants
- [ ] Observabilité (non applicable au stade proposition)

Commentaire: non applicable sans implémentation.

## Synthèse
Je n’ai pas été en mesure de compléter l’implémentation du code dans le cadre du Lab 6. En revanche, j’ai livré une proposition détaillée d’architecture avec:
- ADRs: orchestration centrale, machine d’état
- Diagrammes UML: déploiement, séquence, classes, cas d’utilisation
- Rapport narratif structuré et plan d’adoption

Ces livrables permettent de guider une implémentation ultérieure en réduisant les risques techniques.
