from .models import Uservs
from .serializers import UservsSerializer
from rest_framework import generics

#POST uniquement
class UservsListCreate(generics.CreateAPIView):
  queryset = Uservs.objects.all()
  serializer_class = UservsSerializer

