from app.extensions import ma
from app.models.movie import Movie

class MovieSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Movie
        load_instance = True
        include_relationships = False