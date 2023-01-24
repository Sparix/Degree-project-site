from django.conf.urls.static import static
from django.urls import path

from Degree import settings
from .views import *

urlpatterns = [
    path('', CategoriesHome.as_view(), name='home'),
    path('product/<slug:cat_slug>/', ProductHome.as_view(), name='category'),
    path('aboutproduct/<slug:product_slug>/', AboutProduct.as_view(), name='product'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('cabinet', ProfilePage.as_view(), name='cabinet'),
    path('staff_form', AddProduct.as_view(), name='stuff_form'),
    path('change_password', PasswordChange.as_view(), name='change_psw'),
    path('edit_profile', update_user, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
