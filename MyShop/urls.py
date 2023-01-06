from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoriesHome.as_view(), name='home'),
    path('product/<slug:cat_slug>/', ProductHome.as_view(), name='category'),
    path('<slug:product_slug>/', AboutProduct.as_view(), name='product'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('profile', profile, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)