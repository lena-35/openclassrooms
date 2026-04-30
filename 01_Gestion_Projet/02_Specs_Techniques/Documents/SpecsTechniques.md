# 🛠️ Spécifications Techniques (LE COMMENT) : Architecture & Flux

Ce document est le plan de construction pour les développeurs (Architecture, Flux, Pseudocode).

*C'est ce que l'architecte dit aux maçons. "On va utiliser des briques de 20cm, du béton armé pour les fondations et un serveur de marque X pour gérer le code de la porte". C'est la RÉPONSE technologique.*

---

**Projet :** Modernisation du flux de travail technique (MVP)

**Version :** 1.0

**Référent :** Lead Developer / Architecte Logiciel

**Cible :** Développeurs (pour coder), DevOps (pour l'infrastructure), Architectes (pour la cohérence du système).

**Statut :** En attente de validation

**Date : ** xx/xx/xxxx

---

## 🏗️ 1. Architecture Logicielle & Environnement

### 1.1 Modèle Architectural
L'application repose sur un modèle **MVC (Modèle-Vue-Contrôleur)** :
*   **Modèle (Model) :** Gestion de la persistance (Base de données PostgreSQL).
*   **Vue (View) :** Interface mobile développée en Java (Android).
*   **Contrôleur (Controller) :** Logique métier développée en API REST Python (Flask/FastAPI).

### 1.2 Environnement d'exécution
*   **Backend :** Python 3.10+
*   **Frontend :** Java 17 (SDK Android 33)
*   **Protocole :** REST via HTTP/S
*   **Format d'échange :** JSON (UTF-8)

---

## 🔄 2. Conception des Modules & Flux

### 2.1 Flux de données : "Modification du statut d'une tâche"
1.  **UI (Java) :** L'utilisateur clique sur "Terminer". L'UI envoie un `PATCH` à `/api/v1/tasks/{id}`.
2.  **Controller (Python) :** Réceptionne la requête, extrait le `task_id` et le `new_status`.
3.  **Validation :** Le contrôleur vérifie que l'utilisateur est bien l'assigné de la tâche.
4.  **Persistance (DB) :** Mise à jour du champ `status` dans la table `tasks`.
5.  **Output :** Renvoi d'un code HTTP 200 (Succès) ou 403 (Refusé).

---

## 💻 3. Détails d'Implémentation

### 3.1 Pseudocode (Logique métier de mise à jour)
```python
FONCTION update_task_status(task_id, new_status, user_token):
    # 1. Sécurité : Vérifier l'identité via le token
    user = auth_service.get_user(user_token)
    SI user EST nul ALORS RETOURNER Erreur(401, "Non authentifié")

    # 2. Récupération : Chercher la tâche en base
    task = db.find_task_by_id(task_id)
    SI task EST nul ALORS RETOURNER Erreur(404, "Tâche introuvable")

    # 3. Métier : Vérifier la transition de statut
    SI transition_est_invalide(task.status, new_status) ALORS
        RETOURNER Erreur(400, "Transition impossible")

    # 4. Action : Enregistrer et notifier
    task.status = new_status
    db.save(task)
    notification_service.send(task.owner, "Statut mis à jour")
    
    RETOURNER Succès(200)