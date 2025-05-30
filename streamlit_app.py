import streamlit as st

st.title("Belajar make up")
st.write("ayo belajar bersama andi")
st.image("IMG-20250518-WA0010.jpeg", width=600)
st.title("Berikut beberapa tips dasar untuk melakukan makeup")
st.write("1. Persiapan: Pastikan wajah bersih dan lembab sebelum memulai makeup. Gunakan primer untuk membuat makeup lebih tahan lama. 2. Foundation: Pilih foundation yang sesuai dengan warna kulit Anda. Aplikasikan secara merata untuk menyamarkan noda dan ketidaksempurnaan. 3. Concealer: Gunakan concealer untuk menutupi noda dan lingkaran hitam di bawah mata. 4. Eyeshadow: Pilih warna eyeshadow yang sesuai dengan warna mata Anda. Aplikasikan secara bertahap untuk menciptakan efek yang diinginkan. 5. Mascara: Gunakan mascara untuk mempertebal dan memperpanjang bulu mata. 6. Lipstik atau Lip Gloss: Pilih warna lipstik atau lip gloss yang sesuai dengan warna kulit dan preferensi Anda.")
st.title("Rating makeup gambar tersebut:")
st.header("rate dari 1 - 10") 
angka= st.number_input("70:", value=0, step=1) 

if(angka % 2) == 0:
  st.write(f"{2,4,6,8,10} adalah mantapp!! baguss rating nya") 
else:
  st.write(f"{1,3,5,7,9} adalah baguss makasih yaa!")
