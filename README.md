Luis Steban Chocue


Nicolas Mosquera

Proyecto Final – Machine Learning 

Este proyecto integra Machine Learning supervisado y no supervisado dentro de una aplicación web desarrollada en Flask, permitiendo realizar predicciones y segmentaciones basadas en datos de clientes de telecomunicaciones.

🔵 1. Predicción de Churn (Clasificación Supervisada)
La aplicación permite predecir si un cliente abandonará el servicio (Churn) usando dos modelos:

✔ Regresión Logística

Calcula la probabilidad de que un cliente se dé de baja.


Devuelve un resultado final en formato Yes / No.


✔ K-Nearest Neighbors (KNN)

Clasifica al cliente según el comportamiento de sus “vecinos más cercanos”.


-También devuelve Yes / No.


📌 Entrada requerida por el usuario:
SeniorCitizen


-Tenure (meses de permanencia)


-MonthlyCharges


-TotalCharges


📌 Salida mostrada en la web:
Probabilidad de Churn


-Resultado Regresión Logística (Yes/No)


-Resultado KNN (Yes/No)


🟣 2. Segmentación de Clientes (K-Means Clustering)

El sistema agrupa clientes en clusters basados en características numéricas.

✔ K-Means

Clasifica a un cliente en un cluster específico (0, 1 o 2).


Cada cluster tiene una descripción interpretada previamente.


📌 Entrada requerida del usuario:

-SeniorCitizen


-Tenure


-MonthlyCharges


📌 Salida de la web:

-Número de cluster asignado


-Descripción del cluster (perfil del cliente)


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


🔹 Análisis Supervisado – Churn

Telcoprueba.ipynb (https://drive.google.com/file/d/1IBo8XqV1QBpF1dVoyYEsagcx-y0aOElB/view?usp=sharing)



Explicacion de app en video: 


https://www.canva.com/design/DAG5kSPFEhQ/GFa-P53t2QrTe9fPQDIh0w/watch?utm_content=DAG5kSPFEhQ&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=hb34e11b7a4





#Instalación

Antes de seguir asegurarse que los scripts esten activado 

ejecuta como administrador el PowerShell
y poner el siguiente comando:


Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

despues de la ejecucion saldra un enunciado asi:


La directiva de ejecución te ayuda a protegerte de scripts en los que no confías. Si cambias dicha directiva, podrías
exponerte a los riesgos de seguridad descritos en el tema de la Ayuda about_Execution_Policies en
https:/go.microsoft.com/fwlink/?LinkID=135170. ¿Quieres cambiar la directiva de ejecución?
[S] Sí  [O] Sí a todo  [N] No  [T] No a todo  [U] Suspender  [?] Ayuda (el valor predeterminado es "N"):

luego presiona la tecla s y enter.


#Ya en el proyecto sigue los siguentes pasos.

Sigue estos pasos para ejecutar el proyecto en tu máquina.



1. Clonar el repositorio



git clone https://github.com/TU_USUARIO/tu-repo.git



2. Crear entorno virtual




python -m venv .venv




3. Activar el entorno virtual        



.venv\Scripts\activate



4.entrar a la ruta:      



venv/Scripts



5. ejecutar en la ruta el siguiente comando



./activate 


6. ejecutar el  siguiente comando



cd ..



7. Instalar dependencias




pip install -r requirements.txt





8.Por ultimo ejecuta la aplicacion 



python main.py




