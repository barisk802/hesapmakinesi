import streamlit as st

st.title("🖩 Hesap Makinesi")

st.write("Yapmak istediğiniz işlemi ve sayıları giriniz:")

# Sayı girişleri
a = st.number_input("Birinci Sayı:", step=1.0)
b = st.number_input("İkinci Sayı:", step=1.0)

# İşlem seçimi
işlem = st.selectbox(
    "İşlemi Seçiniz:",
    ("Toplama", "Çıkarma", "Çarpma", "Bölme")
)

# Hesapla butonu
if st.button("Hesapla"):
    if işlem == "Toplama":
        sonuc = a + b
        st.success(f"{a} + {b} = {sonuc}")
    elif işlem == "Çıkarma":
        sonuc = a - b
        st.info(f"{a} - {b} = {sonuc}")
    elif işlem == "Çarpma":
        sonuc = a * b
        st.warning(f"{a} × {b} = {sonuc}")
    elif işlem == "Bölme":
        if b == 0:
            st.error("Bir sayı sıfıra bölünemez ❌")
        else:
            sonuc = a / b
            st.success(f"{a} ÷ {b} = {sonuc}")








