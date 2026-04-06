# 📑 Registre des dépendances, contraintes et risques

**Projet :** [nom du projet]  
**Responsable :** [ton nom]  
**Version :** 1.0  
**Date :** 02/04/2026

---

## 1. Registre des dépendances
*Éléments indispensables (internes ou externes) à la progression du projet.*

| ID | Tâche antécédente (la source) | Tâche bloquée (la conséquence) | Responsable | Échéance | Impact |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **DEP-01** | Accès aux bases de données sources | Phase d'ingestion (etl) | DSI / it client | Semaine 2 | **Arrêt total** du flux. |
| **DEP-02** | Validation du cahier des charges | Début des développements | Mentor / client | [date] | **Report global** planning. |
| **DEP-03** | Réception du dictionnaire de données | Modélisation du schéma sql | Expert métier | [date] | **Risque d'erreurs** mapping. |
| **DEP-04** | Configuration de l'env. cloud | Déploiement et mise en prod | Admin sys | Semaine 3 | **Livraison impossible**. |
| **DEP-05** | Nettoyage des données (cleaning) | Analyse exploratoire (eda) | Data architect | [date] | **Qualité biaisée**. |

---

## 2. Registre des contraintes
*Limites non négociables qui impactent les choix techniques et l'organisation.*

| ID | Nature de la contrainte | Tâche impactée | Source / justification | Impact sur le projet |
| :--- | :--- | :--- | :--- | :--- |
| **CON-01** | Langage : python 3.12 | Développement etl | Standardisation it client | Bibliothèques limitées. |
| **CON-02** | Conformité rgpd | Stockage & traitement | Règlementation légale | Anonymisation obligatoire. |
| **CON-03** | Hébergement github | Versioning & wiki | Méthodologie imposée | Traçabilité centralisée. |
| **CON-04** | Délai de 324 heures | Sprint planning | Budget temps académique | Priorisation (moscow). |

---

## 3. Analyse des risques (amdec)
*Anticipation des menaces. Criticité (c) = gravité (g) x probabilité (p) sur 5.*

| ID | Risque identifié (événement) | G | P | C | Tâche impactée | Plan de mitigation (action) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **RSQ-01** | Données sources corrompues | 5 | 3 | **15** | Analyse (eda) | Script de data quality check. |
| **RSQ-02** | Retard de validation client | 3 | 4 | **12** | Jalons de livraison | Relances j-2 et j-1 (email). |
| **RSQ-03** | Incompatibilité de librairie | 4 | 2 | **8** | Environnement dev | Utilisation de `requirements.txt`. |
| **RSQ-04** | Perte accidentelle de code | 5 | 1 | **5** | Intégrité du projet | Push quotidien sur github. |
| **RSQ-05** | Indisponibilité du mentor | 3 | 2 | **6** | Revue de sprint | Wiki à jour pour autonomie. |

---

## 4. Gouvernance et escalade
* **Suivi hebdomadaire :** mise à jour lors du comité de suivi (cosu).
* **Alerte critique :** tout élément avec une criticité $\ge 12$ est remonté au **chef de projet**.