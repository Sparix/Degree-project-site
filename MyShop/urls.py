from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoriesHome.as_view(), name='home'),
    path('product/<slug:cat_slug>/', ProductHome.as_view(), name='category'),
    path('<slug:product_slug>/', AboutProduct.as_view(), name='product'),
    path('test', test, name='register')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)