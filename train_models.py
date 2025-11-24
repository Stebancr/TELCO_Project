import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import os

if not os.path.exists("models"):
    os.makedirs("models")
    print("Carpeta 'models' creada.")

try:
    df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
except FileNotFoundError:
    print("ERROR: El archivo 'WA_Fn-UseC_-Telco-Customer-Churn.csv' no se encuentra.")
    print("Asegúrate de descargarlo para poder entrenar los modelos.")
    exit()

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna()

# ----------------------------------------------------
# PREPARACIÓN DE DATOS
# ----------------------------------------------------

# Variables para Telco Churn (Logística y KNN)
# Estas features son las que se usan en la predicción del riesgo de fuga.
X_churn = df[["SeniorCitizen", "tenure", "MonthlyCharges", "TotalCharges"]]
y_churn = df["Churn"].map({"Yes": 1, "No": 0})

X_kmeans_features = ["SeniorCitizen", "tenure", "MonthlyCharges"]
X_kmeans = df[X_kmeans_features]

# ===============================================
# 1. REGRESIÓN LOGÍSTICA (Para Predicción de Churn)
# ===============================================
log_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

log_pipeline.fit(X_churn, y_churn)
joblib.dump(log_pipeline, "models/logistic_model.pkl")
print("-> models/logistic_model.pkl creado y listo para la predicción de Churn.")

# ===============================================
# 2. KNN (Para Predicción de Churn)
# ===============================================
knn_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", KNeighborsClassifier(n_neighbors=5))
])

knn_pipeline.fit(X_churn, y_churn)
joblib.dump(knn_pipeline, "models/knn_model.pkl")
print("-> models/knn_model.pkl creado y listo para la predicción de Churn.")

# ===============================================
# 3. KMEANS (Para Clustering)
# ===============================================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_kmeans)

km = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = km.fit_predict(X_scaled)

joblib.dump((scaler, km), "models/kmeans_model.pkl")
print("-> models/kmeans_model.pkl creado (contiene scaler y modelo).")

centers = scaler.inverse_transform(km.cluster_centers_)
centers_df = pd.DataFrame(
    centers, 
    columns=X_kmeans_features
)
print("\nCentroides reales del modelo K-Means:")
print(centers_df)
