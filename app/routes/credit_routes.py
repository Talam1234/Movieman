from flask import Blueprint
from app.models.credit import Credit
from app.schemas.credit_schema import CreditSchema

credit_bp = Blueprint("credits", __name__, url_prefix="/credits")

credit_schema = CreditSchema()

@credit_bp.route("/<int:movie_id>", methods=["GET"])
def get_credit(movie_id):
    credit = Credit.query.filter_by(movie_id=movie_id).first_or_404()
    return credit_schema.jsonify(credit)
