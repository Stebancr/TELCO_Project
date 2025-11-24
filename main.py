from flask import Flask, render_template, request
import uvicorn
import joblib
import numpy as np # Importar para manejar posibles NaNs/errores de conversión

app = Flask(__name__)

# --- CONFIGURACIÓN DE MODELOS Y DESCRIPCIONES ---
try:
    # Cargar modelos
    logistic_model = joblib.load('models/logistic_model.pkl')
    knn_model = joblib.load('models/knn_model.pkl')
    # K-Means carga la tupla (scaler, model)
    scaler_kmeans, kmeans_model = joblib.load('models/kmeans_model.pkl')
    MODELS_LOADED = True
except FileNotFoundError:
    print("ADVERTENCIA: No se encontraron los archivos de modelos. Ejecute train_models.py para generarlos.")
    MODELS_LOADED = False
except Exception as e:
    print(f"Error al cargar los modelos: {e}")
    MODELS_LOADED = False


# Descripciones de los clusters (asumiendo que son para Telco, aunque el prompt sugiere otro dataset)
# Se mantienen las descripciones predefinidas por el equipo.
cluster_descriptions = { 0: "Clientes con alta permanencia y cargos mensuales altos.", 1: "Clientes nuevos con cargos medios.", 2: "Clientes con cargos bajos y bajo riesgo." }


# Función de utilidad para convertir string a float (manejando el caso de TotalCharges vacío/NaN en el dataset original)
def safe_float(value):
    """Convierte un valor de formulario a float, reemplazando cadenas vacías con 0.0 o NaN."""
    if value is None or value.strip() == '':
        return 0.0 # Usamos 0.0 por simplicidad en la demo, aunque en un entorno real se usaría imputación o NaN.
    try:
        return float(value)
    except ValueError:
        return 0.0 # Valor predeterminado en caso de error de conversión


@app.route('/', methods=['GET', 'POST'])
def index():
    # Inicializar resultados
    telco_result = None
    kmeans_result = None
    error_message = None

    if not MODELS_LOADED:
        error_message = "ERROR: Los modelos ML no pudieron cargarse. Asegúrate de que 'models/logistic_model.pkl', 'models/knn_model.pkl' y 'models/kmeans_model.pkl' existen."
        return render_template("index.html", error_message=error_message)


    if request.method == 'POST':
        action = request.form.get('action')

        try:
            if action == 'predict_churn':
                # --- Lógica de Regresión Logística y KNN (Telco Churn) ---
                senior = safe_float(request.form.get("SeniorCitizen_churn"))
                tenure = safe_float(request.form.get("tenure_churn"))
                monthly = safe_float(request.form.get("MonthlyCharges_churn"))
                total = safe_float(request.form.get("TotalCharges_churn"))

                X = np.array([[senior, tenure, monthly, total]])

                # Predicciones
                prob = logistic_model.predict_proba(X)[0][1]
                log_pred = logistic_model.predict(X)[0]
                knn_pred = knn_model.predict(X)[0]

                telco_result = {
                    "log_prob": round(prob, 4),
                    "log_result": "Sí" if log_pred == 1 else "No",
                    "knn_result": "Sí" if knn_pred == 1 else "No"
                }

            elif action == 'predict_kmeans':
                # --- Lógica de K-Means (Clustering) ---
                # Este modelo usa un subconjunto de variables
                senior = safe_float(request.form.get("SeniorCitizen_kmeans"))
                tenure = safe_float(request.form.get("tenure_kmeans"))
                monthly = safe_float(request.form.get("MonthlyCharges_kmeans"))

                X_kmeans = np.array([[senior, tenure, monthly]])

                # Escalar y predecir
                X_scaled = scaler_kmeans.transform(X_kmeans)
                cluster = int(kmeans_model.predict(X_scaled)[0])

                kmeans_result = {
                    "cluster": cluster,
                    "desc": cluster_descriptions.get(cluster, "Descripción no disponible para este cluster.")
                }

        except Exception as e:
            error_message = f"Error al procesar la solicitud para el modelo {action}: {str(e)}"

    # Devolver la plantilla con todos los posibles resultados
    return render_template(
        "index.html",
        telco_result=telco_result,
        kmeans_result=kmeans_result,
        error_message=error_message
    )


if __name__ == '__main__':
    # Configurar puerto y modo para el entorno de prueba
    uvicorn.run("main:app", host="0.0.0.0", port=5001,reload=True)