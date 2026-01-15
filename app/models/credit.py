from app.extensions import db

class Credit(db.Model):
    __tablename__ = "credits"

    # id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(
        db.Integer,
        db.ForeignKey("movies.id"),
        primary_key=True,
        nullable=False,
        unique=True
    )
    title = db.Column(db.String(255))
    cast = db.Column(db.Text)
    crew = db.Column(db.Text)

    # ✅ Back reference
    movie = db.relationship(
        "Movie",
        uselist=False,
        back_populates="credits"
    )
