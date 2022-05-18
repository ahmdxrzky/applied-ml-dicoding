# Laporan Proyek Machine Learning - Ahmad Rizky #

## Domain Proyek ##
Masalah yang diangkat pada proyek ini berada pada domain Kesehatan. Menurut Riskesdas dalam Delima et al. (2016), stroke adalah penyakit penyebab kematian tertinggi di Indonesia, yaitu sebesar 15,4%. Oleh karena itu, diagnosis stroke sedari dini penting untuk dilakukan. Proyek ini mencoba untuk melakukan diagnosis stroke berdasarkan riwayat diri dan kesehatan pasien, seperti pekerjaan, tempat tinggal, level glukosa dalam darah, dan komorbid lainnya.

## Business Understanding ##
### Problem Statement ###
"Bagaimana cara diagnosis penyakit stroke menggunakan pendekatan Machine Learning?"
### Goal ###
"Pembuatan model dengan pendekatan Machine Learning untuk diagnosis penyakit stroke."
### Solution Statements ###
- Membuat 2 model dari pendekatan Machine Learning untuk diagnosis penyakit stroke
- Mengevaluasi model terbaik dengan membandingkan nilai mean squared error dan accuracy dari tiap model.

## Data Understanding ##
Dataset yang digunakan dalam proyek ini adalah Stroke Prediction Dataset. Dataset ini diunggah oleh akun kaggle dengan username Fedesoriano dan dapat diunduh pada tautan https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset.
### Fields pada Dataset ###
Dataset ini berisi 5110 record dengan 12 field. Field yang ada pada dataset ini adalah:
- id: primary key untuk tiap record
- gender: jenis kelamin pasien. Distinct value: Male, Female, and Other 
- age: usia pasien
- hypertension: apakah pasien memiliki penyakit darah tinggi? 0 berarti tidak, 1 berarti iya
- heart_disease: apakah pasien memiliki komorbid penyakit hati? 0 berarti tidak, 1 berarti iya
- ever_married: status perkawinan pasien. Distinct value: Yes and No
- work_type: status pekerjaan pasien. Distinct value: children, Govt_job, Never worked, Private, and Self-employed
- Residence_type: tempat tinggal pasien. Distinct value: Rural and Urban
- avg_glucose_level: rerata kadar glukosa dalam darah pasien
- bmi: indeks massa tubuh
- smoking_status: status pasien dengan rokok. Distinct value: formerly smoked, never smoked, smokes, unknown
- stroke: field target, status stroke pasien. 0 berarti tidak, 1 berarti iya
### Tahapan Data Understanding ###
Tahap-tahap yang dilakukan dalam memahami data, adalah:
- memvisualisasikan fitur numerik menggunakan boxplot
- memvisualisasikan fitur kategorik menggunakan barplot
- memvisualisasikan korelasi fitur kategorik dengan fitur target menggunakan barplot
- memvisualisasikan korelasi fitur numerik dengan fitur target menggunakan heatmap

## Data Preparation ##
Tahap-tahap yang dilakukan dalam data preparation, adalah:
- menghapus field id
- menghapus missing value
- menghapus outlier
- menghapus kategori yang tidak memberikan insight berguna dari sebuah fitur
- menghapus fitur kategorik yang tidak berpengaruh terhadap fitur target (fitur dengan rerata risiko stroke setara untuk tiap kategori)
- menghapus fitur numerik yang tidak berpengaruh terhadap fitur target (<0.1)
- OneHotEncode. Tahap ini adalah tahapan encode data dengan metode OneHotEncode. Fitur-fitur kategorik tentu tidak bisa langsung dimasukkan ke model untuk dipelajari, karena model hanya menerima data-data kuantitatif. Agar data kategorik berubah menjadi data kuantitatif, encoding harus dilakukan. Metode OneHotEncode digunakan, karena data kategorik yang diencoding adalah data nominal (tidak ada tingkatan).
5. Split dataset. Dataset dibagi menjadi data training dan testing dengan rasio 80:20. Angka ini dipilih, karena rasio ini rasio yang cukup melihat dataset yang tidak terlalu besar.
6. Normalisasi. Metode normalisasi yang digunakan adalah Min Max Scaler, yaitu normalisasi yang mengubah nilai menjadi berada pada rentang 0 hingga 1. Sebuah nilai akan ditampilkan sebagai rasio antara selisih nilai tersebut dengan nilai minimal terhadap selisih nilai maksimal dengan nilai minimal.

## Modeling ##
Model yang digunakan dalam proyek ini ada 2, yaitu KNN dan Random Forest. Model KNN menggunakan jumlah neighbors sebesar 5, sedangkan model Random Forest menggunakan jumlah estimator sebesar 100. Melalui metrik-metrik evaluasi yang digunakan dan juga telah dipaparkan di notebook, model terbaik untuk diagnosis stroke adalah model KNN. Hal ini dikarenakan nilai accuracy untuk model KNN lebih besar daripada model Random Forest. Metrik MSE agak sulit untuk digunakan, karena model KNN mengalami underfit dan model Random Forest mengalami overfit.

## Evaluation ##
Metrik evaluasi yang digunakan ada 2, yaitu Mean Squarred Error dan Accuracy.
1. Metrik MSE diterapkan pada data training dan testing untuk menentukan jenis fitting data yang terjadi. MSE mengukur rerata dari kuadrat dari selisih antara hasil prediksi dengan data sebenarnya. Model yang baik harus memiliki MSE pada data training dan testing yang tidak jauh berbeda.
2. Metrik Accuracy diterapkan untuk menentukan akurasi model. Accuracy menghitung rasio antara jumlah prediksi yang benar dengan jumlah data testing. Model yang baik tentunya memiliki nilai accuracy yang besar.

## Referensi ##
Delima, Mihardja LK, Ghani L. 2016. Faktor risiko dominan penderita stroke di indonesia. Buletin Penelitian Kesehatan. 44 (1): 49-58. doi: 10.22435/bpk.v44i1.4949.49-58
