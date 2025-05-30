import streamlit as st

st.title("belajar make up")
st.write("ayo belajar bersama andi")
st.image("IMG-20250518-WA0010.jpeg", width=600)
st.title("Makeup adalah seni menghias wajah dengan menggunakan berbagai produk kosmetik untuk meningkatkan penampilan. Berikut beberapa tips dasar untuk melakukan makeup:

1. *Persiapan*: Pastikan wajah bersih dan lembab sebelum memulai makeup. Gunakan primer untuk membuat makeup lebih tahan lama.
2. *Foundation*: Pilih foundation yang sesuai dengan warna kulit Anda. Aplikasikan secara merata untuk menyamarkan noda dan ketidaksempurnaan.
3. *Concealer*: Gunakan concealer untuk menutupi noda dan lingkaran hitam di bawah mata.
4. *Eyeshadow*: Pilih warna eyeshadow yang sesuai dengan warna mata Anda. Aplikasikan secara bertahap untuk menciptakan efek yang diinginkan.
5. *Mascara*: Gunakan mascara untuk mempertebal dan memperpanjang bulu mata.
6. *Lipstik atau Lip Gloss*: Pilih warna lipstik atau lip gloss yang sesuai dengan warna kulit dan preferensi Anda.

Beberapa tips tambahan:

- *Blend, blend, blend!* Pastikan untuk membaurkan produk makeup secara merata untuk menciptakan efek yang alami.
- *Kurang lebih lebih baik*. Jangan terlalu berlebihan dalam menggunakan produk makeup, karena ini dapat membuat wajah terlihat tidak alami.
- *Praktik membuat sempurna*. Jangan takut untuk bereksperimen dan mencoba berbagai teknik makeup untuk menemukan apa yang paling sesuai dengan Anda.") 
st.header("Aplikasi menilai ganjil/genap") 
angka= st.number_input("70:", value=0, step=1) 

if(angka % 2) == 0:
  st.write(f"{2,4,6,8,10} rating makeup di atas ini") 
else:
  st.write(f"{1,3,5,7,9} adalah jumlah angka ganjil")
