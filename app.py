import streamlit as st
import pandas as pd
import algoritmos

st.set_page_config(page_title="Predicción Matemáticas Aplicadas")

# Menú lateral
seccion = st.sidebar.radio("Menú", ["Inicio", "Subir CSV y Predecir", "Tutoriales"])

# SECCIÓN INICIO
if seccion == "Inicio":
    st.title("🧠 Proyecto: Predicción con Algoritmos de Aprendizaje")
    st.markdown("""
    Bienvenido al proyecto de Matemáticas Aplicadas.

    En esta aplicación puedes:
    - 📁 Subir tus datos en formato CSV
    - 🤖 Seleccionar un algoritmo de predicción
    - 📈 Obtener resultados al instante

    También encontrarás tutoriales para entender mejor cómo funciona cada algoritmo.
    """)

# SECCIÓN PREDICCIÓN
elif seccion == "Subir CSV y Predecir":
    st.title("🔍 Predicción con tus datos")

    archivo = st.file_uploader("📁 Cargar archivo CSV", type=["csv"])

    if archivo is not None:
        df = pd.read_csv(archivo)
        st.write("📄 Vista previa de los datos:")
        st.dataframe(df)

        algoritmo = st.selectbox("Selecciona un algoritmo de predicción", [
            "Árbol de decisión",
            "K-Means",
            "Regresión lineal"
        ])

        if algoritmo != "K-Means":
            target = st.selectbox("Selecciona la variable objetivo (target)", df.columns)

        if st.button("🔍 Predecir"):
            if algoritmo == "Árbol de decisión":
                pred = algoritmos.arbol_decision(df, target)
                st.write("🎯 Predicciones (Árbol de decisión):", pred)

            elif algoritmo == "K-Means":
                clusters = algoritmos.k_means(df.select_dtypes(include='number'))
                st.write("🔹 Cluster asignado para cada fila:", clusters)

            elif algoritmo == "Regresión lineal":
                pred = algoritmos.regresion_lineal(df, target)
                st.write("📈 Predicciones (Regresión lineal):", pred)

            st.success("✅ Predicción realizada con éxito.")

# SECCIÓN TUTORIALES
elif seccion == "Tutoriales":
    st.title("📘 Tutoriales de Algoritmos de Predicción")

    tutorial = st.selectbox("Selecciona un algoritmo para aprender más", [
        "Árbol de decisión",
        "K-Means (agrupamiento)",
        "Regresión lineal"
    ])

    if tutorial == "Árbol de decisión":
        st.header("🌳 Árbol de Decisión")
        st.image("arbol.png", use_container_width=True)

        st.markdown("""
### 🧠 ¿Qué es un Árbol de Decisión?

Es un modelo que simula un árbol donde:
- Cada **nodo** hace una pregunta.
- Cada **rama** representa una respuesta (Sí/No, Alto/Bajo, etc).
- Cada **hoja** da un resultado o predicción.
""")

        # 🔽 SECCIÓN EJEMPLO CON BOTÓN
        st.markdown("### 📊 Ejemplo")

        with open("Ejemplo Arboles de Decisión.xlsx", "rb") as archivo_excel:
            st.download_button(
                label="📥 Descargar ejemplo en Excel",
                data=archivo_excel,
                file_name="Ejemplo Arboles de Decisión.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.markdown("""
---

### 📌 ¿Qué hace el árbol?

Aprende **reglas de decisión** a partir de los datos para **clasificar** nuevas situaciones.

### ✅ ¿Cuándo usarlo?

- Cuando tu resultado es **Sí o No** (o clases).
- Cuando las variables son **categóricas o mixtas**.
- Cuando quieres un modelo **fácil de explicar**.
""")

    elif tutorial == "K-Means (agrupamiento)":
        st.header("📊 K-Means")
        st.image("kmeans.png", use_container_width=True)

        st.markdown("""
### 🤖 ¿Qué es K-Means?

El algoritmo **K-Means** agrupa datos sin saber a qué grupo pertenecen originalmente.

- Divide los datos en **K grupos** (clusters).
- Cada grupo contiene elementos similares.
- Se basa en la distancia a los centroides de los grupos.

---

### 📊 Ejemplo
""")

        with open("Ejemplo K-Means.xlsx", "rb") as archivo_kmeans:
            st.download_button(
                label="📥 Descargar ejemplo de K-Means en Excel",
                data=archivo_kmeans,
                file_name="Ejemplo K-Means.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.markdown("""
---

### ✅ ¿Cuándo usarlo?

- Cuando no tienes etiquetas (datos no clasificados).
- Cuando necesitas descubrir patrones ocultos.
- Para **segmentación de clientes**, análisis de grupos, etc.
""")

    elif tutorial == "Regresión lineal":
        st.header("📈 Regresión Lineal")
        st.image("regresion.png", use_container_width=True)

        st.markdown("""
### 📉 ¿Qué es la Regresión Lineal?

La **regresión lineal** busca encontrar la mejor línea recta que relacione una variable con otra.

- Se usa para **predecir valores numéricos**.
- Tiene la forma: `y = mx + b`

---

### 📊 Ejemplo
""")

        with open("Ejemplo Regresion Lineal.xlsx", "rb") as archivo_regresion:
            st.download_button(
                label="📥 Descargar ejemplo de Regresión Lineal en Excel",
                data=archivo_regresion,
                file_name="Ejemplo Regresion Lineal.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        st.markdown("""
---

### ✅ ¿Cuándo usarlo?

- Cuando la variable de salida es numérica (por ejemplo: ingresos, precios, etc).
- Cuando quieres **detectar tendencias** o hacer predicciones basadas en datos históricos.
""")
