import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# =====================================================================
# THÉORIE : LIEN ENTRE RÉGRESSION ET CLASSIFICATION
# Le cours explique qu'on peut essayer d'adapter une régression linéaire standard
# au cas binaire en projetant la prédiction y continue dans un intervalle [0, 1].
# Si la valeur prédite est < 0.5 -> catégorie 0 ; si >= 0.5 -> catégorie 1.
# =====================================================================

X, y = load_breast_cancer(return_X_y=True)

# Séparation 80% Train / 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=808)

# On entraîne une régression linéaire classique (Moindres Carrés) sur des cibles 0/1
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

# On récupère les prédictions continues (qui peuvent dépasser 0 ou 1)
y_pred_continuous = lin_reg.predict(X_test)

# Application du seuil t = 0.5 décrit dans le cours pour forcer une décision binaire
y_pred_class = [0 if val < 0.5 else 1 for val in y_pred_continuous]

print("=== RÉGRESSION LINÉAIRE APPLIQUÉE À LA CLASSIFICATION ===")
print(f"5 premières prédictions continues brutes : {y_pred_continuous[:5]}")
print(f"5 premières classes obtenues après seuillage : {y_pred_class[:5]}")