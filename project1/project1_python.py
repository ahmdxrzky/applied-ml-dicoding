# -*- coding: utf-8 -*-
"""project1_notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kVt5aoKlfKpaWAY7ZivOVPZXPOTlH1Gh

# Data Loading

Sebelum mengeksplorasi data, import terlebih dahulu library-library dasar yang akan digunakan dalam visualisasi dan eksplorasi data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Import dataset dari file berformat csv dan tampilkan menggunakan Pandas Dataframe."""

stroke_dataset = pd.read_csv('/content/healthcare-dataset-stroke-data.csv')
stroke_dataset = pd.DataFrame(stroke_dataset)
stroke_dataset

"""Gunakan method info() untuk mendapatkan gambaran mengenai jumlah field, record, dan tipe data tiap field."""

stroke_dataset.info()

"""# Data Handling - Missing Value

Karena fitur id hanya berisi primary key atau identifier unik dari dataset, maka fitur ini jelas tidak akan berpengaruh pada status stroke pasien. Fitur id dihapus dan ukuran fitur dataset berkurang 1.
"""

stroke_dataset.drop(['id'], inplace=True, axis=1)
stroke_dataset.shape

"""Melalui rangkuman dataset yang telah diketahui sebelumnya, kita dapat mengetahui adanya missing value pada fitur bmi. Hapus semua missing value dan ukuran record dataset berkurang 201."""

stroke_dataset = stroke_dataset.dropna()
stroke_dataset = stroke_dataset.reset_index(drop=True)
stroke_dataset.shape

"""# Data Handling - Outliers

Gunakan method describe() dengan parameter include diatur sama dengan all agar deskripsi statistik dari seluruh fitur dapat ditampilkan, baik fitur numerik ataupun kategorik.
"""

stroke_dataset.describe(include = "all")

"""Dari deskripsi statistik di atas, fitur avg_glucose_level dan bmi nampak memiliki nilai maksimal yang sangat jauh dari kuartil atasnya (terindikasi ada outlier). Kita lakukan eksplorasi visual fitur numerik untuk mendeteksi keberadaan outlier."""

sns.boxplot(x=stroke_dataset['avg_glucose_level'])

sns.boxplot(x=stroke_dataset['bmi'])

"""Boxplot dari fitur avg_glucose_level dan bmi menunjukkan adanya outlier. Kita gunakan metode IQR untuk menghilangkan outlier."""

Q1 = stroke_dataset["avg_glucose_level"].describe()['25%']
Q3 = stroke_dataset["avg_glucose_level"].describe()['75%']
IQR = Q3 - Q1
stroke_dataset = stroke_dataset.loc[(stroke_dataset[['avg_glucose_level']] < Q3+1.5*IQR).all(axis=1)]
stroke_dataset.shape

Q1 = stroke_dataset["bmi"].describe()['25%']
Q3 = stroke_dataset["bmi"].describe()['75%']
IQR = Q3 - Q1
stroke_dataset = stroke_dataset.loc[(stroke_dataset[['bmi']] < Q3+1.5*IQR).all(axis=1)]
stroke_dataset.shape

"""Visualisasi boxplot kembali untuk dua fitur tersebut untuk melihat apakah outlier sudah berhasil dibersihkan."""

sns.boxplot(x=stroke_dataset['avg_glucose_level'])

sns.boxplot(x=stroke_dataset['bmi'])

"""# Data Handling - Univariate Analysis

Kelompokkan fitur-fitur kategorik dan numerik dari dataset.
"""

kategorik = ["gender", "ever_married", "work_type", "Residence_type", "smoking_status"]
numerik = ["age", "hypertension", "heart_disease", "avg_glucose_level", "bmi"]

"""Visualisasikan jumlah record per tiap distinct value dari fitur gender."""

fitur = kategorik[0]
count = stroke_dataset[fitur].value_counts()
visual_dataframe = pd.DataFrame({'jumlah data':count})
print(visual_dataframe)
count.plot(kind='bar', title=fitur)

"""Karena gender unknown tidak akan memberikan insight yang baik terhadap studi ini, maka record tersebut dihapus dan ukuran record dataset berkurang 1."""

stroke_dataset = stroke_dataset.loc[(stroke_dataset["gender"] != "Other")]
stroke_dataset.shape

"""Visualisasikan jumlah record per tiap distinct value dari fitur ever_married, work_type, dan Residence_type untuk melihat apa saja unique value yang dimiliki tiap fitur.


"""

fitur = kategorik[1]
count = stroke_dataset[fitur].value_counts()
visual_dataframe = pd.DataFrame({'jumlah data':count})
print(visual_dataframe)
count.plot(kind='bar', title=fitur)

fitur = kategorik[2]
count = stroke_dataset[fitur].value_counts()
visual_dataframe = pd.DataFrame({'jumlah data':count})
print(visual_dataframe)
count.plot(kind='bar', title=fitur)

fitur = kategorik[3]
count = stroke_dataset[fitur].value_counts()
visual_dataframe = pd.DataFrame({'jumlah data':count})
print(visual_dataframe)
count.plot(kind='bar', title=fitur)

"""Visualisasikan jumlah record per tiap distinct value dari fitur smoking_status."""

fitur = kategorik[4]
count = stroke_dataset[fitur].value_counts()
visual_dataframe = pd.DataFrame({'jumlah data':count})
print(visual_dataframe)
count.plot(kind='bar', title=fitur)

"""Karena smoking_status unknown tidak akan memberikan insight yang baik terhadap studi ini, maka record tersebut dihapus dan ukuran record dataset berkurang 1482."""

stroke_dataset = stroke_dataset.loc[(stroke_dataset["smoking_status"] != "Unknown")]
stroke_dataset.shape

"""# Data Handling - Multivariate Analysis

Lakukan analisis multivariat dari seluruh fitur kategorik terhadap fitur stroke untuk melihat pengaruh tiap fitur terhadap fitur stroke menggunakan barplot.
"""

fitur_kategorik = stroke_dataset.select_dtypes(include='object').columns.to_list()
 
for col in fitur_kategorik:
  sns.catplot(x=col, y="stroke", kind="bar", dodge=False, height = 4, aspect = 3,  data=stroke_dataset, palette="Blues")
  plt.title("Rerata risiko Stroke terhadap tiap kategori pada fitur {}".format(col))

"""Karena rerata risiko stroke dari tiap kelompok pada fitur gender dan Residence_type relatif setara, maka dua fitur ini dapat dihapus. Fitur dataset berkurang 2."""

stroke_dataset.drop(["gender", "Residence_type"], inplace=True, axis=1)
kategorik.remove("gender")
kategorik.remove("Residence_type")
stroke_dataset.shape

"""Lakukan analisis multivariat dari seluruh fitur numerik menggunakan heatmap."""

plt.figure(figsize=(10, 8))
correlation_matrix = stroke_dataset.corr().round(2)
 
# Untuk mencetak nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=1, )
plt.title("Matriks Korelasi Fitur-Fitur Numerik", size=20)

"""Karena skor korelasi antara fitur bmi dengan stroke negatif, maka fitur bmi dapat dihapus. Fitur dataset berkurang 2."""

stroke_dataset.drop(['avg_glucose_level', 'bmi'], inplace=True, axis=1)
numerik.remove("bmi")
numerik.remove("avg_glucose_level")
stroke_dataset.shape

"""# Data Preparation"""

stroke_dataset

"""Agar fitur kategorik dapat dipelajari oleh model, lakukan OneHotEncoding. Encoding jenis ini membantu melabeli kategori dari tiap fitur tanpa memberikan peringkat bahwa 1 kategori lebih baik dari kategori lain."""

from sklearn.preprocessing import OneHotEncoder
stroke_dataset = pd.concat([stroke_dataset, pd.get_dummies(stroke_dataset[kategorik[0]], prefix=kategorik[0])],axis=1)
stroke_dataset = pd.concat([stroke_dataset, pd.get_dummies(stroke_dataset[kategorik[1]], prefix=kategorik[1])],axis=1)
stroke_dataset = pd.concat([stroke_dataset, pd.get_dummies(stroke_dataset[kategorik[2]], prefix=kategorik[2])],axis=1)
stroke_dataset.drop([kategorik[0], kategorik[1], kategorik[2]], axis=1, inplace=True)
stroke_dataset

"""Split dataset untuk training dan testing dengan rasio 80:20."""

from sklearn.model_selection import train_test_split
 
X = stroke_dataset.drop(["stroke"], axis =1)
y = stroke_dataset["stroke"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 123,
                                                    stratify = y)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""Lakukan normalisasi dengan StandardScaler agar nilai fitur numerik pada X_train dan X_test berada pada rentang [-1, 1]."""

# Normalization
from sklearn.preprocessing import MinMaxScaler

minmax = MinMaxScaler()
minmax.fit(X_train[numerik])
X_train[numerik] = minmax.transform(X_train.loc[:, numerik])
X_train[numerik]

X_test[numerik] = minmax.transform(X_test.loc[:, numerik])
X_test[numerik]

"""# Model Development

Import library-library yang akan digunakan pada model development, yaitu KNN, Random Forest, dan metrik-metrik evaluasi (MSE dan Accuracy). Metrik Fitting Score (selisih MSE pada data testing dan training) menjadi optimizing metric, sedangkan metrik accuracy menjadi satisficing metric.
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

# Siapkan dataframe untuk analisis model
models_table = pd.DataFrame(index=['train_mse', 'test_mse', 'fitting_score', 'accuracy'],
                            columns=['KNN', 'RandomForest'])

"""Pembuatan model KNN dengan jumlah neighbor yang memengaruhi prediksi adalah 5. Hitung metrik evaluasi untuk moodel ini."""

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
train_mse = mean_squared_error(y_true=y_train, y_pred=knn.predict(X_train)) * 100
test_mse = mean_squared_error(y_true=y_test, y_pred=knn.predict(X_test)) * 100
models_table.loc['train_mse','KNN'] = round(train_mse, 3)
models_table.loc['test_mse','KNN'] = round(test_mse, 3)
models_table.loc['fitting_score', 'KNN'] = round(test_mse-train_mse, 3)
models_table.loc['accuracy','KNN'] = round(accuracy_score(y_pred=knn.predict(X_test), y_true=y_test) * 100, 3)

"""Pembuatan model Random Forest dengan jumlah estimator adalah 50. Hitung metrik evaluasi untuk moodel ini."""

rf = RandomForestClassifier(n_estimators=50)
rf.fit(X_train, y_train)
train_mse = mean_squared_error(y_true=y_train, y_pred=rf.predict(X_train)) * 100
test_mse = mean_squared_error(y_true=y_test, y_pred=rf.predict(X_test)) * 100
models_table.loc['train_mse','RandomForest'] = round(train_mse, 3)
models_table.loc['test_mse','RandomForest'] = round(test_mse, 3)
models_table.loc['fitting_score', 'RandomForest'] = round(test_mse-train_mse, 3)
models_table.loc['accuracy','RandomForest'] = round(accuracy_score(y_pred=rf.predict(X_test), y_true=y_test) * 100, 3)

"""# Model Evaluation"""

models_table

"""Nilai accuracy untuk model KNN dan Random Forest sudah memenuhi kriteria (>90%). Nilai fitting_score (tanpa memerhatikan tanda) dari model KNN lebih kecil daripada model Random Forest.

Kesimpulan: model KNN adalah model terbaik untuk diagnosis stroke.
"""