# 🎬 Movie Recommendation System

This is a **content-based movie recommendation system** built with **Python** and **FastAPI**, using the **Bag of Words (BoW)** technique.  
It recommends movies similar to a given movie by analyzing their overviews (descriptions) and computing similarity scores.

---

## ✨ Features

- Preprocesses movie descriptions with stemming and stopword removal.
- Uses **CountVectorizer** (BoW) to create feature vectors.
- Computes **cosine similarity** between movies.
- FastAPI backend with:
  - `/ping` health-check endpoint
  - `/recommend` endpoint to get top 5 similar movies
- Modular structure for easy extension.

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI** (backend framework)
- **scikit-learn** (CountVectorizer, cosine similarity)
- **NLTK** (PorterStemmer)
- **Pandas** (data handling)

## 📡 API Endpoints

### `GET /ping`

Health-check endpoint.

**Response:**

```json
{
  "message": "pong"
}
```

### `GET /recommend?movie_id=<id>`

**Request**

```json
{
  "movie_id": 123
}
```

**_Response_**

```json
{
  "recommendations": [
    { "movie_id": 101, "movie_title": "Guardians of the Galaxy" },
    { "movie_id": 202, "movie_title": "John Carter" },
    { "movie_id": 303, "movie_title": "Star Trek" },
    { "movie_id": 404, "movie_title": "The Avengers" },
    { "movie_id": 505, "movie_title": "The Last Airbender" }
  ]
}
```
