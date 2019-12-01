from django.urls import path

from . import views

urlpatterns = [
    path('leave-requests/', views.LeaveRequestList.as_view()),
    path('leave-requests/<int:pk>/', views.LeaveRequestDetail.as_view()),
]
