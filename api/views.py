from rest_framework import generics, viewsets

from api.models import Generation, Images, User
from api.serializers import GenerationSerializer, UserSerializer


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
        user_id = self.kwargs.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        return queryset

    def create(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        request.data['user_id'] = user_id
        return super().create(request)


class GenerationAcquire(generics.CreateAPIView):
    serializer_class = GenerationSerializer

    def create(self, request, *args, **kwargs):
        queryset = Generation.objects.filter(status='pending').first()
        queryset.status = 'running'
        return super().create(request, *args, **kwargs)


class GenerationsStatusComplete(generics.UpdateAPIView):
    serializer_class = GenerationSerializer
