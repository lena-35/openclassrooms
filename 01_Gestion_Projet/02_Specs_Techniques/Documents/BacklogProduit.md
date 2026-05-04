# 📋 Backlog Produit : Application de Gestion de Tâches

Ce document fait le pont entre le client et l'équipe technique. Il définit les fonctionnalités à développer, leur priorité et les critères de validation.

---

**Projet :** Modernisation du flux de travail technique (MVP)

**Version :** 1.0

**Référent :** Product Owner (PO)

**Cible :** Équipe de développement (pour l'estimation), Client (pour le suivi).

**Statut :** Prêt pour le Sprint Planning

**Date : ** xx/xx/xxxx

---

## 🎯 1. Objectifs du Projet
*   **Cible :** Équipes techniques de la start-up (Techniciens & Managers).
*   **Problème :** Frustration liée à la perte d'information, manque de clarté des assignations et suivi de statut informel.
*   **Indicateur de succès :** 100% des tâches assignées sont tracées dans l'outil d'ici la fin du mois.

---

## 📝 2. User Stories Détaillées (Priorité MoSCoW)

| ID | Priorité | Titre | Description | Estimation (SP) |
| :--- | :--- | :--- | :--- | :--- |
| **US_01** | **MUST** | Création de tâche | En tant qu'utilisateur, je veux créer une tâche avec un titre et une description afin de lister mon travail. | 3 |
| **US_02** | **MUST** | Assignation | En tant qu'administrateur, je veux assigner une tâche à un collaborateur afin de répartir la charge. | 2 |
| **US_03** | **SHOULD** | Filtrage temporel | En tant qu'utilisateur, je veux filtrer les tâches par date d'échéance afin de prioriser mes actions. | 5 |
| **US_04** | **COULD** | Personnalisation | En tant qu'utilisateur, je veux personnaliser la couleur de mes étiquettes pour mon confort visuel. | 1 |

---

## ✅ 3. Critères d'Acceptation (Détail des US)

### US_01 : Création de tâche
*   **Critère 1 :** Un formulaire permet de saisir un titre (max 50 car.) et une description (max 500 car.).
*   **Critère 2 :** La tâche est enregistrée avec le statut par défaut "À faire".
*   **Critère 3 :** Un message de succès confirme la création à l'utilisateur.

### US_02 : Assignation de tâche
*   **Critère 1 :** Le manager accède à une liste déroulante des utilisateurs actifs.
*   **Critère 2 :** Seul un utilisateur avec le rôle "Manager" peut voir le bouton d'assignation.
*   **Critère 3 :** L'assigné reçoit une notification (Push ou Email) automatique.

### US_03 : Filtrage par échéance
*   **Critère 1 :** L'utilisateur peut sélectionner une plage de dates (début/fin).
*   **Critère 2 :** Les tâches s'actualisent dynamiquement sans rechargement de la page complète.
*   **Critère 3 :** Les tâches dont la date est dépassée s'affichent en rouge.

---

## ⚠️ 4. Exigences Non-Fonctionnelles (NF)

*   **Performance (NF_01) :** Le temps de chargement de la liste (jusqu'à 100 éléments) ne doit pas excéder 2 secondes.
*   **Sécurité (NF_02) :** Seuls les utilisateurs authentifiés via JWT peuvent accéder aux fonctions de modification.
*   **Accessibilité (NF_03) :** L'interface doit être lisible sur écran mobile de 5 pouces minimum.

---

## 📜 5. Journal des Modifications (Changelog)

| Date | Version | Auteur | Nature de la modification |
| :--- | : :--- | :--- | :--- |
| 30/04/2026 | 1.0 | [Nom] | Création du Backlog initial et définition des critères d'acceptation. |