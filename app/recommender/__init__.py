from app.recommender.recommender import MovieRecommender

recommender = None

def init_recommender():
    global recommender
    print("🚀 init_recommender() called")

    recommender = MovieRecommender()

    print("✅ recommender initialized:", recommender)
