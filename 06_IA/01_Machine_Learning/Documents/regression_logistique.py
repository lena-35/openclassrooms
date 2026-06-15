import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split

# =====================================================================
# THÉORIE : RÉGRESSION LOGISTIQUE BINAIRE
# La fonction logistique (sigmoïde) écrase la sortie linéaire entre [0, 1] 
# pour fournir la probabilité d'appartenir à la catégorie cible.
# =====================================================================

X, y = load_breast_cancer(return_X_y=True)

# Séparation 80% Train / 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=808)

clf = LogisticRegression(random_state=808, max_iter=10000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)                  # Sort les classes (Seuil t = 0.5)
y_hat_proba = clf.predict_proba(X_test)[:, 1]  # Sort la probabilité de la classe 1

print("=== ÉVALUATION DE LA RÉGRESSION LOGISTIQUE (TEST) ===")
# PARADOXE DE L'EXACTITUDE : Une bonne accuracy (bien classés / total) peut cacher 
# un mauvais ciblage si les classes sont déséquilibrées. On vérifie via la matrice.
print(f"Exactitude (Accuracy) : {accuracy_score(y_test, y_pred):.3f}")

# CONFIGURATION SCIKIT-LEARN DE LA MATRICE DE CONFUSION :
# Classes triées numériquement (0 puis 1) :
#           Prédit 0     Prédit 1
# Réel 0   [   TN    ,    FP    ]  <- (TN: Vrais Négatifs, FP: Faux Positifs)
# Réel 1   [   FN    ,    TP    ]  <- (FN: Faux Négatifs, TP: Vrais Positifs)
print("\nMatrice de confusion (Seuil t=0.5) :")
print(confusion_matrix(y_test, y_pred))

# SEUILS PERSONNALISÉS (Exemple du cours avec t = 0.3)
y_pred_03 = [0 if val < 0.3 else 1 for val in y_hat_proba]
print("\nMatrice de confusion (Seuil t=0.3) :")
print(confusion_matrix(y_test, y_pred_03))

# Rappel = TP / (TP+FN) -> Minimise les Faux Négatifs (vital en médecine)
# Précision = TP / (TP+FP) -> Minimise les Faux Positifs (vital pour éviter les faux spams)
print(f"Précision (t=0.3) : {precision_score(y_test, y_pred_03):.4f}")
print(f"Rappel (t=0.3) : {recall_score(y_test, y_pred_03):.4f}")

# COURBE ROC ET SCORE AUC
# Courbe du Rappel en fonction du taux de Faux Positifs pour TOUS les seuils.
# L'AUC (Aire sous la courbe) varie de 0.5 (aléatoire) à 1.0 (parfait).
print(f"\nScore global ROC-AUC : {roc_auc_score(y_test, y_hat_proba):.4f}")