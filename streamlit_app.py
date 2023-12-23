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
sepal_length = st.slider("Sepal Length")

st.write(f"Test Seti Doğruluğu:")

# Sınıflandırma tahmini
st.subheader("Sınıflandırma Tahmini")
st.write('Hello world!')
