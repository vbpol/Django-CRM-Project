from django.urls import path
from . import views
urlpatterns = [
    path('',views.FooCreateView.as_view(),name='path_add'),
]
