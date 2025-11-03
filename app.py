import pickle
import streamlit as st
import requests

# ---- CONFIG ----
st.set_page_config(
    page_title="🎬 Movie Recommender",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- CUSTOM STYLES ----
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');

        /* Background image with overlay */
        .stApp {
            background-image: 
                linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)),
                url("https://images.unsplash.com/photo-1517602302552-471fe67acf66?auto=format&fit=crop&w=1920&q=80");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #FFFFFF;
        }

        /* Header style */
        h1 {
            color: #FFD700;
            text-align: center;
            font-family: 'Poppins', 'Trebuchet MS', sans-serif;
            font-weight: 700;
            font-size: 3rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.8), 0 0 20px rgba(255, 215, 0, 0.5);
            margin-top: 30px;
            margin-bottom: 20px;
            animation: fadeInDown 1s ease-in-out;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Improved selectbox styling */
        div[data-baseweb="select"] {
            width: 60% !important;
            margin: 0 auto;
            background-color: rgba(42, 42, 64, 0.9);
            border-radius: 10px;
            padding: 10px 5px;
            font-size: 1.1rem;
            color: white;
        }

        div[data-baseweb="select"] > div {
            min-height: 55px !important;
            display: flex;
            align-items: center;
            font-size: 1.05rem;
        }

        div[data-baseweb="select"]:hover {
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
            transition: 0.3s;
        }

        div[data-baseweb="select"] span {
            font-weight: 600;
            color: #FFD700;
        }

        /* Button styling */
        .stButton>button {
            background-color: #FFD700;
            color: black;
            border-radius: 10px;
            font-weight: bold;
            font-size: 1.1rem;
            padding: 0.6rem 1.2rem;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background-color: #FFC300;
            transform: scale(1.05);
        }

        /* Movie card layout */
        .movie-card {
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 10px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transition: 0.3s;
        }

        .movie-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 14px rgba(255, 215, 0, 0.5);
        }

        .movie-title {
            font-size: 16px;
            font-weight: bold;
            color: #FFD700;
            margin-top: 8px;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #BBBBBB;
            margin-top: 50px;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---- FETCH POSTER ----
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"

# ---- RECOMMENDER FUNCTION ----
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names, recommended_movie_posters

# ---- MAIN UI ----
st.markdown("<h1>🎥 Movie Recommender System</h1>", unsafe_allow_html=True)

movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🎬 Type or select a movie:",
    movie_list,
    index=None,
    placeholder="Choose your favorite movie..."
)

if st.button("✨ Show Recommendations"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

    cols = st.columns(5)
    for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
        with col:
            st.markdown(f"""
                <div class="movie-card">
                    <img src="{poster}" width="100%" style="border-radius:10px">
                    <div class="movie-title">{name}</div>
                </div>
            """, unsafe_allow_html=True)
else:
    st.info("👆 Select a movie and click *Show Recommendations* to begin.")

# ---- FOOTER ----
st.markdown("<div class='footer'>💡 Powered by Streamlit & TMDB API</div>", unsafe_allow_html=True)
