# Laporan Proyek Machine Learning - Ahmad Rizky #

## Domain Proyek ##
Masalah yang diangkat pada proyek ini berada pada domain **Kesehatan**. Menurut Riskesdas dalam Delima et al. (2016), stroke adalah penyakit penyebab kematian tertinggi di Indonesia, yaitu sebesar 15,4%. Oleh karena itu, diagnosis stroke sedari dini penting untuk dilakukan. Proyek ini mencoba untuk melakukan diagnosis stroke berdasarkan riwayat diri dan kesehatan pasien, seperti pekerjaan, tempat tinggal, level glukosa dalam darah, dan komorbid lainnya.

## Business Understanding ##
### Problem Statement ###
"Bagaimana cara diagnosis penyakit stroke menggunakan pendekatan Machine Learning?"
### Goal ###
"Pembuatan model dengan pendekatan Machine Learning untuk diagnosis penyakit stroke."
### Solution Statements ###
- Membuat 2 model dari pendekatan Machine Learning untuk diagnosis penyakit stroke
- Mengevaluasi model terbaik dengan membandingkan nilai fittingn score dan accuracy dari tiap model. Metrik accuracy menjadi ***satisficing metric*** dan metrik fitting score menjadi ***optimizing metric***

## Data Understanding ##
Dataset yang digunakan dalam proyek ini adalah [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset). Dataset ini sudah cukup bersih, tetapi memiliki 201 missing value pada fitur bmi.
### Fields pada Dataset ###
Dataset ini berisi 5110 record dengan 12 field. Gambar rangkuman mengenai dataset: <br>
![dataset_info](https://user-images.githubusercontent.com/99194827/169442588-e9af7f43-1b48-4502-9300-85179f33215f.png) <br><br>
Field yang ada pada dataset ini adalah:
- id <br>
  isi: primary key untuk tiap record sebagai unique identifier <br>
  tipe: integer
- gender <br>
  isi: jenis kelamin pasien <br>
  distinct value: Male berarti Pria, Female berarti Wanita, Other berarti tidak diketahui <br>
  tipe: string
- age <br>
  isi: usia pasien <br> 
  tipe: float
- hypertension <br>
  isi: status penyakit daerah tinggi pasien <br>
  distinct value: 0 berarti tidak, 1 berarti iya <br>
  tipe: boolean
- heart_disease <br>
  isi: status penyakit hati pasien <br>
  distinct value: 0 berarti tidak, 1 berarti iya <br>
  tipe: boolean
- ever_married <br>
  isi: status perkawinan pasien <br>
  distinct value: Yes berarti pernah, No berarti belum pernah <br>
  tipe: string
- work_type <br>
  isi: pekerjaan pasien <br>
  distinct value: children berarti anak-anak, Govt_job berarti pekerja pemerintahan, Never worked berarti belum pernah bekerja, Private berarti pekerja swasta, Self-employed berarti pekerja bebas atau pengusaha <br>
  tipe: string
- Residence_type <br>
  isi: tempat tinggal pasien <br>
  distinct value: Rural berarti desa, Urban berarti kota <br>
  tipe: string
- avg_glucose_level <br>
  isi: rerata kadar glukosa dalam darah pasien <br>
  tipe: float
- bmi <br>
  isi: indeks massa tubuh <br>
  tipe: float
- smoking_status <br>
  isi: hubungan rokok dengan pasien <br>
  distinct value: formerly smoked berarti pernah merokok tapi sudah berhenti, never smoked berarti tidak pernah merokok, smokes berarti aktif merokok, unknown berarti tidak diketahui <br>
  tipe: string
- stroke <br>
  isi: field target, status stroke pasien <br>
  distinct value: 0 berarti tidak, 1 berarti iya <br>
  tipe: boolean
### Tahapan Data Understanding ###
Tahap-tahap yang dilakukan dalam memahami data, adalah:
- melihat deskripsi statistik dari dataset <br>
  ![dataset_statistics](https://user-images.githubusercontent.com/99194827/169442667-22cf9254-7e30-46f5-a8c1-96b8b76a1037.png) <br>
  Dari deskripsi statistik di atas, nampak fitur avg_glucose_level dan bmi memiliki nilai maksimum yang jauh dari nilai kuartil atasnya, sehingga terindikasi ada outlier.
- memvisualisasikan fitur numerik menggunakan boxplot <br>
  Gambar Boxplot fitur avg_glucose_level: <br>
  ![boxplot_avg_glucose_level_before](https://user-images.githubusercontent.com/99194827/169442866-d5c657d2-3a1e-4cbe-88a6-e3021c1a253d.png) <br>
  Ada outlier terdeteksi. <br><br>
  Gambar Boxplot fitur bmi: <br>
  ![boxplot_bmi_before](https://user-images.githubusercontent.com/99194827/169442891-33919aa1-232c-4b9b-901c-c45831b720cc.png) <br>
  Outlier sangat jelas terlihat.
- memvisualisasikan fitur kategorik menggunakan barplot <br>
  Gambar Barplot fitur gender: <br>
  ![barplot_gender](https://user-images.githubusercontent.com/99194827/169442910-c2c15298-290c-4d1a-b8d6-abb99fbd2524.png) <br>
  Ada 3 unique value pada fitur ini. Value other tidak memberikan insight berguna untuk proyek, karena sulit menjelaskan pengaruh jenis kelamin yang tidak diketahui terhadap diagnosis stroke. <br><br>
  Gambar Barplot fitur ever_married: <br>
  ![barplot_ever_married](https://user-images.githubusercontent.com/99194827/169442933-1c9f6421-9f02-4bea-8cc0-ef789424e848.png) <br>
  Ada 2 unique value pada fitur ini. <br><br>
  Gambar Barplot fitur work_type: <br>
  ![barplot_work_type](https://user-images.githubusercontent.com/99194827/169442947-436dcea5-32dd-494e-9666-bdb3016a2be6.png) <br>
  Ada 5 unique value pada fitur ini. <br><br>
  Gambar Barplot fitur Residence_type: <br>
  ![barplot_residence_type](https://user-images.githubusercontent.com/99194827/169442963-9c1a122c-946b-40cc-9ca8-ee960e57197a.png) <br>
  Ada 2 unique value pada fitur ini. <br><br>
  Gambar Barplot fitur smoking_status: <br>
  ![barplot_smoking_status](https://user-images.githubusercontent.com/99194827/169442981-df48ee1b-9caf-40b5-a193-a4245d221904.png) <br>
  Ada 3 unique value pada fitur ini. Value unknown tidak memberikan insight berguna untuk proyek, karena sulit menjelaskan pengaruh merokok yang tidak diketahui terhadap diagnosis stroke.
- memvisualisasikan korelasi fitur kategorik dengan fitur target menggunakan catplot <br>
  Gambar Catplot fitur stroke vs fitur gender: <br>
  ![catplot_gender](https://user-images.githubusercontent.com/99194827/169443024-0db4b527-9c9b-4b62-907e-2dfebac7692a.png) <br>
  Rerata risiko stroke pada male dan female tidak jauh berbeda, sehingga dapat dikatakan fitur gender kurang memengaruhi fitur stroke. <br><br>
  Gambar Catplot fitur stroke vs fitur ever_married: <br>
  ![catplot_ever_married](https://user-images.githubusercontent.com/99194827/169443045-dadbd14d-3230-4b28-a07f-e382d03e2777.png) <br>
  Rerata risiko stroke pada pasien yang belum dan sudah menikah terlihat jauh berbeda, artinya fitur ever_married memengaruhi fitur stroke. <br><br>
  Gambar Catplot fitur stroke vs fitur work_type: <br>
  ![catplot_work_type](https://user-images.githubusercontent.com/99194827/169443079-ff1e5b0b-c2d5-4cc5-bfc5-37b1fa56dcbb.png) <br>
  Rerata risiko stroke pada tiap kategori pekerjaan terlihat bervariasi, artinya fitur work_type memengaruhi fitur stroke. <br><br>
  Gambar Catplot fitur stroke vs fitur Residence_type: <br>
  ![catplot_residence_type](https://user-images.githubusercontent.com/99194827/169443113-21de49a1-8bb4-49aa-85f6-7183ebdcecdb.png) <br>
  Rerata risiko stroke pada pasien yang tinggal di rural dan urban tidak jauh berbeda, sehingga dapat dikatakan fitur residence_type kurang memengaruhi fitur stroke. <br><br>
  Gambar Catplot fitur stroke vs fitur smoking_status: <br>
  ![catplot_smoking_status](https://user-images.githubusercontent.com/99194827/169443153-6c7cd720-aeb1-4a8d-bbfe-27518277380a.png) <br>
  Rerata risiko stroke pada tiap kategori status merokok terlihat bervariasi, artinya fitur smoking_status memengaruhi fitur stroke.
- memvisualisasikan korelasi fitur numerik dengan fitur target menggunakan heatmap <br>
  Gambar Heatmap fitur numerik: <br>
  ![heatmap](https://user-images.githubusercontent.com/99194827/169443172-55adf28d-b9f7-47a4-8705-39205b1cf2f0.png) <br>
  Koefisien korelasi fitur bmi dan avg_glucose_level terhadap fitur stroke sangat kecil (<0.05), sehingga dua fitur ini dapat dikatakan kurang memengaruhi fitur stroke.

## Data Preparation ##
Tahap-tahap yang dilakukan dalam data preparation, adalah:
### Data Cleaning ###
Beberapa hal yang dilakukan pada tahap ini, adalah:
- Fitur id dihapus <br>
  Hal ini dilakukan karena fitur id hanya berisi primary key (identifier unik) yang tidak akan memengaruhi diagnosis stroke.
- Missing value dihapus <br>
  Missing value dideteksi dengan metode .info() dan dihapus dengan metode .dropna().
- Outlier dihapus <br>
  Outlier dideteksi di visualisasi boxplot terhadap fitur-fitur numerik. Melalui visualisasi boxplot yang telah dilakukan sebelumnya, fitur avg_glucose_level dan bmi terdeteksi memiliki outlier. Outlier-outlier tersebut dihapus menggunakan metode IQR, dengan IQR adalah selisih antara kuartil atas dan kuartil bawah. x dikatakan sebagai outlier apabila memenuhi:
  ```
  x < Q1 - 1.5*IQR atau x > Q3 + 1.5*IQR
  
  ```
  Gambar boxplot fitur avg_glucose_level sebelum dan sesudah handling outlier: <br>
  ![boxplot_avg_glucose_level_before](https://user-images.githubusercontent.com/99194827/169443367-a5fa02c3-359e-4ebf-bcaa-a59c627d88c6.png)
  ![boxplot_avg_glucose_level_after](https://user-images.githubusercontent.com/99194827/169443372-15576a1f-e7c5-4617-8629-2a7ef80d7460.png) <br><br>
  Gambar boxplot fitur bmi sebelum dan sesudah handling outlier: <br>
  ![boxplot_bmi_before](https://user-images.githubusercontent.com/99194827/169443477-61410c9d-76f9-4637-8208-c12e9e5a1ee5.png)
  ![boxplot_bmi_after](https://user-images.githubusercontent.com/99194827/169443490-31a4b6be-edf6-46fd-a46d-2471e7c25f9f.png)

### Feature Selection ###
Beberapa hal yang dilakukan pada tahap ini, adalah:
- Kategori yang tidak memberikan insight berguna dari tiap fitur kategorik dihapus <br>
  Setelah melakukan visualisasi barplot dari tiap fitur kategorik, distinct value beserta jumlah data untuk tiap value dapat diketahui. Kategori other dari fitur gender dan unknown dari fitur smoking_status dihapus, karena tidak memberikan insight yang berguna terhadap proyek.
- Fitur kategorik yang tidak berpengaruh terhadap fitur stroke dihapus <br>
  Fitur kategorik dikatakan tidak berpengaruh terhadap fitur stroke jika rerata risiko stroke terhadap kategori dari suatu fitur kategorik relatif sama. Untuk memudahkan pembandingan kriteria ini, visualisasi catplot digunakan. Dilihat dari catplot yang telah dibuat, fitur kategorik yang tidak memenuhi persyaratan ini adalah fitur gender dan residence_type, sehingga kedua fitur tersebut dihapus.
- Fitur numerik yang tidak berpengaruh terhadap fitur stroke dihapus <br>
  Fitur numerik dikatakan tidak berpengaruh terhadap fitur stroke jika koefisien korelasinya bernilai kurang dari 0.05. Untuk memudahkan pembandingan kriteria ini, visualisasi heatmap digunakan. Dilihat dari heatmap yang telah dibuat, fitur numerik yang tidak memenuhi persyaratan ini adalah fitur avg_glucose_level dan bmi, sehingga kedua fitur dihapus.
### Data Transform ###
Beberapa hal yang dilakukan pada tahap ini, adalah:
- Label Encoding <br>
  Metode label encoding yang digunakan adalah One Hot Encoding. Dengan menggunakan metode ini, fitur kategorik diubah menjadi data kuantitatif, sehingga data dapat digunakan untuk pembelajaran model. Data dari satu fitur akan digenerasi menjadi fitur-fitur dengan jumlah setara dengan jumlah distinct value dari fitur tersebut. <br>
  Gambar Fitur ever_married sebelum encoding <br>
  ![ever_married_before](https://user-images.githubusercontent.com/99194827/169443657-e97ee74b-1f82-475b-8e1b-09af999ed4c1.png) <br><br>
  Gambar Fitur ever_married setelah encoding <br>
  ![ever_married_after](https://user-images.githubusercontent.com/99194827/169443675-201220f9-231d-4a43-840c-591b3fd13103.png)
- Split dataset <br>
  Dataset dibagi menjadi data training dan testing dengan rasio 80:20. Angka ini dipilih, karena rasio ini rasio yang cukup mengingat dataset tidak terlalu besar. Parameter stratify didefinisikan setara dengan fitur target, agar proporsi label pada data train dan test setara dengan proporsi label pada dataset keseluruhan.
- Normalisasi <br>
  Normalisasi mengubah nilai dari suatu fitur menjadi berada pada rentang 0 hingga 1. Sebuah nilai akan ditampilkan sebagai rasio antara selisih nilai tersebut dengan nilai minimal fitur dan selisih nilai maksimal dengan nilai minimal fitur, sebagai berikut. <br>
  ![Normalisasi](https://www.oreilly.com/library/view/regression-analysis-with/9781788627306/assets/ffb3ac78-fd6f-4340-aa92-cde8ae0322d6.png)


## Modeling ##
Model yang digunakan dalam proyek ini ada 2, yaitu KNN dan Random Forest.
- Model KNN melakukan klasifikasi dari suatu nilai dengan melihat klasifikasi dari titik-titik yang dekat dengan nilai tersebut. Kedekatan titik-titik data dengan suatu nilai diukur dengan formula jarak euclidean. Parameter n_neighbors mendefinisikan jumlah titik terdekat yang memengaruhi klasifikasi suatu nilai. Pada proyek ini, parameter n_neighbors yang digunakan adalah 5. Artinya, klasifikasi suatu nilai bergantung pada klasifikasi dari 5 titik data terdekat dari nilai tersebut. Apabila 3 titik data terdekat diklasifikasikan sebagai kategori 1, maka nilai tersebut akan diklasifikasikan sebagai kategori 1 juga. Nilai n_neighbors tersebut dipilih agar waktu training tidak terlalu lama. <br>
  KNN memiliki kelebihan, yaitu sangat mudah untuk diterapkan. Sementara itu, kekurangan dari KNN adalah KNN kurang bekerja baik pada dataset besar dengan dimensi data yang besar serta membutuhkan normalisasi/standardisasi.
- Model Random Forest melakukan klasifikasi dengan bantuan decision tree. Decision tree sendiri adalah metode klasifikasi suatu nilai dengan menanyakan pertanyaan-pertanyaan bertingkat mengenai kategori dari nilai tersebut. Hasil akhir dari decision tree adalah kategori klasifikasi dari nilai. Random Forest adalah metode klasifikasi yang menggabungkan hasil klasifikasi dari beberapa decision tree. Pada proyek ini, parameter n_estimators yang digunakan adalah 50. Artinya, klasifikasi suatu nilai bergantung pada klasifikasi dari 50 decision tree. Apabila 51 decision tree mengklasifikasikan nilai sebagai kategori 1, maka nilai tersebut akan diklasifikasikan sebagai kategori 1. Nilai n_estimators tersebut dipilih agar waktu training tidak terlalu lama. <br>
  Random Forest memiliki kelebihan, yaitu tidak memerlukan normalisasi/standardisasi. Sementara itu, kekurangan dari Random Forest adalah membutuhkan waktu training lebih lama. <br>

Melalui metrik-metrik evaluasi yang digunakan, model terbaik untuk diagnosis stroke adalah model KNN. Hal ini dikarenakan nilai accuracy untuk model KNN dan Random Forest sudah memenuhi kriteria (>90%) dan besar nilai fitting_score (tanpa memerhatikan tanda) dari model KNN lebih kecil.

## Evaluation ##
Metrik evaluasi yang digunakan ada 2, yaitu Fitting Score dan Accuracy. Metrik accuracy menjadi satisficing metric dan metrik fitting score menjadi optimizing metric.
- Metrik Fitting Score adalah selisih antara nilai MSE pada data testing dengan MSE pada data training. Metrik ini menggambarkan jenis fitting data yang terjadi. MSE mengukur rerata dari kuadrat dari selisih antara hasil prediksi dengan data sebenarnya. Model dengan besar fitting score (tanpa memerhatikan tanda) paling rendah adalah model yang baik. <br>
  Gambar 17 Formula MSE: <br>
  ![MSE](https://vedexcel.com/wp-content/uploads/2020/12/MSE_Python.gif)
- Metrik Accuracy diterapkan untuk menentukan akurasi model. Accuracy menghitung rasio antara jumlah prediksi yang benar (True Positive dan True Negative) dengan jumlah data testing. Model dengan accuracy >90% sudah dikatakan baik pada proyek ini.
  Gambar 18 Formula Accuracy: <br>
  ![Accuracy](https://th.bing.com/th/id/OIP.XsegOFaHxkbrh5kIHoHn2wHaBX?pid=ImgDet&rs=1) <br>

Melalui metrik-metrik evaluasi yang digunakan, model terbaik untuk diagnosis stroke adalah model KNN. Hal ini dikarenakan nilai accuracy untuk model KNN dan Random Forest sudah memenuhi kriteria (>90%) dan besar nilai fitting_score (tanpa memerhatikan tanda) dari model KNN lebih kecil. <br>
![evaluation](https://user-images.githubusercontent.com/99194827/169443755-64a00f3b-8b2e-4016-b7ea-449d326d3fa3.png)

## Referensi ##
Delima, Mihardja LK, Ghani L. 2016. Faktor risiko dominan penderita stroke di indonesia. Buletin Penelitian Kesehatan. 44 (1): 49-58. doi: 10.22435/bpk.v44i1.4949.49-58
