from rest_framework import routers

from api.views import (
    GenerationAcquire,
    GenerationsUserSet,
    GenerationsViewSet,
    UsersViewSet,
    UserViewByTgID,
)
from django.contrib import admin
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'generations', GenerationsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/users/telegram/<str:telegram_id>/', UserViewByTgID.as_view()),
    path('api/v1/generations/', include(router.urls)),
    path('api/v1/users/<int:user_id>/generations/', GenerationsUserSet.as_view()),
    path('api/v1/generation/acquire', GenerationAcquire.as_view()),
]
