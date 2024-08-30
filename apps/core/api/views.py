from rest_framework import status
from rest_framework.generics import (
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView
)
from rest_framework.response import Response

from apps.core.api.serializers import (
    ThreadSerializer,
    ThreadCreateSerializer,
    MessageCreateSerializer,
)
from apps.core.models import Thread, Message


class ThreadListCreateAPIView(ListCreateAPIView):
    create_serializer_class = ThreadCreateSerializer
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()

    def get_queryset(self):
        return self.queryset.filter(participants=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data, context={'initiator': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ThreadDestroyAPIView(DestroyAPIView):
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()

    def get_queryset(self):
        return self.queryset.filter(participants=self.request.user)


class MessageCreateListAPIView(ListCreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()
    filterset_fields = ('is_read',)

    def get_queryset(self):
        return self.queryset.filter(
            thread__participants=self.request.user,
            thread_id=self.kwargs['thread_id']
        ).order_by('-created_at')

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data={
                **request.data,
                'sender': request.user.id,
                'thread': kwargs.get('thread_id'),
            }
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MarkMessageAsReadAPIView(UpdateAPIView):
    serializer_class = ThreadSerializer
    queryset = Message.objects.all()

    def get_queryset(self):
        return self.queryset.filter(
            thread__participants=self.request.user,
            is_read=False
        ).exclude(
            sender=self.request.user
        )

    def update(self, request, *args, **kwargs):
        message = self.get_object()
        message.is_read = True
        message.save(update_fields=['is_read'])
        return Response(status=status.HTTP_200_OK)
