from ninja import ModelSchema

from politician.models import Politician


class SchemaPolitician(ModelSchema):
    class Config:
        model = Politician
        model_fields = '__all__'
