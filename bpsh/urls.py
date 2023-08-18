from bpshapi.views import UserView, CityView, ShopView, ProductView, CommentView
from bpshapi.views.auth import check_user, register_user
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'cities', CityView, 'city')
router.register(r'shops', ShopView, 'shop')
router.register(r'products', ProductView, 'shop')
router.register(r'comments', CommentView, 'comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
