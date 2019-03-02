from rest_framework.serializers import ModelSerializer
from .models import Artiste, Solex, Notification, Description

class ArtisteSerializer(ModelSerializer):
  class Meta:
    model = Artiste
    fields = '__all__'

class SolexSerializer(ModelSerializer):
  class Meta:
    model = Solex
    fields = '__all__'

class NotificationSerializer(ModelSerializer):
  class Meta:
    model = Notification
    fields = '__all__'

class DescriptionSerializer(ModelSerializer):
  class Meta:
    model = Description
    fields = '__all__'