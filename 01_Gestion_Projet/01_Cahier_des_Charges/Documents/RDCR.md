# 📑 Registre des dépendances, contraintes et risques

Documents complémentaires pour la planification des sprints.

---

**Projet :** Modernisation du système d'analyse des ventes et démographie

**Version :** 1.0 (Méthodologie Agile : document vivant)

**Cible :** Équipe technique, Product Owner, Comité de suivi

**Statut :** Actif

**Référent :** Architecte Logiciel

**Date : ** xx/xx/xxxx

---

## 1. Registre des dépendances
*Éléments indispensables à la progression du projet.*

| ID | Tâche antécédente | Tâche bloquée | Responsable | Échéance | Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DEP-01** | Accès aux bases sources | Phase d'ingestion (ETL) | DSI Client | Semaine 2 | **Arrêt total** |
| **DEP-02** | Validation du CDCF | Début développements | Product Owner | [Date] | **Report global** |
| **DEP-04** | Configuration Cloud | Déploiement / Prod | Admin Sys | Semaine 3 | **Livraison impossible** |

## 2. Registre des contraintes
*Limites non négociables impactant les choix techniques.*

| ID | Nature | Tâche impactée | Justification | Impact |
| :--- | :--- | :--- | :--- | :--- |
| **CON-01** | Techno : ASP.NET/Angular | Développement | Standard IT client | Architecture imposée |
| **CON-02** | Conformité RGPD | Traitement données | Règlement légal | Anonymisation requise |
| **CON-04** | Délai : 324 heures | Sprint planning | Budget académique | Priorisation MoSCoW |

## 3. Analyse des risques (AMDEC)
*Criticité (C) = Gravité (G) x Probabilité (P) sur 5.*

| ID | Risque identifié | G | P | C | Plan de mitigation (action) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RSQ-01** | Incompatibilité code | 5 | 3 | **15** | Audit approfondi au Sprint 0 |
| **RSQ-02** | Retard validation client | 3 | 4 | **12** | Relances J-2 et J-1 par email |
| **RSQ-04** | Perte de code source | 5 | 1 | **5** | Push quotidien sur GitHub |

---

## 4. Gouvernance et escalade
* **Suivi hebdomadaire :** Mise à jour lors du comité de suivi (COSU).
* **Alerte critique :** Tout risque avec une criticité $\ge 12$ est remonté au **Product Owner**.