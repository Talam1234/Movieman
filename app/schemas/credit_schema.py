from app.extensions import ma
from app.models.credit import Credit

class CreditSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Credit
        load_instance = True
