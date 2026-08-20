import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score, confusion_matrix, silhouette_score
from sklearn.model_selection import train_test_split

# =====================================================================
# THÉORIE : APPRENTISSAGE NON SUPERVISÉ (K-MEANS)
# Pas de variable cible (y) pour s'entraîner. Le but est de regrouper 
# automatiquement les données proches (via la distance euclidienne).
# Objectif : des groupes denses (intra-classe min) et bien séparés (inter-classe max).
# =====================================================================

# --- PARTIE A : LES BLOBS ARTIFICIELS ---
centers = [[2, 2], [-2, -2], [2, -2]]
X_blobs, _ = make_blobs(n_samples=3000, centers=centers, cluster_std=0.7, random_state=808)

# Séparation 80% Train / 20% Test pour valider sur de nouvelles données
X_train_b, X_test_b = train_test_split(X_blobs, test_size=0.20, random_state=808)

k_means = KMeans(n_clusters=3, random_state=808)
k_means.fit(X_train_b)

print("=== 1. ÉVALUATION K-MEANS (BLOBS SUR JEU DE TEST) ===")
# .score() calcule l'inertie (somme des carrés des distances aux centres)
print(f"Inertie relative (Score Test) : {k_means.score(X_test_b):.2f}")

# Silhouette : mesure si le point est bien dans son groupe (proche de 1 = top)
labels_test_b = k_means.predict(X_test_b)
print(f"Coefficient de silhouette : {silhouette_score(X_test_b, labels_test_b):.4f}\n")


# --- PARTIE B : LE DATASET IRIS ---
iris = datasets.load_iris()
X_iris, y_iris = iris.data, iris.target

X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(X_iris, y_iris, test_size=0.20, random_state=808)

model_iris = KMeans(n_clusters=3, n_init="auto", random_state=808)
model_iris.fit(X_train_i)

labels_test_i = model_iris.predict(X_test_i)

# RÉALIGNEMENT DES ÉTIQUETTES : K-Means attribue des numéros de clusters (0,1,2) 
# au hasard. Pour comparer avec les vraies classes (y_test_i), on réaligne proprement :
labels_test_i_clean = labels_test_i.copy()
labels_test_i_clean[labels_test_i == 0] = 1
labels_test_i_clean[labels_test_i == 1] = 0

print("=== 2. ÉVALUATION K-MEANS (IRIS SUR JEU DE TEST) ===")
print(f"Exactitude (Accuracy) : {accuracy_score(y_test_i, labels_test_i_clean):.3f}")
print("Matrice de confusion :")
print(confusion_matrix(y_test_i, labels_test_i_clean))