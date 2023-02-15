from pathlib import Path
from uuid import uuid4

from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Generation, Images, User
from api.serializers import GenerationSerializer, ImagesSerializer, UserSerializer
from django.forms.models import model_to_dict


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewByTgID(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        tg_id = self.kwargs.get('telegram_id')
        if tg_id is not None:
            queryset = queryset.filter(telegram_id=tg_id)
        return queryset


class GenerationsViewSet(viewsets.ModelViewSet):
    queryset = Generation.objects.all()
    serializer_class = GenerationSerializer


class GenerationsUserSet(generics.ListCreateAPIView):
    serializer_class = GenerationSerializer

    def get_queryset(self):
        queryset = Generation.objects.all()
        user_id = self.kwargs.get('user')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user')
        request.data['user'] = user_id
        return super().create(request)


@api_view(['POST'])
def acquire(request):
    generation = Generation.objects.filter(status='pending').first()
    if not generation:
        return Response(data=[], status=status.HTTP_201_CREATED)
    generation.status = 'running'
    generation.save()
    data = model_to_dict(generation)
    return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def complete(request, uid):
    generation = Generation.objects.filter(uid=uid).first()
    generation.status = 'complete'
    generation.save()
    data = model_to_dict(generation)
    return Response(data=data, status=status.HTTP_201_CREATED)


IMAGES = Path('.data/images')


class GenerationsImageUpload(generics.CreateAPIView):
    serializer_class = ImagesSerializer

    def create(self, request, *args, **kwargs):
        generation_id = self.kwargs['generation_id']
        dir = IMAGES / str(generation_id)
        dir.mkdir(parents=True, exist_ok=True)
        filename = f'{uuid4().hex}.png'
        filepath = dir / filename

        file = request.data.get('file')
        content = file.read()
        with open(filepath, 'wb') as fs:
            fs.write(content)

        request.data['generation'] = generation_id
        request.data['url'] = str(filepath)
        return super().create(request)
