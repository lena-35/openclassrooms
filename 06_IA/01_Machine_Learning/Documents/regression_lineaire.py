import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# =====================================================================
# THÉORIE : RÉGRESSION LINÉAIRE MULTIPLE
# Prédire une valeur numérique continue (Ventes) à partir de plusieurs
# prédicateurs (TV, Radio, Journal). On cherche l'équation linéaire optimale.
# =====================================================================

# Chargement du fichier du cours
df = pd.read_csv("Advertising.csv")
X = df[["TV", "Radio", "Newspaper"]].values
y = df["Sales"].values

# Séparation 80% Train / 20% Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=808)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("=== ÉVALUATION DE LA RÉGRESSION LINÉAIRE (TEST) ===")
# R² proche de 1 = le modèle explique bien les variations des ventes
print(f"Score R² : {r2_score(y_test, y_pred):.4f}")
# RMSE = écart moyen constaté entre la droite et les vraies ventes
print(f"Erreur RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")