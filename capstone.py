import streamlit as st
import pandas as pd

st.set_page_config(layout = "centered")

with st.sidebar:
    st.header("Mengenai Penulis")
    st.subheader("William Wirawan")
    st.caption("_DQLab Tetris Batch 3 #171_")
    st.caption("LinkedIn profile: ")
    st.caption("https://linkedin.com/in/william-wirawan")
        
    from PIL import Image

    image = Image.open("C:/Users/William/IMG_2382.PNG")
    st.image(image,
            use_column_width=True
    )

    image = Image.open("C:/Users/William/IMG_2383.PNG")
    st.image(image,
            use_column_width=True
    )

st.title("Perkembangan Indeks Harga Saham Gabungan")
st.markdown("_Data harian periode Januari - Desember 2022_")
st.caption("Penulis: William Wirawan")

st.write("Dalam perkembangannya, IHSG telah menjadi salah satu tolok ukur penting yang digunakan oleh para investor dan analis untuk mengukur kinerja pasar saham Indonesia. Dalam perjalanan waktu, perubahan IHSG mencerminkan naik turunnya harga saham di pasar dan mempengaruhi kondisi ekonomi secara luas.")

st.write("Membaca dan memahami IHSG dapat memberikan gambaran tentang bagaimana perusahaan-perusahaan di Indonesia tumbuh dan berkembang, serta bagaimana kondisi ekonomi secara keseluruhan. Hal ini juga membantu investor dalam mengambil keputusan investasi yang tepat.")

# uploaded_file = st.file_uploader("upload foto", type=["jpg", "jpeg", "png"])
# if uploaded_file is not None:
#     st.image(uploaded_file, caption="ilustrasi Bursa Efek Indonesia", use_column_width=True)

from PIL import Image

image = Image.open("Gambar\Gambar Bursa Efek Indonesia.jpg")
st.image(image,
         caption="ilustrasi Bursa Efek Indonesia", use_column_width=True
)

st.write("IHSG adalah indeks pasar saham utama yang mewakili pergerakan harga saham secara keseluruhan di Bursa Efek Indonesia. Indeks ini dihitung berdasarkan kapitalisasi pasar (market capitalization) dari saham-saham yang tercatat di bursa. Dalam perhitungannya, IHSG memberikan bobot yang lebih besar pada saham-saham dengan kapitalisasi pasar yang lebih tinggi. IHSG sering dianggap sebagai cerminan dari sentimen investasi dan performa ekonomi Indonesia.")
st.write("Per tanggal 31 Desember 2022, jumlah perusahaan yang tercatat (emiten) di Bursa Efek Indonesia sebanyak 824 emiten.")

st.write("Selain IHSG, terdapat juga 11 indeks sektoral di Bursa Efek Indonesia yang mencerminkan performa sektor-sektor tertentu dalam pasar saham. Berikut adalah 11 indeks sektoral tersebut:")

data = pd.read_csv("jumlah_emiten_per_sector.csv")
st.table(data)

st.write("Informasi mengenai distribusi jumlah emiten per sektor dapat dilihat di bawah.")

image = Image.open("Gambar\distribusi_jumlah_emiten_per_sektor.png")
st.image(image,
         caption="distribusi jumlah emiten per sektor", use_column_width=True
)

st.write("Dari scatterplot di atas, sektor **healthcare**, **transportation** dan **technology** memiliki jumlah emiten paling sedikit di Bursa Efek Indonesia, yakni di bawah 40 emiten.")
st.write("Sedangkan sektor **cyclicals**, **non_cyclicals** dan **financials** menjadi penyumbang emiten terbanyak yaitu di atas 100 emiten, bahkan sektor cyclicals dengan 139 emiten.")

st.header("CORRELATION HEATMAP")

st.write("Masing-masing sektor memberikan kontribusi terhadap naik turunnya pergerakan Indeks Harga Saham Gabungan setiap harinya.")
st.write("Setiap sektor memiliki hubungan dan pengaruh yang berbeda-beda terhadap IHSG maupun sektor lainnya. Secara garis besar, kita dapat melihatnya melalui correlation heatmap di bawah ini.")

image = Image.open("Gambar\ihsg_heatmap_correlation.png")
st.image(image,
         caption="peta hubungan antar sektor di Bursa Efek Indonesia", use_column_width=True
)

with st.expander("Insight dari correlation heatmap"):
    st.write("1. Sektor **basic materials** dan **industrials** memiliki korelasi positif yang kuat terhadap pergerakan IHSG")
    st.write("2. Sektor **properties** memiliki korelasi positif namun lemah terhadap pergerakan IHSG")
    st.write("3. **Healthcare** menjadi satu-satunya sektor yang berkorelasi negatif terhadap pergerakan IHSG")

st.write("Scatterplot dapat digunakan untuk menampilkan pola, kecenderungan, atau korelasi antara dua variabel.")
st.write("Berikut scatterplot dari beberapa sektor yg berkorelasi dengan IHSG.")

st.header("SCATTERPLOT")

image = Image.open("Gambar\scatterplot_ihsg_basic_materials.png")
st.image(image,
         use_column_width=True
)

image = Image.open("Gambar\scatterplot_ihsg_industrials.png")
st.image(image,
         use_column_width=True
)

image = Image.open("Gambar\scatterplot_ihsg_healthcare.png")
st.image(image,
         use_column_width=True
)

with st.expander("Insight dari scatterplot"):
    st.write("1. Persebaran data antara IHSG dan sektor **basic materials** dan **industrials** memiliki arah dari kiri bawah ke kanan atas yang menandakan adanya korelasi positif antara IHSG dan kedua sektor tersebut")
    st.write("2. Dari scatterplot antara IHSG dan sektor **healthcare**, persebaran data terlihat merata dan cenderung berkumpul di kanan bawah yang mengindikasikan korelasi negatif terhadap pergerakan IHSG")

st.write("Untuk melihat pergerakan Indeks Harga Saham Gabungan dari waktu ke waktu (dalam hal ini Januari s/d Desember 2022), kita dapat merujuk kepada lineplot berikut ini.")

st.header("LINEPLOT")

image = Image.open("Gambar\lineplot_ihsg.png")
st.image(image,
         use_column_width=True
)

st.write("IHSG memiliki 2 titik tertinggi yaitu sekitar bulan April dan September")

image = Image.open("Gambar\lineplot_basic_materials.png")
st.image(image,
         use_column_width=True
)

st.write("Sektor basic_materials memiliki kemiripan titik tertinggi dengan IHSG, yaitu di bulan April")

image = Image.open("Gambar\lineplot_industrials.png")
st.image(image,
         use_column_width=True
)

st.write("Sektor industrials juga memiliki kemiripan dengan IHSG yaitu mencapai titik tertinggi di bulan September")

image = Image.open("Gambar\lineplot_properties.png")
st.image(image,
         use_column_width=True
)

st.write("Pada periode yang sama, IHSG menunjukkan pergerakan yang cukup fluktuatif, di sisi lain pergerakan sektor properties tidak terlalu fluktuatif")

st.write("Kesimpulan:")
st.write("1. **Basic_materials** dan **industrials** adalah dua sektor yang memiliki korelasi positif terkuat terhadap pergerakan IHSG, artinya pergerakan kedua sektor ini searah dengan pergerakan IHSG dimana bila kedua sektor ini menguat, akan memberikan dampak penguatan terhadap IHSG dan juga sebaliknya.")
st.write("2. Sementara **healthcare** adalah satu-satunya sektor yang bergerak berlawanan dengan IHSG dimana bila sektor healthcare mengalami pelemahan, maka IHSG akan mengalami penguatan.")
st.write("3. Jumlah emiten terbesar ada di sektor **cyclicals, non_cyclicals, dan financials**. Namun banyaknya jumlah emiten tersebut tidak memiliki pengaruh yang signifikan terhadap pergerakan IHSG.")
st.write("4. Jumlah emiten terkecil ada di sektor **healthcare, transportation, dan technology**. Serupa dengan hal di atas, jumlah emiten tidak mempengaruhi pergerakan IHSG secara signifikan.")
