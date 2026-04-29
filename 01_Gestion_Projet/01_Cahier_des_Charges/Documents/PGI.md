# 👥 Plan de gestion des intervenants (pgi)

**Projet :** [nom du projet]  
**Responsable :** [ton nom]  
**Version :** 1.0  
**Date :** 02/04/2026

---

## 1. Cartographie des parties prenantes (stakeholders)
*Analyse de l'intérêt et de l'influence de chaque acteur pour adapter la communication.*

| Intervenant | Rôle / fonction | Intérêt (1-5) | Influence (1-5) | Stratégie |
| :--- | :--- | :---: | :---: | :--- |
| **Le mentor** | Validateur technique | 5 | 5 | **Gérer de près** (validation technique). |
| **Chef de projet** | Pilotage & planning | 4 | 5 | **Satisfaire** (respect des délais). |
| **Expert métier** | Référent données | 5 | 3 | **Informer** (qualité des data). |
| **Utilisateurs** | Bénéficiaires finaux | 3 | 2 | **Surveiller** (adéquation besoin). |

---

## 2. Matrice des responsabilités (raci)
*Définition précise des rôles pour chaque grande étape du projet.*
* **R** (responsible) : réalise la tâche.  
* **A** (accountable) : valide la tâche (un seul par ligne).  
* **C** (consulted) : apporte son expertise.  
* **I** (informed) : reçoit l'information.

| Tâches / jalons | Toi (data architect) | Chef de projet | Mentor | Expert métier |
| :--- | :---: | :---: | :---: | :---: |
| **Cadrage & cahier des charges** | **R** | **C** | **A** | **I** |
| **Accès & ingestion (etl)** | **R** | **I** | **C** | **A** |
| **Modélisation & analyse (eda)** | **R** | **I** | **A** | **C** |
| **Visualisation (dashboard)** | **R** | **A** | **C** | **C** |
| **Livraison & soutenance** | **R** | **C** | **A** | **I** |

---

## 3. Plan de communication
*Organisation des échanges pour garantir la transparence du projet.*

| Type de point | Fréquence | Participants | Support / canal |
| :--- | :--- | :--- | :--- |
| **Comité de suivi (cosu)** | Hebdomadaire | Toi + cdp | Visioconférence (teams/meet) |
| **Revue de sprint** | Toutes les 2 sem. | Toi + mentor | Démo sur github / streamlit |
| **Flash report** | Chaque vendredi | Tous | Email court (fait/à faire/risques) |
| **Urgent / bloquant** | Ad hoc | Selon besoin | Slack / discord / teams |

---

## 4. Gestion des conflits et escalade
* En cas de désaccord technique entre l'expert métier et la faisabilité data, l'arbitrage est rendu par le **mentor**.
* En cas de retard de livraison d'une dépendance externe, l'alerte est remontée au **chef de projet** via le registre des risques.