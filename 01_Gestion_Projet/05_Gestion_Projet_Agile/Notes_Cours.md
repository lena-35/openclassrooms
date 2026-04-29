# 📓 Notes : Maîtriser la Gouvernance et le Cycle de Vie d'un Projet

> **Cours :** Gemini

> **Début du cours :** 15/04/2026

> **Fin du cours :** 28/04/2026

---

## 🧭 Partie 1 :  Gouvernance et Cycle de Vie d'un Projet
*La réussite du projet repose sur un flux logique de transformation d'un besoin en produit, soutenu par une gestion rigoureuse de la qualité documentaire. Cette approche garantit la traçabilité et l'alignement des équipes à travers les axes suivants :*

- ***Hiérarchie et Responsabilités** : Identifier précisément quel acteur est responsable de la rédaction de chaque document.*
- ***Rituels et Flux Documentaires** : Maîtriser le cycle de vie des réunions et les livrables associés pour chaque phase du projet.*
- ***Agilité des Spécifications** : Gérer le cycle de vie des spécifications techniques et de tests dans un flux itératif.*
- ***Traçabilité des Révisions (Global)** : Maintenir un historique des étapes clés et des évolutions majeures impactant le produit global.*
- ***Maîtrise du Détail (Interne)** : Documenter chaque modification technique au sein des documents spécifiques pour une transparence totale.*

	![Modèle de developpement projet](images/Gouvernance_CycleVie_Projet.jfif)
	
	![Modèle de developpement projet](images/Gouvernance_CycleVie_Projet.png)


### 1.1 Hiérarchie des Documents et Responsabilités

| Document | Phase | Rédacteur | Format Type | Emplacement exact | Contenu Clé |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Contrat / Devis** | Stratégie | **CTO** | **PDF Scellé** | Fichiers / SharePoint | Engagement légal et financier. |
| **Cahier des Charges** | Cadrage | **PO** | **Wiki (Markdown)** | Azure DevOps Wiki | Vision, Besoins et User Stories. |
| **Dossier d'Architecture** | Conception Macro | **Architecte logiciel** | **Wiki (Markdown)** | Azure DevOps Wiki | Schémas, flux et choix technos. |
| **Specs Techniques** | Conception Micro | **Lead Dev** | **Wiki (Markdown)** | Azure DevOps Wiki | Pseudocode et détails d'implémentation. |
| **Plan de Test / Gherkin** | Préparation QA | **QA** | **Test Plan** | Azure Test Plans | Scénarios de tests et critères d'acceptation. |
| **Code Source** | Réalisation | **Développeur** | **Code / Git** | Azure Repos | Code informatique et branches. |
| **Tickets de Bugs** | Validation | **QA** | **Work Items** | Azure Boards | Anomalies détectées à corriger. |
| **Rapport de Test** | Validation | **QA** | **Wiki (Markdown)** | Azure DevOps Wiki | Bilan de santé de la version et statut "Go/No-Go". |

<br>

### 1.2 Cadre Opérationnel : Responsabilités, Rituels et Traçabilité

| Réunion | Moment | Participants | Document d'entrée | Document de sortie |
| :--- | :--- | :--- | :--- | :--- |
| **Kick-off** | Début du projet | Client, CTO, PO | Demande client | **Contrat / Devis (CTO)** |
| **Ateliers** | Phase de cadrage | Client, PO, Architecte | Vision client | **CdCF (PO)** + **Architecture (Arch)** |
| **Refinement** | Avant le Sprint | PO, Arch, Lead Dev, QA | User Story | **Specs Tech (Lead Dev)** + **Plan de Test (QA)** |
| **Sprint Planning** | Début de cycle | PO, Lead Dev, Team Dev | Specs Tech | **Backlog de Sprint (Tâches)** |
| **Daily Meeting** | Chaque matin | Lead Dev, Team Dev, QA | Tâches en cours | **Code Source (Dev)** |
| **Sprint Demo / QA** | Fin de cycle | Client, PO, QA | Code Source | **Rapport de Test (QA)** + Validation PO |

<br>

### 1.3 Cycle de Vie des Spécifications (Flux Agile)

| Étape | État du Document de Specs | Horizon de temps | Rôle du QA |
| :--- | :--- | :--- | :--- |
| **Lancement (Sprint 0)** | Squelette + Socle technique | Prêt pour les Sprints 1 & 2 | Définition de la stratégie de test globale. |
| **En cours de projet** | Incrémental (mise à jour continue) | Toujours +2 Sprints d'avance | Rédaction des scénarios Gherkin en avance de phase. |
| **Fin de V1** | Complet et Finalisé | Correspond au produit livré | Validation finale (Recette) et rapport de conformité. |

<br>

### 1.4 Changelog Global - Historique des révisions des documents du projet
*Note: On n'y note que les étapes clés (les "Milestones"). Si la somme des modifications internes aboutit à une nouvelle version du produit (ex: passer de la v1.0 à la v1.1), alors on met à jour le Global.*

| Date | Version | Responsable | Évolution Majeure | Impact Produit |
| :--- | :--- | :--- | :--- | :--- |
| 15/04/26 | **v1.2** | **QA** | Validation campagne de non-régression | **Go-Live** : Produit certifié sans régressions. |
| 10/04/26 | **v1.1** | PO | Intégration JIRA | Permet le tracking externe des tickets. |
| 05/04/26 | **v1.0** | Lead Dev | Sortie du MVP | Première version stable utilisable par les Ops. |

<br>

### 1.5 Changelog interne - Historique des révisions d'un document spécifique
*Note: On y note tout. Une correction de virgule, un changement de nom de variable, l'ajout d'un paragraphe technique. C'est la cuisine interne.*

| Date | Rédacteur | Objet de la modification | Section impactée | Justification |
| :--- | :--- | :--- | :--- | :--- |
| 15/04/26 | **QA** | Correction des critères d'acceptation | *§ 5.1 - Authentification* | Échec des tests sur les mots de passe vides. |
| 10/04/26 | **PO** | Ajout du connecteur API JIRA | *§ 4.2 - Connecteurs* | Demande urgente client (Tickets tiers). |
| 08/04/26 | **Lead Dev** | Update du schéma JSON (Task) | *§ 2.1 - Modèles* | Ajout du champ `external_id` (UUID). |
| 05/04/26 | **Lead Dev** | Correction endpoint `/auth` | *§ 3.4 - Sécurité* | Le port 8080 était erroné dans la spec. |

<br>

---

## 💡 Mes Réflexions "Data Architect"
- Centralisation et "Docs as Code" : L'utilisation systématique du Wiki Azure DevOps (Markdown) permet de traiter la documentation technique avec la même rigueur que le code source. Cela facilite le versionnement, la recherche globale et garantit que la donnée technique reste accessible sans sortir de l'écosystème de développement.
- Traçabilité et Intégrité du Flux : La clé d'une gouvernance réussie réside dans la corrélation stricte entre les Work Items (Azure Boards) et les Commits (Azure Repos). Pour un Data Architect, cette liaison assure qu'aucune modification structurelle du code n'est orpheline d'une spécification ou d'un besoin métier validé.

## ❓ Points à approfondir / Questions
- [ ] Automatisation du Changelog : Existe-t-il des extensions ou des scripts permettant de générer automatiquement le Changelog Interne en agrégeant les messages de commits liés aux User Stories via des Pull Requests ?
- [ ] Synchronisation Architecture/Specs : Quel mécanisme de revue mettre en place pour s'assurer que le Dossier d'Architecture (vision macro) est systématiquement aligné lorsque le Lead Dev modifie une Spec Technique (vision micro) durant un sprint ?
- [ ] Gouvernance des fichiers PDF : Comment assurer le lien de versioning entre les documents "scellés" (SharePoint) et l'évolution rapide des besoins documentés sur le Wiki ?  