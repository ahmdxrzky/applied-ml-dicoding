# Laporan Proyek Machine Learning - Ahmad Rizky #

## Domain Proyek ##
Masalah yang diangkat pada proyek ini berada pada domain **Rekomendasi Film**. Tingginya tingkat stress manusia, terutama mereka yang tinggal di kota, menuntut orang-orang untuk dapat menghibur diri sendiri. Salah satu sarana penghiburan mandiri di kala pandemi adalah menonton film. Akan tetapi, ada banyak sekali film saat ini dan ditawarkan dalam berbagai macam genre. Oleh karena itu, sistem rekomendasi film patut untuk dibuat. Proyek ini mencoba untuk membuat sistem rekomendasi berdasarkan genre film.

## Business Understanding ##
### Problem Statement ###
"Bagaimana cara membuat sistem rekomendasi film menggunakan pendekatan Machine Learning?"
### Goal ###
"Pembuatan model dengan pendekatan Machine Learning sebagai sistem rekomendasi film."
### Solution Statements ###
Mengukur kemiripan antar film menggunakan *jaccard similarity*

## Data Understanding ##
Dataset yang digunakan dalam proyek ini adalah [IMDB Movies Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows). Dataset ini memiliki banyak sekali missing value pada beberapa fitur, tetapi fitur-fitur tersebut tidak digunakan untuk sistem rekomendasi ini. 
### Fields pada Dataset ###
Dataset ini berisi 1000 record dengan 16 field. Gambar rangkuman mengenai dataset: <br>
![dataset_info](https://user-images.githubusercontent.com/99194827/169693379-45d791a5-28aa-445a-b5ae-1557e0a8bbe0.png) <br><br>
Field yang ada pada dataset ini adalah:
- Poster_Link <br>
  isi: tautan dari poster yang digunakan di website IMDB <br>
  tipe: string
- Series_Title <br>
  isi: judul film <br>
  tipe: string
- Released_Year <br>
  isi: tahun rilis film <br> 
  tipe: string
- Certificate <br>
  isi: batas usia penonton <br>
  tipe: string
- Runtime <br>
  isi: durasi film <br>
  tipe: string
- Genre <br>
  isi: genre film <br>
  tipe: string
- IMDB_Rating <br>
  isi: rating film di website IMDB <br>
  tipe: float
- Overview <br>
  isi: cerita pengantar film <br>
  tipe: string
- Meta_score <br>
  isi: skor yang didapatkan film <br>
  tipe: float
- Director <br>
  isi: nama sutradara <br>
  tipe: string
- Star1 <br>
  isi: nama aktor/aktris <br>
  tipe: string
- Star2 <br>
  isi: nama aktor/aktris <br>
  tipe: string
- Star3 <br>
  isi: nama aktor/aktris <br>
  tipe: string
- Star4 <br>
  isi: nama aktor/aktris <br>
  tipe: string
- No_of_Votes <br>
  isi: total pemberi skor (voters) <br>
  tipe: integer
- Gross <br>
  isi: pendapatan film <br>
  tipe: object
### Tahapan Data Understanding ###
Tahap-tahap yang dilakukan dalam memahami data, adalah:
- melihat jumlah data unik dari fitur Series_Title <br>
  ![fitur Series_Title](https://user-images.githubusercontent.com/99194827/169694015-9458cf21-0c3c-49af-b269-bcddb748fc64.png) <br>
  Dari gambar di atas, nampak fitur Series_Title memiliki 1 nilai redundant.
- melihat data dari fitur Genre <br>
  ![fitur Genre](https://user-images.githubusercontent.com/99194827/169694203-e3fbc5cc-78cf-4275-8529-0d1dc2e468bb.png) <br>
  Terlihat bahwa 1 film bisa memiliki lebih dari 1 genre.

## Data Preparation ##
Tahap-tahap yang dilakukan dalam data preparation, adalah:
### Data Cleaning ###
Beberapa hal yang dilakukan pada tahap ini, adalah:
- membuat data pada fitur Series_Title unik <br>
  Sebelumnya telah diketahui bahwa ada 1 record redundant di fitur Series_Title. <br>
  ![redundant_data](https://user-images.githubusercontent.com/99194827/169694243-e623d06d-b128-4f18-a0b6-28f63303c4ec.png) <br>
  Data redundant terjadi, karena film tersebut diremake pada tahun yang berbeda. Oleh karena itu, khusus untuk film ini, data Series_Title-nya dipadukan dengan tahun rilisnya.
- cek missing value
  ![missing_value](https://user-images.githubusercontent.com/99194827/169694503-639622f4-2ea6-4367-b573-1e0471850c62.png)
### Feature Selection ###
Beberapa hal yang dilakukan pada tahap ini, adalah:
mengekstrak fitur baru (First_genre) yang mewakili value pertama dari fitur Genre <br>
  ![First_genre](https://user-images.githubusercontent.com/99194827/169694342-f75dd97c-c774-4407-af5a-a250eb69a120.png)
- menghapus fitur yang tidak digunakan dalam sistem rekomendasi <br>
  ![fitur rekomendasi](https://user-images.githubusercontent.com/99194827/169694415-67041554-b130-4f64-846e-e234e58149e1.png)

## Modeling ##
Beberapa hal yang dilakukan pada tahap ini, adalah:
- Konversi data dari fitur First_genre ke dalam bentuk vektor <br>
  Proses ini dilakukan dengan fitur tfidfvectorizer. Vektor yang dihasilkan akan digunakan untuk mempermudah perhitungan kemiripan antar film.
- Menghitung kemiripan antar film menggunakan perhitungan Cosine Similarity <br>
  Setelah data divektorisasi, maka kedekatan antar data diukur menggunakan cosine similarity. Prinsip ini didasarkan pada fakta bahwa dua titik ujung vektor yang dekat adalah dua titik yang memiliki sudut terkecil. Persamaan yang digunakan adalah:
  ![Cosine_Similarity](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a4c9a778656537624a3303e646559a429868863)
- Mendefinisikan fungsi rekomendasi film yang akan menampilkan 10 film dengan similarity index paling tinggi dengan film yang diinput <br>
  Proses ini mengurutkan 10 besar film dengan similarity index tertinggi relatif terhadap film yang menjadi input atau masukan.

## Evaluation ##
Testing yang dilakukan adalah menggunakan fungsi rekomendasi kepada 2 film untuk ditampilkan 10 film yang memiliki similarity index tertinggi dengan masing-masing film. <br>
![first_class](https://user-images.githubusercontent.com/99194827/169695058-836ebc55-be8e-46be-bf9b-a13397752960.png) <br>
![the_kid](https://user-images.githubusercontent.com/99194827/169695118-33cf1d98-1881-4a58-bfe9-fbedcffa4c02.png)
