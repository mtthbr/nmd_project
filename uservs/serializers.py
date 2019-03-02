from rest_framework.serializers import ModelSerializer
from .models import Uservs

class UservsSerializer(ModelSerializer):
  class Meta:
    model = Uservs
    fields = '__all__'
