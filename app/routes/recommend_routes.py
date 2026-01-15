from flask import Blueprint, jsonify, request
from app.recommender import recommender   # SAME OBJECT

recommend_bp = Blueprint("recommend", __name__, url_prefix="/recommend")

@recommend_bp.route("/<int:movie_id>", methods=["GET"])
def recommend(movie_id):
    print("🔹 recommend route hit")

    if recommender is None:
        print("❌ recommender is NONE")
        return jsonify({"error": "Recommender not initialized"}), 500

    n = int(request.args.get("n", 5))
    results = recommender.recommend(movie_id, n)

    return jsonify({
        "movie_id": movie_id,
        "recommendations": results
    })
