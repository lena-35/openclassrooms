import pandas as pd

# 1. Chargement des données (Palmer Penguins)
print("Chargement des données Penguins...")
filename = "https://raw.githubusercontent.com/OpenClassrooms-Student-Center/8063076-Initiez-vous-au-Machine-Learning/master/data/palmer_penguins_openclassrooms.csv"
data = pd.read_csv(filename)

# Affichage des premières lignes pour valider le chargement
print("\nAperçu des données :")
print(data.head())

##############
# Question 1 #
##############
print("\nQuestion 1:")
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
X = data['bill_length_mm'].values.reshape(-1, 1)
y = data['body_mass_g']
reg.fit(X, y)
score = reg.score(X,y)
print(f"Score R2 pour body_mass_g ~ bill_length_mm : {score:.4f}")

X = data['bill_depth_mm'].values.reshape(-1, 1)
y = data['body_mass_g']

# Entraînement
reg.fit(X, y)

# Score
score = reg.score(X,y)
print(f"Score R2 pour body_mass_g ~ bill_depth_mm : {score:.4f}")

X = data['flipper_length_mm'].values.reshape(-1, 1)
y = data['body_mass_g']
reg.fit(X, y)
score = reg.score(X,y)
print(f"Score R2 pour body_mass_g ~ flipper_length_mm : {score:.4f}")



##############
# Question 2 #
##############
print("\nQuestion 2:")
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X = scaler.fit_transform(data[['bill_length_mm','bill_depth_mm','flipper_length_mm']])

# Entraînement
reg.fit(X, y)

# Prédiction
y_pred = reg.predict(X)

from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error
print(f"RMSE: {mean_squared_error(y, y_pred)}")
print(f"MAPE: {mean_absolute_percentage_error(y, y_pred)}")


##############
# Question 3 #
##############
print("\nQuestion 3:")
scaler = MinMaxScaler()
reg = LinearRegression()
for espece in ['Adelie', 'Gentoo', 'Chinstrap']:
    df = data[data.species == espece].copy()
    y = df['body_mass_g']
    X = scaler.fit_transform(df[['bill_length_mm','bill_depth_mm','flipper_length_mm']])
    # Entraînement
    reg.fit(X, y)
    print(espece, "\nScore: ", reg.score(X, y))

    y_pred = reg.predict(X)
    print(f"RMSE: {mean_squared_error(y, y_pred)}")
    print(f"MAPE: {mean_absolute_percentage_error(y, y_pred)}\n--")


##############
# Question 4 #
##############
print("\nQuestion 4:")
import numpy as np
scaler = MinMaxScaler()
y = data['body_mass_g']
X = scaler.fit_transform(data[['bill_length_mm','bill_depth_mm','flipper_length_mm']])
reg = LinearRegression()

score = []

from sklearn.model_selection import train_test_split
test_size=0.20
for random_state in np.arange(200):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    reg.fit(X_train, y_train)
    print("--\n",test_size, reg.score(X_test, y_test))
    score.append(reg.score(X_test, y_test))

import seaborn as sns
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(6, 6))
sns.boxplot(y=score)  # 'y=score' pour un boxplot vertical plus lisible
plt.title(f"Distribution des scores R2 (test_size={test_size})")

# Remplacez plt.show() par ces deux lignes :
plt.savefig("./Images/Boxplot_resultat.png") 
print("\nGraphique sauvegardé avec succès dans 'Images/Boxplot_resultat.png'")

##############
# Question 5 #
##############
print("\nQuestion 5:")
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# 1. Chargement et préparation des données
filename = "https://raw.githubusercontent.com/OpenClassrooms-Student-Center/8063076-Initiez-vous-au-Machine-Learning/master/data/palmer_penguins.csv"
data = pd.read_csv(filename)

# CORRECTION : On convertit en object pour autoriser le remplacement par des entiers
data['sex'] = data['sex'].astype('object')

data.loc[data.sex == 'male', 'sex'] = 0
data.loc[data.sex == 'female', 'sex'] = 1
data.dropna(inplace=True)
data['sex'] = data['sex'].astype('int')

# Affichages de vérification demandés
print(data['sex'])
print(data['sex'].value_counts())

# 2. Scindage du dataset
scaler = MinMaxScaler()
y = data['sex'].values
X = scaler.fit_transform(data[['bill_length_mm','bill_depth_mm','flipper_length_mm', 'body_mass_g']])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 3. Entraînement et prédictions
clf = LogisticRegression(random_state = 42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred) # On stocke la matrice dans cm

# 4. Matrice de confusion
tn, fp, fn, tp = cm.ravel()

print("Matrice de confusion :\n", cm)
print(f"\nTN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}")


##############
# Question 6 #
##############
print("\nQuestion 6:")
from sklearn.metrics import confusion_matrix, recall_score, precision_score
print("recall_score: ", recall_score(y_test, y_pred))
print("precision_score: ", precision_score(y_test, y_pred))


##############
# Question 7 #
##############
print("\nQuestion 7:")
y_proba = clf.predict_proba(X_test)[:, 1]

# Seuil 0.3
y_pred_03 = [0 if value < 0.3 else 1 for value in y_proba]
cm_03 = confusion_matrix(y_test, y_pred_03)
tn_03, fp_03, fn_03, tp_03 = cm_03.ravel()
print("Matrice de confusion seuil 03:\n", cm_03)
print(f"Seuil 03: TN: {tn_03}, FP: {fp_03}, FN: {fn_03}, TP: {tp_03}\n")

# Seuil 0.7
y_pred_07 = [0 if value < 0.7 else 1 for value in y_proba]
cm_07 = confusion_matrix(y_test, y_pred_07)
tn_07, fp_07, fn_07, tp_07 = cm_07.ravel()
print("Matrice de confusion seuil 07:\n", cm_07)
print(f"Seuil 07: TN: {tn_07}, FP: {fp_07}, FN: {fn_07}, TP: {tp_07}\n")



##############
# Question 8 #
##############
print("\nQuestion 8:")

# Correction du type pour éviter l'erreur TypeError
data['species'] = data['species'].astype('object')
data.loc[data.species == 'Adelie', 'species'] = 3
data.loc[data.species == 'Gentoo', 'species'] = 2
data.loc[data.species == 'Chinstrap', 'species'] = 1
data['species'] = data['species'].astype('int')

scaler = MinMaxScaler()
y = data['species'].values

# Création de X1 (avec poids) et X2 (sans poids)
X1 = scaler.fit_transform(data[['bill_length_mm','bill_depth_mm','flipper_length_mm', 'body_mass_g']])
X2 = scaler.fit_transform(data[['bill_length_mm','bill_depth_mm','flipper_length_mm']])

# Division des jeux de données
X1_train, X1_test, y_train, y_test = train_test_split(X1, y, test_size=0.20, random_state=42)
X2_train, X2_test, y_train, y_test = train_test_split(X2, y, test_size=0.20, random_state=42)

# Entraînement des modèles
clf1 = LogisticRegression(random_state = 42)
clf1.fit(X1_train, y_train)

clf2 = LogisticRegression(random_state = 42)
clf2.fit(X2_train, y_train)

# Prédictions et matrices
y1_pred = clf1.predict(X1_test)
cm1 = confusion_matrix(y_test, y1_pred)
print("Matrice de confusion Modèle 1 (avec poids) :\n", cm1)

y2_pred = clf2.predict(X2_test)
cm2 = confusion_matrix(y_test, y2_pred)
print("\nMatrice de confusion Modèle 2 (sans poids) :\n", cm2)



##############
# Question 9 #
##############
print("\nQuestion 9:")
X = data[['bill_length_mm','bill_depth_mm','flipper_length_mm', 'body_mass_g','sex']]

from sklearn.cluster import KMeans
km = KMeans( n_clusters=3, random_state = 808, n_init = 10)
km.fit(X)
y_pred = km.labels_
data['labels'] = km.labels_
# Comptage du nombre de manchots par espèce et par label
resultat = data[['species', 'labels', 'island']].groupby(by = ['species', 'labels']).count().reset_index().rename(columns = {'island': 'count_'})
print(resultat)


###############
# Question 10 #
###############
print("\nQuestion 10:")
from sklearn.metrics import silhouette_score

scores = []
for n in range(2, 11, 1):
    km = KMeans( n_clusters=n, random_state = 808, n_init = 10)
    km.fit(X)
    labels_ = km.predict(X)
    scores.append(silhouette_score(X,labels_ ))

plt.figure()
plt.plot(range(2, 11, 1), scores)

# Sauvegarde de l'image
plt.savefig("./Images/Silhouette_resultat.png") 
print("\nGraphique sauvegardé avec succès dans 'Images/Silhouette_resultat.png'")