from flask import Flask
from .config import Config
from .extensions import db, ma
from app.recommender import init_recommender

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    # 🔥 REGISTER MODELS FIRST
    from app.models import Movie, Credit

    # 🔥 INITIALIZE recommender INSIDE app context
    with app.app_context():
        print("🧠 Initializing recommender inside create_app()")
        init_recommender()

    from .routes.movie_routes import movie_bp
    from .routes.credit_routes import credit_bp
    from app.routes.recommend_routes import recommend_bp

    app.register_blueprint(movie_bp)
    app.register_blueprint(credit_bp)
    app.register_blueprint(recommend_bp)

    return app
