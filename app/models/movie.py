from app.extensions import db

class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    original_title = db.Column(db.String(255))
    overview = db.Column(db.Text)
    genres = db.Column(db.Text)
    keywords = db.Column(db.Text)
    original_language = db.Column(db.String(10))
    popularity = db.Column(db.Float)
    release_date = db.Column(db.String(20))
    runtime = db.Column(db.Float)
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.Integer)



    # Relationship
    credits = db.relationship(
        "Credit",
        back_populates="movie",
        uselist=False,
    )