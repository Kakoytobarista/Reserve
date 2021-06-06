from django.urls import path
from . import views
from .views import pageNotFound


urlpatterns = [
    path('main/', views.index, name='index'),
    path('main/booking/<int:reserver_id>/', views.ReceptionView.as_view(), name='reception'),
    # url(r'^date_from_ajax/$', 'app.views.date_from_ajax', name='date_from_ajax'),
]

handler404 = pageNotFound
