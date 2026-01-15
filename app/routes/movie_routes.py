from flask import Blueprint
from app.models.movie import Movie
from app.schemas.movie_schema import MovieSchema
from flask import jsonify

movie_bp = Blueprint("movies", __name__, url_prefix="/movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_bp.route("/", methods=["GET"])
def get_movies():
    movies = Movie.query.all()
    return movies_schema.jsonify(movies)

# @movie_bp.route("/<int:id>", methods=["GET"])
# def get_movie(id):
#     movie = Movie.query.get_or_404(id)
#     return movie_schema.jsonify(movie)

@movie_bp.route("/<int:id>", methods=["GET"])
def get_movie(id):
    movie = Movie.query.get_or_404(id)

    return jsonify({
        "id": movie.id,
        "title": movie.title,
        "overview": movie.overview,
        "vote_average": movie.vote_average,
        "runtime": movie.runtime,
        "original_language": movie.original_language,
        "genres": movie.genres,
        "keywords": movie.keywords,
        "original_title": movie.original_title,
        "popularity": movie.popularity,
        "vote_count": movie.vote_count,
        "release_date": movie.release_date.isoformat() if movie.release_date else None,
        "credits": {
            "cast": movie.credits.cast if movie.credits else [],
            "crew": movie.credits.crew if movie.credits else []
        }
    })

