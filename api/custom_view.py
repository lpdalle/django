from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Generation


@api_view(['POST'])
def acquire(request):
    generation = Generation.objects.filter(status='pending').first()
    generation.status = 'running'
    generation.save()
    return Response(generation, status=status.HTTP_200_OK)


@api_view(['POST'])
def complete(uid: int):
    generation = Generation.objects.filter(uid=uid).first()
    generation.status = 'complete'
    generation.save()
    return Response(generation, status=status.HTTP_200_OK)
    