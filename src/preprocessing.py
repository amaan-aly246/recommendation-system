import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def process_text(text):
    if not isinstance(text, str):
        return ""
    return " ".join([ps.stem(word) for word in text.split()])

def load_data(path='data/movies-final.csv', n_samples=5000):
    movies = pd.read_csv(path)
    movies_subset = movies[['id', 'title', 'overview']].copy()
    sample_movies = movies_subset.head(n_samples)
    sample_movies['overview'] = sample_movies['overview'].apply(process_text)

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(sample_movies['overview'])
    similarity = cosine_similarity(vectors)
    
    return sample_movies, similarity
