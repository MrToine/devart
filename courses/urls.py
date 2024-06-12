from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:course_id>-<slug:course_name>/', views.show, name="show"),
]