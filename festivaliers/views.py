from django.shortcuts import render

from .models import Festivalier
from .serializers import FestivalierSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['get'])
def fetch_festivaliers(request):

  rest_list = Festivalier.objects.order_by('-sign_in_date')
  serializer = FestivalierSerializer(rest_list, many=True)
  return Response(serializer.data)