# 🧭 Spécifications Fonctionnelles (LE QUOI) : Module Gestion des Tâches

Ce document détaille les règles métier et les critères d'acceptation. C'est la base de référence pour valider le besoin utilisateur.

*C'est ce que le Product Owner dit à l'architecte. "Je veux 3 chambres, une cuisine ouverte et que la porte s'ouvre avec un code". C'est le BESOIN utilisateur.*

---

**Projet :** Modernisation du flux de travail technique (MVP)

**Version :** 1.0

**Référent :** Product Owner (PO) / Chef de Projet

**Cible :** Client (validation), Équipe de développement (compréhension), Testeurs (préparation des tests).

**Statut :** En cours de rédaction

**Date : ** xx/xx/xxxx

---

## 👥 1. Acteurs et Rôles
*   **Technicien :** Peut consulter sa liste de tâches, modifier le statut d'une tâche assignée et ajouter des commentaires.
*   **Manager :** Peut créer des tâches, les assigner et visualiser l'avancement global.

---

## 🛠️ 2. Description des Fonctionnalités

### 2.1 Gestion des tâches (US_01)
*   **Description :** Affichage d'une liste de missions triées par priorité.
*   **Champs obligatoires :** Titre, Description, Date d'échéance, Priorité (Basse/Moyenne/Haute).

### 2.2 Mise à jour du statut (US_02)
*   **Workflow :** `À faire` ➔ `En cours` ➔ `Terminé`.
*   **Règles métier :** 
    *   Une tâche ne peut pas être marquée "Terminée" si la description est vide.
    *   Seul le technicien assigné peut modifier le statut.

---

## 📱 3. Interface et Cinématique (IHM)
*   **Écran d'accueil :** Dashboard avec compteurs (Tâches en retard, à faire).
*   **Navigation :** Menu latéral pour basculer entre "Mes tâches" et "Paramètres".

---

## 📈 4. Besoins Non-Fonctionnels
*   **Disponibilité :** 99.9% (hors maintenance).
*   **Temps de réponse :** < 1s pour l'affichage de la liste.