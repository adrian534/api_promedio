# 🎓 API de Cálculo de Promedio con Flask

Este proyecto consiste en el desarrollo de una API REST utilizando **Python** y el micro-framework **Flask**. El servicio permite recibir un objeto JSON con el nombre de un estudiante y una lista de calificaciones para devolver automáticamente el promedio calculado.

## 🚀 Funcionalidades
* Recepción de datos mediante el método **POST**.
* Procesamiento de listas dinámicas de calificaciones.
* Respuesta estructurada en formato **JSON**.

---

## 📸 Evidencias de Funcionamiento

### 1. Ejecución del Servidor
A continuación se muestra la terminal con el servidor de Flask activo y corriendo en el entorno local:
![Servidor Activo](URL_DE_TU_CAPTURA_1)

### 2. Prueba de la API (Petición POST)
Prueba realizada mediante el comando `curl`, donde se observa el envío de datos y la respuesta exitosa del servidor con el promedio calculado:
![Prueba de API](URL_DE_TU_CAPTURA_2)

### 3. Error de Método (Navegador)
Evidencia de que el endpoint `/promedio` está protegido y solo acepta el método POST (en el navegador muestra *Method Not Allowed*):
![Error de Método](URL_DE_TU_CAPTURA_3)

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Framework:** Flask
* **Herramientas:** Git, GitHub, Terminal (Zsh)
