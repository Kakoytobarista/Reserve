from django.urls import path
from django.views.decorators.cache import cache_page

from workers.views import *


urlpatterns = [
    path('', WorkersHome.as_view(), name='workers'),
    path('about/', AboutPage.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', cache_page(30)(WorkersCategory.as_view()), name='category'),
    path('delete/<slug:post_slug>/', DeletePost.as_view(), name='delete_post'),
    path('update/<slug:post_slug>/', UpdatePost.as_view(), name='update_post'),

]
