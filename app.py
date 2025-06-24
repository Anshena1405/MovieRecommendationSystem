from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend_multiple(selected_movies):
    indices = [movies[movies['title'] == title].index[0] for title in selected_movies]
    combined_scores = similarity[indices[0]].copy()
    for idx in indices[1:]:
        combined_scores += similarity[idx]
    recommended_indices = sorted(
        list(enumerate(combined_scores)), key=lambda x: x[1], reverse=True
    )
    selected_indices = set(indices)
    recommendations = []
    for i in recommended_indices:
        if i[0] not in selected_indices:
            recommendations.append(movies.iloc[i[0]].title)
        if len(recommendations) == 10:
            break
    return recommendations

@app.route('/')
def index():
    return render_template('index.html', movie_list=movies['title'].values)

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_movies = request.form.getlist('movie')
    if len(selected_movies) != 5:
        return render_template('index.html', movie_list=movies['title'].values, error="Please select exactly 5 movies.")
    
    recommendations = recommend_multiple(selected_movies)
    return render_template('result.html', selected_movies=selected_movies, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
