#  Movie Recommendation System

A content-based **Movie Recommendation System** built using **Python**, **Machine Learning**, and **Streamlit**.  
The system recommends similar movies using cosine similarity and displays posters fetched from the TMDB API.


##  Features
-  Content-based movie recommendation  
-  Uses **CountVectorizer** and **Cosine Similarity**  
-  Displays HD posters using **TMDB API**  
-  Built with Streamlit for a clean, fast UI  
-  Uses pickle files for quick loading of model and data  



##  How It Works

### Data Processing (main.py – Jupyter Notebook)
- Used **TMDB 10,000 movies dataset**  
- Performed **feature engineering**  
- Combined metadata (overview, genres) into a single **tags** column  
- Converted text into numerical vectors using **CountVectorizer**  
- Calculated similarity matrix using **cosine similarity**  
- Saved:
  - `movies.pkl` — cleaned movie dataframe  
  - `similarity.pkl` — cosine similarity matrix  

###  Frontend (app.py – Streamlit)
- Loads pickle files  
- When a user selects a movie, the app:
  1. Finds similar movies  
  2. Fetches poster URLs using **TMDB API**  
  3. Displays them in 3 columns (5 per row)  


##  Tech Stack

**Backend & ML**
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Pickle  

**Frontend**
- Streamlit  
- TMDB API  

##  Project Structure

movie-recommender

- app.py                 
- main.py               
- movies.pkl            
- similarity.pkl         
- config.py              
- requirements.txt
- README.md
