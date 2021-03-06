# -*- coding: utf-8 -*-
"""project2_notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gw9GrzSfj4JJpe54BIeSpuR2sd3LVlNQ

# Data Loading

Import library-library yang akan digunakan
"""

# Import library
import pandas as pd
import numpy as np
import tensorflow as tf

"""Load dataset dari file csv dan tampilkan dengan pandas dataframe"""

# Membaca dataset
 
df = pd.read_csv("/content/imdb_top_1000.csv")
df

"""Gunakan method .info() untuk melihat fitur-fitur pada dataset dan tipe datanya"""

df.info()

"""# Data Understanding dan Data Preparation

Karena sistem rekomendasi ini akan merekomendasikan film berdasarkan genrenya, maka fitur title harus unik. Cek berapa record judul film yang unik.
"""

len(df.Series_Title.unique())

"""Dari 1000 record dataset, ternyata ada 999 record dengan judul yang unik. Cek record mana saja yang judulnya tidak unik."""

df.loc[df['Series_Title'].duplicated() == True]

"""Terlihat ada 1 judul film yang redundant."""

df.loc[df['Series_Title'] == "Drishyam"]

"""Dari fakta di atas, dapat kita simpulkan bahwa film yang redundant ternyata adalah film yang memiliki remake version. Oleh karena itu, judul film tsb harus dipadupadankan dengan tahun rilisnya agar bisa menjadi unik. Kemudian, cek kembali jumlah value unik dari fitur Series_Title"""

for i in range(len(df.index)):
  if (df['Series_Title'] == "Drishyam")[i] == True:
    df["Series_Title"][i] = df['Series_Title'][i] + ' ' + df['Released_Year'][i]

len(df.Series_Title.unique())

"""Hapus semua fitur, kecuali Series_Title dan Genre, karena keduanya akan menjadi fitur pembentuk sistem rekomendasi."""

columns = df.columns.tolist()
wanted_columns = ["Series_Title", "Genre"]

for column in df.columns.tolist():
  if column in wanted_columns:
    columns.remove(column)

df = df.drop(columns=columns)
df

"""Cek missing value dan hapus jika ada"""

df.isnull().sum()

"""# Model Development

Lakukan proses transformasi fitur menggunakan TfidfVectorizer.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
 
# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()
 
# Melakukan perhitungan idf pada fitur Genre
tf.fit(df['Genre']) 
 
# Mapping array dari fitur index integer ke fitur Series_Title
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(df["Genre"]) 
 
# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan genre
# Baris diisi dengan judul film
 
pd.DataFrame(
    tfidf_matrix.todense(), 
    columns=tf.get_feature_names_out(),
    index=df.Series_Title
).sample(15, axis=1).sample(10, axis=0)

"""Gunakan cosine similarity untuk mengukur kemiripan antar film."""

from sklearn.metrics.pairwise import cosine_similarity
 
# Menghitung cosine similarity pada matrix tf-idf
cos_sim = cosine_similarity(tfidf_matrix) 
cos_sim

# Membuat dataframe dari variabel cos_sim dengan baris dan kolom berupa judul film
cos_sim_dataframe = pd.DataFrame(cos_sim, index=df['Series_Title'], columns=df['Series_Title'])
print('Shape:', cos_sim_dataframe.shape)
 
# Melihat similarity matrix untuk tiap film
cos_sim_dataframe.sample(6, axis=1).sample(10, axis=0)

def movie_recommendations(Series_Title, similarity_data=cos_sim_dataframe, features=df[["Series_Title", "Genre"]], n=10):
    """
    Rekomendasi Film berdasarkan kemiripannya
 
    Parameter:
    ---
    Series_Title : tipe data string (str)
                   judul film (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan film sebagai 
                      indeks dan kolom
    features : tipe data pd.DataFrame (object)
               Mengandung fitur-fitur yang digunakan untuk mendefinisikan kemiripan
    n : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    """
 
 
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,Series_Title].to_numpy().argpartition(
        range(-1, -n, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    nearest = similarity_data.columns[index[-1:-(n+2):-1]]
    
    # Drop nama_resto agar nama resto yang dicari tidak muncul dalam daftar rekomendasi
    nearest = nearest.drop(Series_Title, errors='ignore')
 
    return pd.DataFrame(nearest).merge(features).head(n)

"""# Evaluation

Metrik evaluasi yang relevan untuk sistem rekomendasi seperti ini adalah presisi. Presisi pada proyek ini mengukur banyaknya film hasil rekomendasi yang genrenya relevan dengan genre film masukan. Untuk mempermudah penggunaan berulang, fungsi precision di buat sebagai berikut.
"""

def precision(Series_Title):
  """
    Tingkat presisi sistem rekomendasi
 
    Parameter:
    ---
    Series_Title : tipe data string (str)
                   judul film yang ingin dicari hasil rekomendasinya
    """
  mr_df = movie_recommendations(Series_Title)
  target_genre = df[df["Series_Title"] == Series_Title]["Genre"].tolist()
  target_genre = target_genre[0]
  true_counter = 0
  
  for name in mr_df["Genre"].tolist():
    if name == target_genre:
      true_counter += 1
  
  precision = (true_counter/mr_df.shape[0]) * 100
  print("Tingkat presisi sistem rekomendasi dari film {}: {}%".format(Series_Title, int(precision)))

"""Mencari film yang mirip dan direkomendasikan setelah film X: First Class, serta menghitung tingkat presisinya."""

df[df.Series_Title.eq('X: First Class')]

movie_recommendations('X: First Class')

precision("X: First Class")

"""Mencari film yang mirip dan direkomendasikan setelah film The Kid, serta menghitung tingkat presisinya."""

df[df.Series_Title.eq('The Kid')]

movie_recommendations('The Kid')

precision("The Kid")