# Stroke Diagnosis #

## Complete Script ##
Complete script for this project can be accessed [here](https://github.com/ahmdxrzky/applied-ml-dicoding/blob/main/project1/project1_notebook.ipynb).

## Project Domain ##
Problem being highlighted in this project is in **Health** domain. According to Riskesdas in Delima et al. (2016), stroke is the highest death-cause disease in Indonesia, which round on 15,4%. So, stroke early detection is important to be done. This project tries to do stroke diagnosis based on patient medical record, i.e. work field, neighborhood, glucose level in blood, and other comorbid disease.

## Business Understanding ##
### Problem Statement ###
"How to diagnose stroke with Machine Learning approach?"
### Goal ###
"Model making with Machine Learning approach to diagnose stroke."
### Solution Statements ###
- Make 2 models with Machine Learning approach to diagnose stroke
- Evaluate best model by compare fitting score and accuracy of each model. Accuracy become ***satisficing metric***, while fitting score become ***optimizing metric***

## Data Understanding ##
Dataset being used in this project is [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset). This dataset is clean enough, but it has 201 missing values in bmi feature.
### Dataset's Fields ###
This dataset contains 5110 records with 12 fields. Summary of the dataset based on its fields is shown below: <br>
![dataset_info](https://user-images.githubusercontent.com/99194827/169442588-e9af7f43-1b48-4502-9300-85179f33215f.png) <br><br>
Fields in this dataset are:
- id <br>
  content: unique identifier <br>
  type: integer
- gender <br>
  distinct value: Male, Female, and Other <br>
  type: string
- age <br>
  type: float
- hypertension <br>
  content: patient's status due to hypertension disease <br>
  distinct value: 0 means no, 1 means having the disease <br>
  type: boolean
- heart_disease <br>
  content: patient's status due to heart disease <br>
  distinct value: 0 means no, 1 means having the disease <br>
  type: boolean
- ever_married <br>
  content: patient's marriage status <br>
  distinct value: Yes means ever married, No means haven't married yet <br>
  type: string
- work_type <br>
  content: patient's work field <br>
  distinct value: children means underage (haven't get job ever), Govt_job means employee in public sector, Never worked means haven't worked yet even in the work age, Private means employee in private sector, Self-employed means freelance or business owner <br>
  type: string
- Residence_type <br>
  content: patient's neighborhood type <br>
  distinct value: Rural and Urban <br>
  type: string
- avg_glucose_level <br>
  content: average of glucose level in patient's blood <br>
  type: float
- bmi <br>
  type: float
- smoking_status <br>
  content: relationship between patient and cigarettes <br>
  distinct value: formerly smoked means have stopped from smoking, never smoked means haven't smoking ever, smokes means actively smoking, and unknown <br>
  type: string
- stroke <br>
  content: target field, patient's status due to stroke <br>
  distinct value: 0 means no, 1 means having the disease <br>
  type: boolean
### Data Understanding Stages ###
- see statistical description of the dataset <br>
  ![dataset_statistics](https://user-images.githubusercontent.com/99194827/169442667-22cf9254-7e30-46f5-a8c1-96b8b76a1037.png) <br>
  From the description above, it is known that avg_glucose_level and bmi have max value that really far from its upper quartile (possibly outlier detected).
- visualize numerical feature with boxplot <br>
  Boxplot of avg_glucose_level: <br>
  ![boxplot_avg_glucose_level_before](https://user-images.githubusercontent.com/99194827/169442866-d5c657d2-3a1e-4cbe-88a6-e3021c1a253d.png) <br>
  There are outlier detected. <br><br>
  Boxplot of bmi: <br>
  ![boxplot_bmi_before](https://user-images.githubusercontent.com/99194827/169442891-33919aa1-232c-4b9b-901c-c45831b720cc.png) <br>
  Outlier are strongly shown.
- visualize categorical feature with barplot <br>
  Barplot of gender: <br>
  ![barplot_gender](https://user-images.githubusercontent.com/99194827/169442910-c2c15298-290c-4d1a-b8d6-abb99fbd2524.png) <br>
  There are 3 unique values. "Other" gives no useful insight for the project, because it's hard to explain connection between unknown gender with stroke diagnosis. <br><br>
  Barplot of ever_married: <br>
  ![barplot_ever_married](https://user-images.githubusercontent.com/99194827/169442933-1c9f6421-9f02-4bea-8cc0-ef789424e848.png) <br>
  There are 2 unique values. <br><br>
  Barplot of work_type: <br>
  ![barplot_work_type](https://user-images.githubusercontent.com/99194827/169442947-436dcea5-32dd-494e-9666-bdb3016a2be6.png) <br>
  There are 5 unique values. <br><br>
  Barplot of Residence_type: <br>
  ![barplot_residence_type](https://user-images.githubusercontent.com/99194827/169442963-9c1a122c-946b-40cc-9ca8-ee960e57197a.png) <br>
  There are 2 unique values. <br><br>
  Barplot of smoking_status: <br>
  ![barplot_smoking_status](https://user-images.githubusercontent.com/99194827/169442981-df48ee1b-9caf-40b5-a193-a4245d221904.png) <br>
  There are 4 unique values. "Other" gives no useful insight for the project, because it's hard to explain connection between unknown smoking status with stroke diagnosis.
- visualize correlation between categorical features and target feature with catplot <br>
  Catplot of stroke vs gender: <br>
  ![catplot_gender](https://user-images.githubusercontent.com/99194827/169443024-0db4b527-9c9b-4b62-907e-2dfebac7692a.png) <br>
  Average stroke risk for male and female have no big different, so it can be says that gender is less affecting stroke. <br><br>
  Catplot of stroke vs ever_married: <br>
  ![catplot_ever_married](https://user-images.githubusercontent.com/99194827/169443045-dadbd14d-3230-4b28-a07f-e382d03e2777.png) <br>
  Average stroke risk between patient that haven't and have married seem very different, so it can be says that ever_married is affecting stroke. <br><br>
  Catplot of stroke vs work_type: <br>
  ![catplot_work_type](https://user-images.githubusercontent.com/99194827/169443079-ff1e5b0b-c2d5-4cc5-bfc5-37b1fa56dcbb.png) <br>
  Average stroke risk in every categories are varied, so it can be says that work_type is affecting stroke. <br><br>
  Catplot of stroke vs Residence_type: <br>
  ![catplot_residence_type](https://user-images.githubusercontent.com/99194827/169443113-21de49a1-8bb4-49aa-85f6-7183ebdcecdb.png) <br>
  Average stroke risk for rural and urban have no big different, so it can be says that residence_type is less affecting stroke. <br><br>
  Catplot of stroke vs smoking_status: <br>
  ![catplot_smoking_status](https://user-images.githubusercontent.com/99194827/169443153-6c7cd720-aeb1-4a8d-bbfe-27518277380a.png) <br>
  Average stroke risk in every categories are varied, so it can be says that smoking_status is affecting stroke.
- visualize correlation between numerical features and target feature with heatmap <br>
  Heatmap: <br>
  ![heatmap](https://user-images.githubusercontent.com/99194827/169443172-55adf28d-b9f7-47a4-8705-39205b1cf2f0.png) <br>
  Coefficient of correlation of bmi and avg_glucose_level toward stroke are very low (<0.05), so these features can be say less affecting stroke.

## Data Preparation ##
Stages of data preparation:
### Data Cleaning ###
Few things done in this stage:
- Deletion of id feature <br>
  This is done because id only unique identifier that clearly won't affect stroke diagnosis.
- Deletion of missing values <br>
  Missing values are detected with .info() method and deleted with .dropna() method.
- Deletion of Outlier <br>
  Outlier detected in boxplot visualization. Through those visualizations, avg_glucose_level and bmi are detected having outliers. Outliers deleted with IQR method, while IQR stands for substraction between upper and lower quartile. x can be says as an outlier if and only if:
  ```
  x < Q1 - 1.5*IQR atau x > Q3 + 1.5*IQR
  
  ```
  Boxplot of avg_glucose_level before and after outliers handling: <br>
  ![boxplot_avg_glucose_level_before](https://user-images.githubusercontent.com/99194827/169443367-a5fa02c3-359e-4ebf-bcaa-a59c627d88c6.png)
  ![boxplot_avg_glucose_level_after](https://user-images.githubusercontent.com/99194827/169443372-15576a1f-e7c5-4617-8629-2a7ef80d7460.png) <br><br>
  Boxplot of bmi before and after outliers handling: <br>
  ![boxplot_bmi_before](https://user-images.githubusercontent.com/99194827/169443477-61410c9d-76f9-4637-8208-c12e9e5a1ee5.png)
  ![boxplot_bmi_after](https://user-images.githubusercontent.com/99194827/169443490-31a4b6be-edf6-46fd-a46d-2471e7c25f9f.png)

### Feature Selection ###
Few things done in this stage:
- Deletion of "useless" categories from categorical features <br>
  After barplot visualization conducted from each categorical features, distinct value and number of data for each values are known. "Other" from gender and "Unknown" from smoking_status are deleted, because they give no significant insights for the project.
- Deletion of categorical features that less affecting stroke <br>
  According to catplot visualization, gender and residence_type are deleted because categories of each features have no significant different correlation each other.
- Deletion of numerical features that less affecting stroke <br>
  According to heatmap visualization, avg_glucose_level and bmi are deleted, because they have low correlation with stroke feature.
### Data Transform ###
Few things done in this stage:
- Label Encoding <br>
  Label encoding used here is One Hot Encoding. By using this method, categorical features' values turned as numerical value, data can be learned by the model. <br>
  ever_married before encoding <br>
  ![ever_married_before](https://user-images.githubusercontent.com/99194827/169443657-e97ee74b-1f82-475b-8e1b-09af999ed4c1.png) <br><br>
  ever_married after encoding <br>
  ![ever_married_after](https://user-images.githubusercontent.com/99194827/169443675-201220f9-231d-4a43-840c-591b3fd13103.png)
- Split dataset <br>
  Dataset splitted as data training and testing with 80:20 ratio. Parameter of stratify defined to be equal with target feature, so proportion of label on training and testing data equal with the whole dataset.
- Normalization <br>
  Normalization changes value from a feature to be in range 0 to 1. A value will be transformed as follows: <br>
  ![Normalisasi](https://www.oreilly.com/library/view/regression-analysis-with/9781788627306/assets/ffb3ac78-fd6f-4340-aa92-cde8ae0322d6.png)


## Modeling ##
Model used here are KNN and Random Forest.
- KNN is classifying a value based on classification of nearest dots with the value. Closeness of dots with the value is measured with euclidean distance. Parameter of n_neighbors defined number of nearest dots that will affect classification of a value. In thi project, parameter of n_neighbors being used is 5, simply means that classification of a value depends on classification of 5 nearest dots from the value. If the 3 nearest dots classified as 1, then the value will be classified as 1, too. <br>
  KNN has advantage, which is very easy to apply. Meanwhile, the advantage of KNN is that it isn't work good to big dataset with high dimention and also need normalization/standardization.
- Random Forest is classifying a value with help from decision trees. Decision tree is a classification method with asking compound questions about the value. Final result of a decision tree is the classified category. Random Forest is classification that combine classification result from many decision trees. In this project, parameter of n_estimators being used is 50, simply means that classification of a value depends on result from 50 decision trees. If the 26 decision tree classifying a value as 1, then the value will be classified as 1, too. <br>
  Random Forest has advantage kelebihan, where they need no normalization/standardization. Meanwhile, the advantage of Random Forest is that it needs longer training time. <br>

According to evaluation metrics used here, best model for stroke diagnosis is KNN. Accuracy score for KNN and Random Forest has fulfill desired criteria (>90%) and fitting_score from KNN is lower.

## Evaluation ##
There are 2 evaluation metrics used here, which are Fitting Score and Accuracy. Accuracy become satisficing metric and fitting score become optimizing metric.
- Fitting Score is substraction between MSE on testing and MSE on training data. This metric describes type of data fitting that happened. MSE measures average of powered of substraction between prediction value and actual value. Model with lower fitting score is better model. <br>
  Formula MSE: <br>
  ![MSE](https://vedexcel.com/wp-content/uploads/2020/12/MSE_Python.gif)
- Accuracy measures ratio between number of total true prediction (True Positive dan True Negative) with number of total prediction. Model with accuracy >90% can be said as good in this project.
  Formula Accuracy: <br>
  ![Accuracy](https://th.bing.com/th/id/OIP.XsegOFaHxkbrh5kIHoHn2wHaBX?pid=ImgDet&rs=1) <br>

According to evaluation metrics used here, best model for stroke diagnosis is KNN. Accuracy score for KNN and Random Forest has fulfill desired criteria (>90%) and fitting_score from KNN is lower. <br>
![evaluation](https://user-images.githubusercontent.com/99194827/169443755-64a00f3b-8b2e-4016-b7ea-449d326d3fa3.png)

## Reference ##
Delima, Mihardja LK, Ghani L. 2016. Faktor risiko dominan penderita stroke di indonesia. Buletin Penelitian Kesehatan. 44 (1): 49-58. doi: 10.22435/bpk.v44i1.4949.49-58
