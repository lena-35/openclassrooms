from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# =====================================================================
# THÉORIE : CLASSIFICATION MULTICLASSE NOMINALE
# Contrairement au cas binaire (0 ou 1), le dataset Iris comporte 3 classes non ordonnées.
# La régression logistique s'adapte automatiquement (via la stratégie One-vs-Rest ou Multinomiale).
# =====================================================================

X, y = load_iris(return_X_y=True)  # 3 espèces d'Iris (0, 1, 2)

# Séparation 80% Train / 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=808)

# Entraînement du modèle multiclasse
clf = LogisticRegression(random_state=808, max_iter=10000)
clf.fit(X_train, y_train)

# Évaluation sur les données inconnues de Test
y_pred = clf.predict(X_test)

print("=== RÉGRESSION LOGISTIQUE MULTICLASSE (IRIS TEST) ===")
# La matrice est ici un tableau 3x3 (une ligne et colonne par espèce)
print("Matrice de confusion 3x3 :")
print(confusion_matrix(y_test, y_pred))

print("\nRapport de classification détaillé :")
print(classification_report(y_test, y_pred))