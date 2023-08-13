from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('widget/add/', views.add_Widget, name='widget_create'),
path('widget/<int:pk>/delete', views.WidgetDelete.as_view(), name='widget_delete'),
]