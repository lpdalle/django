from rest_framework import routers

from api.views import (
    GenerationsImageUpload,
    GenerationsUserSet,
    GenerationsViewSet,
    UsersViewSet,
    UserViewByTgID,
    acquire,
    complete,
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
    path('api/v1/users/<int:user>/generations/', GenerationsUserSet.as_view()),
    path('api/v1/generations/acquire', acquire),
    path('api/v1/generations/<int:uid>/complete', complete),
    path('api/v1/generations/<int:generation_id>/images/', GenerationsImageUpload.as_view()),
]
