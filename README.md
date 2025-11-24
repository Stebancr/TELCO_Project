Proyecto Final – Machine Learning 
Este proyecto integra Machine Learning supervisado y no supervisado dentro de una aplicación web desarrollada en Flask, permitiendo realizar predicciones y segmentaciones basadas en datos de clientes de telecomunicaciones.
🔵 1. Predicción de Churn (Clasificación Supervisada)
La aplicación permite predecir si un cliente abandonará el servicio (Churn) usando dos modelos:
✔ Regresión Logística
Calcula la probabilidad de que un cliente se dé de baja.


Devuelve un resultado final en formato Yes / No.


✔ K-Nearest Neighbors (KNN)
Clasifica al cliente según el comportamiento de sus “vecinos más cercanos”.


También devuelve Yes / No.


📌 Entrada requerida por el usuario:
SeniorCitizen


Tenure (meses de permanencia)


MonthlyCharges


TotalCharges


📌 Salida mostrada en la web:
Probabilidad de Churn


Resultado Regresión Logística (Yes/No)


Resultado KNN (Yes/No)


🟣 2. Segmentación de Clientes (K-Means Clustering)
El sistema agrupa clientes en clusters basados en características numéricas.
✔ K-Means
Clasifica a un cliente en un cluster específico (0, 1 o 2).


Cada cluster tiene una descripción interpretada previamente.


📌 Entrada requerida del usuario:
SeniorCitizen


Tenure


MonthlyCharges


📌 Salida de la web:
Número de cluster asignado


Descripción del cluster (perfil del cliente)


🟢 3. Funcionalidad de la Web
La aplicación Flask:
✔ Recibe datos mediante formularios HTML.
✔ Ejecuta los modelos previamente entrenados (.pkl).
🟠 4. Flujo General del Proyecto
Usuario ingresa datos en el formulario.


Flask procesa la solicitud POST.


Los valores se convierten en un vector para el modelo.


Se cargan los modelos desde los archivos .pkl.


Se ejecuta la predicción (Churn) o clasificación (K-Means).


La web muestra:


Probabilidad


Clasificación (Yes/No)


Cluster asignado


Descripción del cluster



🚀 Instalación
Sigue estos pasos para ejecutar el proyecto en tu máquina.
1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/tu-repo.git
cd tu-repo


2. Crear entorno virtual
python -m venv .venv


3. Activar el entorno virtual
Windows (CMD)
.venv\Scripts\activate
4. Instalar dependencias
pip install -r requirements.txt
Notebooks (Análisis Exploratorio y Modelado)
🔹 Análisis Supervisado – Churn
Telcoprueba.ipynb (https://drive.google.com/file/d/1IBo8XqV1QBpF1dVoyYEsagcx-y0aOElB/view?usp=sharing)
Incluye:
Limpieza de datos


Exploración


Entrenamiento RL y KNN


Graficación de métricas

Aplicación Web
La app web permite utilizar los 3 modelos entrenados.
1. Entrenar y exportar los modelos
python train_models.py
El script:
Carga los datasets


Preprocesa variables


Entrena:
 ✔ Regresión Logística
 ✔ KNN
 ✔ K-Means


Exporta los modelos en archivos .pkl dentro de /modelos/
2. Ejecutar la aplicación web
python main.py
La aplicación abrirá en:
http://localhost:8080

