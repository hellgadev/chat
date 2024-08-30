from django.urls import path

from apps.core.api.views import (
    ThreadListCreateAPIView,
    ThreadDestroyAPIView,
    MessageCreateListAPIView,
    MarkMessageAsReadAPIView,
)

urlpatterns = [
    path('', ThreadListCreateAPIView.as_view()),
    path('<int:pk>/', ThreadDestroyAPIView.as_view()),
    path('<int:thread_id>/messages/', MessageCreateListAPIView.as_view()),
    path('<int:thread_id>/messages/<int:pk>/mark-as-read/', MarkMessageAsReadAPIView.as_view()),
]
