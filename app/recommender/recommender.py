import ast
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.models.movie import Movie

class MovieRecommender:

    def __init__(self):
        print("🔹 Initializing MovieRecommender...")
        self._load_from_db()
        self._prepare_data()
        self._build_similarity()
        print("✅ Recommender ready!")

    def _load_from_db(self):
        print("🔹 Loading movies from MySQL...")

        movies = Movie.query.with_entities(
            Movie.id,
            Movie.title,
            Movie.overview,
            Movie.genres,
            Movie.keywords
        ).all()

        print(f"✅ Loaded {len(movies)} movies")

        self.df = pd.DataFrame(
            movies,
            columns=["id", "title", "overview", "genres", "keywords"]
        )

        print(self.df.head())  # preview

    def _prepare_data(self):
        print("🔹 Preparing tags...")

        self.df["overview"] = self.df["overview"].fillna("")

        self.df["genres"] = self.df["genres"].fillna("[]").apply(
            lambda x: " ".join(
                [i["name"] for i in ast.literal_eval(x)]
            )
        )

        self.df["keywords"] = self.df["keywords"].fillna("[]").apply(
            lambda x: " ".join(
                [i["name"] for i in ast.literal_eval(x)]
            )
        )

        self.df["tags"] = (
            self.df["overview"] + " " +
            self.df["genres"] + " " +
            self.df["keywords"]
        )

        print("✅ Tags column created")
        print(self.df[["id", "title", "tags"]].head())

    def _build_similarity(self):
        print("🔹 Building similarity matrix...")

        cv = CountVectorizer(
            max_features=5000,
            stop_words="english"
        )

        vectors = cv.fit_transform(self.df["tags"]).toarray()
        self.similarity = cosine_similarity(vectors)

        self.movie_index = pd.Series(
            self.df.index,
            index=self.df["id"]
        )

        print("✅ Similarity matrix built")
        print(f"Matrix shape: {self.similarity.shape}")

    def recommend(self, movie_id, n=5):
        print(f"🔹 Recommendation requested for movie_id={movie_id}")

        if movie_id not in self.movie_index:
            print("❌ Movie ID not found in index")
            return []

        idx = self.movie_index[movie_id]
        print(f"Movie index in dataframe: {idx}")

        distances = sorted(
            enumerate(self.similarity[idx]),
            reverse=True,
            key=lambda x: x[1]
        )

        recommendations = []
        for i in distances[1:n+1]:
            movie = self.df.iloc[i[0]]
            recommendations.append({
                "id": int(movie["id"]),
                "title": movie["title"]
            })

        print("✅ Recommendations:", recommendations)
        return recommendations
