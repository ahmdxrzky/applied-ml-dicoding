# Laporan Proyek Machine Learning - Ahmad Rizky #

## Project Overview ##
Masalah yang diangkat pada proyek ini berada pada domain **Rekomendasi Film**. Tingginya tingkat stress manusia, terutama mereka yang tinggal di kota, menuntut orang-orang untuk dapat menghibur diri sendiri. Salah satu sarana penghiburan mandiri di kala pandemi adalah menonton film. Akan tetapi, ada banyak sekali film saat ini dan ditawarkan dalam berbagai macam genre. Oleh karena itu, sistem rekomendasi film patut untuk dibuat. Proyek ini mencoba untuk membuat sistem rekomendasi berdasarkan genre film.

## Business Understanding ##
### Problem Statement ###
"Bagaimana cara membuat sistem rekomendasi film menggunakan pendekatan Machine Learning?"
### Goal ###
"Pembuatan model dengan pendekatan Machine Learning sebagai sistem rekomendasi film."
### Solution Statements ###
Mengukur kemiripan antar film menggunakan pendekatan ***Content-based Filtering***.

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
  Terlihat bahwa 1 film bisa memiliki 1 atau lebih genre.

## Data Preparation ##
Tahap-tahap yang dilakukan dalam data preparation, adalah:
### Data Cleaning ###
Beberapa hal yang dilakukan pada tahap ini, adalah:
- membuat data pada fitur Series_Title unik <br>
  Sebelumnya telah diketahui bahwa ada 1 record redundant di fitur Series_Title. <br>
  ![redundant_data](https://user-images.githubusercontent.com/99194827/169694243-e623d06d-b128-4f18-a0b6-28f63303c4ec.png) <br>
  Data redundant terjadi, karena film tersebut diremake pada tahun yang berbeda. Oleh karena itu, khusus untuk film ini, data Series_Title-nya dipadukan dengan tahun rilisnya.
- cek missing value <br>
  ![missing_value](https://user-images.githubusercontent.com/99194827/169694503-639622f4-2ea6-4367-b573-1e0471850c62.png)
### Feature Selection ###
Hal yang dilakukan pada tahap ini, adalah:
menghapus fitur yang tidak digunakan dalam sistem rekomendasi <br>
![fitur rekomendasi](https://user-images.githubusercontent.com/99194827/169694415-67041554-b130-4f64-846e-e234e58149e1.png)

## Modeling and Results ##
Beberapa hal yang dilakukan pada tahap ini, adalah:
- Konversi data dari fitur Genre ke dalam bentuk vektor <br>
  Proses ini dilakukan dengan kelas tfidfvectorizer. Tiap judul film bisa memiliki 1 atau lebih genre, sehingga tiap film dapat direpresentasikan sebagai vektor dengan jumlah dimensi setara dengan jumlah genre. Kelas tfidfvectorizer akan memberikan bobot untuk tiap genre bagi tiap film. <br>
  ![tfidfvectorizer](https://user-images.githubusercontent.com/99194827/169762446-102cd00c-a41a-4f23-beb2-bd86a9b1af5e.png)
- Menghitung kemiripan antar film menggunakan perhitungan Cosine Similarity <br>
  Setelah data divektorisasi, maka kedekatan antar data diukur menggunakan cosine similarity. Prinsip ini didasarkan pada fakta bahwa dua titik yang dekat dapat diasumsikan sebagai titik-titik ujung dari dua vektor yang saling terpisah oleh sudut yang kecil. Persamaan yang digunakan adalah: <br>
  ![Cosine_Similarity](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a4c9a778656537624a3303e646559a429868863) <br><br>
  Kemiripan antar 2 film dapat diwakili oleh similarity index yang didapatkan dari perhitungan di atas, nampak pada gambar di bawah: <br>
  ![image](https://user-images.githubusercontent.com/99194827/169797215-b30732cf-e132-4dd2-bf2e-b316cffc6033.png) <br>
Hasil dari modelling ini adalah:
sistem rekomendasi film dalam bentuk fungsi yang akan menampilkan 10 film dengan similarity index paling tinggi dengan film masukan. Proses ini mengurutkan 10 besar film dengan similarity index tertinggi relatif terhadap film masukan. <br>
![image](https://user-images.githubusercontent.com/99194827/169797415-0610fa31-d397-4ad5-9602-9f4befb1ce8e.png)

## Evaluation ##
Metrik evaluasi yang relevan untuk sistem rekomendasi ini adalah presisi. Presisi menghitung tingkat kesamaan genre film-film hasil luaran dengan genre film masukan. Formula metrik presisi untuk sistem rekomendasi, adalah sebagai berikut: <br>
![image](https://user-images.githubusercontent.com/99194827/169797046-60a9f49e-d008-4300-a2bd-2f255483f905.png) <br><br>
Pada proyek ini, metrik presisi diwujudkan dalam bentuk fungsi bernama precision dengan parameter berupa string dari judul film yang ingin dicari rekomendasinya. <br><br>
Tingkat presisi hasil rekomendasi film The Kid: <br>
![the_kid_precision](https://user-images.githubusercontent.com/99194827/169796003-3ed3ee0f-a4b0-452b-b9c6-2ee14140711b.png)
