import streamlit as st

st.title("🖩 Hesap Makinesi")

print("""****************************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
****************************
""")





a=int(input("Birinci Sayı:"))
b=int(input("İkinci Sayı:"))
print=("Yapacağınız işlemi seçiniz."(1-Toplama,2-Çıkarma,3-Çarpma,4-Bölme)))

işlem= input("İşlemi Giriniz:")

if işlem=="1":
    print("{} ile {} in toplamı {} dir".format(a,b,a+b))

elif işlem=="2":
    print("{} ile {} in farkı {} dir".format(a,b,a-b))

elif işlem=="3":
    print("{} ile {} çarpı {} dir".format(a,b,a * b))

elif işlem=="4":
    print("{} ile {} bölümü {} dir".format(a,b,a / b))

else :

    print("Geçersiz işlem!")




