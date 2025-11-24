-Luis Steban chocue
-Nicolas Estiven Mosquera Ortiz

Descripción general del sistema
El sistema desarrollado permite predecir la probabilidad de churn (abandono de clientes) utilizando un modelo de Machine Learning previamente entrenado.
El usuario carga un archivo CSV o introduce datos mediante un formulario, y la aplicación devuelve:


La probabilidad de churn expresada en porcentaje.


Un resultado categórico (“Yes” si el cliente probablemente abandonará, “No” si es poco probable).


El objetivo principal es que el usuario visualice de forma sencilla si un cliente tiene riesgo de irse.

Funcionamiento interno del modelo
El modelo utilizado fue entrenado con un conjunto de datos donde cada registro representaba información relevante de los clientes, como:

Duración del contrato
Métodos de pago
Tipo de servicio
Consumo mensual
Historial de uso
Servicios adicionales

A partir de estos datos, se entrenaron modelos (como Regresión Logística, Random Forest o Gradient Boosting) que aprenden patrones asociados al abandono.
Durante la fase de entrenamiento el modelo aprende las relaciones entre las variables y el resultado real (“Churn” o “No churn”).

El archivo model.pkl contiene este modelo ya entrenado.
Flujo de predicción
Cuando el usuario ingresa datos en la aplicación, ocurre lo siguiente:
Preprocesamiento.

Los datos de entrada se transforman exactamente igual que en el entrenamiento:
Se convierten variables categóricas en numéricas (OneHotEncoder).


Se escalan numéricamente features si el modelo lo requiere.


Se reorganiza el orden de las columnas según el modelo entrenado.


Este paso es obligatorio para que la predicción sea coherente con lo aprendido.

Predicción
Una vez procesados, los datos se envían al modelo:
El modelo devuelve un valor entre 0 y 1, que representa la probabilidad de churn.
Clasificación (Yes / No)
Con base en esa probabilidad se define el resultado final:
Si la probabilidad es mayor o igual al 50%, el sistema genera “Yes”.

Si es menor al 50%, genera “No”.
Visualización en la página
La interfaz muestra únicamente:
Probabilidad: por ejemplo, “0.72” → 72%

Resultado: “Yes” o “No”
El objetivo es que la interfaz sea simple y amigable para cualquier usuario, evitando mostrar detalles técnicos.
