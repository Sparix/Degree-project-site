from django.conf.urls.static import static
from django.urls import path

from Degree import settings
from .views import *

urlpatterns = [
    path('', CategoriesHome.as_view(), name='home'),
    path('product/<slug:cat_slug>/', ProductHome.as_view(), name='category'),
    path('<slug:product_slug>/', AboutProduct.as_view(), name='product'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('profile', AddProduct.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)