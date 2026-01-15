from app import create_app
from app.extensions import db
from app.recommender import init_recommender

# force model registration
from app.models import Movie, Credit

app = create_app()

with app.app_context():
    db.create_all()
    init_recommender()

if __name__ == "__main__":
    app.run(debug=True)
