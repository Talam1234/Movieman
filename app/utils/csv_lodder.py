import pandas as pd
from app.extensions import db
from app.models.movie import Movie
from app.models.credit import Credit

def load_movies(csv_path):
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        movie = Movie(
            id=int(row["id"]),
            title=row["title"],
            original_title=row["original_title"],
            overview=row["overview"],
            genres=row["genres"],
            keywords=row["keywords"],
            popularity=row["popularity"],
            release_date=row["release_date"],
            runtime=row["runtime"],
            vote_average=row["vote_average"],
            vote_count=row["vote_count"]
        )
        db.session.merge(movie)
    db.session.commit()
