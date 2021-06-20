from django.urls import path
from django.views.decorators.cache import cache_page

from workers.views import *

urlpatterns = [
    path('', cache_page(60)(WorkersHome.as_view()), name='workers'),
    path('about/', AboutPage.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', cache_page(30)(WorkersCategory.as_view()), name='category'),

]
