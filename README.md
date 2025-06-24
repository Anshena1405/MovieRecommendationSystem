# 🎬 Multi-Movie Recommender System

A clean, interactive movie recommendation web app that lets you choose **any 5 movies** you like and recommends 10 similar movies — built using **Flask**, **Python**, and **cosine similarity**.

This project is designed as a portfolio-ready recommendation system with a modern frontend and fully customizable backend logic.

---

## 📊 Dataset

The dataset is based on **[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** from Kaggle.

Used columns: `title`, `overview`, `genres`, `keywords`

Similarity is calculated using **TF-IDF** vectorization of the movie overviews.

---

## 🚀 Features

- Select **any 5 movies** from a visually organized grid
- Get top 10 movie recommendations based on content similarity
- Responsive, scrollable UI with hover effects
- Flask backend with HTML + CSS frontend
- Easy to extend with posters, ratings, genres, etc.

---

## 🛠️ Tech Stack

- 🧠 **Python**, **Flask**
- 🧩 **scikit-learn** (cosine similarity, TF-IDF)
- 💻 **HTML**, **CSS** (custom styling)
- 📦 `movies.pkl`, `similarity.pkl` for fast loading

---

## 💻 Setup & Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
