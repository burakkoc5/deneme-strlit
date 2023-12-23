import streamlit as st


# Streamlit uygulaması
st.title("Veri Bilimi Modeli Dashboard")

# Veri setini gösterme
st.subheader("Veri Seti")
# Model Performansı
st.subheader("Model Performansı")
# Eğitim seti doğruluğu
st.write(f"Eğitim Seti Doğruluğu: ")


# Kullanıcıdan özellik değerlerini girmesini isteme
sepal_length = st.slider("Sepal Length", float(X['sepal length (cm)'].min()), float(X['sepal length (cm)'].max()), float(X['sepal length (cm)'].mean()))
sepal_width = st.slider("Sepal Width", float(X['sepal width (cm)'].min()), float(X['sepal width (cm)'].max()), float(X['sepal width (cm)'].mean()))
petal_length = st.slider("Petal Length", float(X['petal length (cm)'].min()), float(X['petal length (cm)'].max()), float(X['petal length (cm)'].mean()))
petal_width = st.slider("Petal Width", float(X['petal width (cm)'].min()), float(X['petal width (cm)'].max()), float(X['petal width (cm)'].mean()))
st.write(f"Test Seti Doğruluğu:")

# Sınıflandırma tahmini
st.subheader("Sınıflandırma Tahmini")
st.write('Hello world!')
