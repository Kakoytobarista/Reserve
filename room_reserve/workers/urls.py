from django.urls import path

from workers.views import *

urlpatterns = [
    path('', WorkersHome.as_view(), name='workers'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WorkersCategory.as_view(), name='category'),

]
