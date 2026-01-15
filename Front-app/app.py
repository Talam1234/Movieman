import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="Movieman Recommender",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movieman – Movie Recommendation System")

# ----------------------------
# Helper functions
# ----------------------------

@st.cache_data
def fetch_movies():
    print("🔹 Fetching movies list")
    res = requests.get(f"{API_BASE_URL}/movies/")
    res.raise_for_status()
    return res.json()

def fetch_movie(movie_id):
    print(f"🔹 Fetching movie {movie_id}")
    res = requests.get(f"{API_BASE_URL}/movies/{movie_id}", timeout=5)
    res.raise_for_status()
    return res.json()

def fetch_recommendations(movie_id):
    print(f"🔹 Fetching recommendations for {movie_id}")
    res = requests.get(
        f"{API_BASE_URL}/recommend/{movie_id}?n=5",
        timeout=10
    )
    res.raise_for_status()
    return res.json()["recommendations"]

# ----------------------------
# Load movie list
# ----------------------------

try:
    movies = fetch_movies()
except Exception as e:
    st.error("❌ Flask API not reachable")
    st.exception(e)
    st.stop()

# ----------------------------
# Sidebar movie selector
# ----------------------------

st.sidebar.header("🎥 Select a Movie")

movie_map = {m["title"]: m["id"] for m in movies}
selected_title = st.sidebar.selectbox(
    "Movie",
    movie_map.keys()
)

selected_movie_id = movie_map[selected_title]

# ----------------------------
# Movie details
# ----------------------------

try:
    movie = fetch_movie(selected_movie_id)
except Exception as e:
    st.error("❌ Failed to load movie details")
    st.exception(e)
    st.stop()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(movie["title"])
    st.write(movie.get("overview", "No overview available"))

with col2:
    st.metric("⭐ Rating", movie.get("vote_average", "N/A"))
    st.metric("⏱ Runtime", f'{movie.get("runtime", "N/A")} min')
    st.metric("🌐 Language", movie.get("original_language", "N/A"))

# ----------------------------
# Recommendations Section
# ----------------------------

st.divider()
st.subheader("🎯 Recommended Movies")

try:
    recommendations = fetch_recommendations(selected_movie_id)

    if not recommendations:
        st.warning("No recommendations found")
    else:
        for rec in recommendations:
            st.write(f"🎬 **{rec['title']}** (ID: {rec['id']})")

except Exception as e:
    st.error("❌ Recommendation API failed")
    st.exception(e)

