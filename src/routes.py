from fastapi import APIRouter
from preprocessing import load_data

router = APIRouter()

# Load data once
sample_movies, similarity = load_data()

@router.get("/recommend")
def recommend_movie(movie_id : int):
    if movie_id not in sample_movies['id'].values:
        return {"error": f"Movie with id {movie_id} does not exist"}
    
    movie_index = sample_movies[sample_movies['id'] == movie_id].index[0]
    distances = similarity[movie_index]
    similar_movies_list = sorted(
        list(enumerate(distances)), reverse=True, key=lambda x: x[1]
    )[1:6]

    # recommendations = [sample_movies.iloc[i[0]].title for i in similar_movies_list]
    recommendations = []
    for i in similar_movies_list:
        recommendations.append({
            "movie_id" : int(sample_movies.iloc[i[0]].id),
            "movie_title": sample_movies.iloc[i[0]].title
        })
    return {"recommendations": recommendations}


# test route 
@router.get("/ping")
def ping():
    return {"message": "pong"}
