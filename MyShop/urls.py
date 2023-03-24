from django.conf.urls.static import static
from django.urls import path

from Degree import settings
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('categories', CategoriesHome.as_view(), name='categories'),
    path('product/<slug:cat_slug>/', ProductHome.as_view(), name='category'),
    path('aboutproduct/<slug:product_slug>/', product_detail, name='product'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('cabinet', ProfilePage.as_view(), name='cabinet'),
    path('staff_form', AddProduct.as_view(), name='stuff_form'),
    path('change_password', PasswordChange.as_view(), name='change_psw'),
    path('edit_profile', update_user, name='edit_profile'),
    path('search/', Search.as_view(), name='search'),
    path('filter/<slug:cat_slug>/', FilterProduct.as_view(), name='filter'),
    path('orders_user', UserOrder.as_view(), name='orders_user'),
    path('aboutproduct/<slug:product_slug>/comment', comments, name='comment_user')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
