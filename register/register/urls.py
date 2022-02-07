"""register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from sextosentido import views
from sextosentido.views import ProductViewSet, LoginAPIView, LogOutAPIView, LoggedInUser
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

router = routers.SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('loginAPI', LoginAPIView, basename='loginAPI')
router.register('logoutAPI', LogOutAPIView, basename='logoutAPI')
router.register('user', LoggedInUser, basename='logged_in_user')
schema_view = get_schema_view(
    openapi.Info(
        title="SextoSentidoAPI",
        default_version='v 1.0',
        description="Dotcom API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@epcotsa.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'sextosentido'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('rest_framework.urls')),
    path('register/<sku>', views.register, name='register' ),
    path('profile/', user_views.profile, name='profile'),
    path('signin/', user_views.signin, name='signin'),
    path('login/', authentication_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
]
