from bpshapi.views import UserView, CityView, ShopView
from bpshapi.views.auth import check_user, register_user
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'cities', CityView, 'city')
router.register(r'shops', ShopView, 'shop')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
