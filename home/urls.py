from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('toggle-online/',views.ToggleOnlineView.as_view()),
    path('connect/<int:id>',views.ConnectionView.as_view()),
]
