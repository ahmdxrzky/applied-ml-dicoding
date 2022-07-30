# Movie Recommender System #

## Project Overview ##
Problem being highlighted in this project comes from **Entertainment domain**. Human's stress level that increased by time, especially for those who live in Urban area, made people have to be able to entertain themselves. One of many way to do this in pandemic era is watch movies. Unfortunately, there are so many movie released and served in various genres. As the result, building a movie recommender system is a must. This project tries to build a movie recommender system based on its genre.

## Business Understanding ##
### Problem Statement ###
"How to make a movie recommender system using Machine Learning approach?"
### Goal ###
"Model making with Machine Learning approach as movie recommender system."
### Solution Statement ###
"Measure similarities between movies using ***Content-based Filtering***."

## Data Understanding ##
Dataset being used in this project is [IMDB Movies Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows). This dataset has so many missing values in few features, but those features aren't used in this recommender system.
### Fields of Dataset ###
This dataset contains 1000 records with 16 fields. Summary of the dataset based on its fields is shown below: <br>
![dataset_info](https://user-images.githubusercontent.com/99194827/169693379-45d791a5-28aa-445a-b5ae-1557e0a8bbe0.png) <br><br>
Fields in this dataset are:
- Poster_Link <br>
  content: link of the movie's poster used in IMDB's website <br>
  type: string
- Series_Title <br>
  type: string
- Released_Year <br>
  type: string
- Certificate <br>
  content: age allowed to watch the movie <br>
  type: string
- Runtime <br>
  content: duration of the movie <br>
  type: string
- Genre <br>
  type: string
- IMDB_Rating <br>
  content: rating of the movie on IMDB's website <br>
  type: float
- Overview <br>
  content: moie's synopsis <br>
  type: string
- Meta_score <br>
  content: score that brought by the movie <br>
  type: float
- Director <br>
  type: string
- Star1 <br>
  content: name of the actor/actress <br>
  type: string
- Star2 <br>
  content: name of the actor/actress <br>
  type: string
- Star3 <br>
  content: name of the actor/actress <br>
  type: string
- Star4 <br>
  content: name of the actor/actress <br>
  type: string
- No_of_Votes <br>
  content: total number of voters <br>
  type: integer
- Gross <br>
  content: revenue of the movie <br>
  type: object
### Stages of Data Understanding ###
- see total number of unique data from Series_Title feature <br>
  ![fitur Series_Title](https://user-images.githubusercontent.com/99194827/169694015-9458cf21-0c3c-49af-b269-bcddb748fc64.png) <br>
  From the picture above, this feature has 1 redundant value.
- see data from Genre feature
  ![fitur Genre](https://user-images.githubusercontent.com/99194827/169694203-e3fbc5cc-78cf-4275-8529-0d1dc2e468bb.png) <br>
  It is known that a movie could have one or more genres. 

## Data Preparation ##
Stages of data preparation:
### Data Cleaning ###
Few things done in this stage:
- manipulate Series_Title feature so it won't have any redundant value <br>
  This is the redundant data <br>
  ![redundant_data](https://user-images.githubusercontent.com/99194827/169694243-e623d06d-b128-4f18-a0b6-28f63303c4ec.png) <br>
  This can be happened since the movie being remaked, so these two movies have different year of release. Special for these movies, their titles are being combined with their year of release.
- check of missing value <br>
  ![missing_value](https://user-images.githubusercontent.com/99194827/169694503-639622f4-2ea6-4367-b573-1e0471850c62.png)
### Feature Selection ###
Few things done in this stage:
deletion of features that aren't used <br>
![fitur rekomendasi](https://user-images.githubusercontent.com/99194827/169694415-67041554-b130-4f64-846e-e234e58149e1.png)

## Modeling and Results ##
Few things done in this stage:
- Data conversion from Genre feature into vector form <br>
  This process done with tfidfvectorizer class. Each movie could have 1 or more genres, so each movie will be represented as vectors with total number of dimensions equal to total number of genres. Tfidfvectorizer class will give weight for each genre of a movie. <br>
  ![tfidfvectorizer](https://user-images.githubusercontent.com/99194827/169762446-102cd00c-a41a-4f23-beb2-bd86a9b1af5e.png)
- Measure similarities between movies using Cosine Similarity method <br>
  After data being vectorized, closeness between data measured with cosine similarity method. This principal based on the fact that two near dots can be assumed as endpoints of two vectors, separated with small angle. Equation being used is: <br>
  ![Cosine_Similarity](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a4c9a778656537624a3303e646559a429868863) <br><br>
  Similarities between 2 movies can be represented with similarity index from calculation above, shown below: <br>
  ![image](https://user-images.githubusercontent.com/99194827/169797215-b30732cf-e132-4dd2-bf2e-b316cffc6033.png) <br>
Result from this modelling is:
A movie recommender system that will be show 10 movies with highest similarity index with movie being inputted by the user. This process sorts top 10 movies with highest similarity index with movie being inputted by the user. <br>
![image](https://user-images.githubusercontent.com/99194827/169797415-0610fa31-d397-4ad5-9602-9f4befb1ce8e.png)

## Evaluation ##
Evaluation metric relevants with this type of project is precision. Precision measures similarity between genre of input and output movie. Formula of precision for recommender system is shown below: <br>
![image](https://user-images.githubusercontent.com/99194827/169797046-60a9f49e-d008-4300-a2bd-2f255483f905.png) <br><br>
Precision of The Kid movies: <br>
![the_kid_precision](https://user-images.githubusercontent.com/99194827/169796003-3ed3ee0f-a4b0-452b-b9c6-2ee14140711b.png)
