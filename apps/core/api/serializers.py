from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from apps.accounts.api.serializers import UserSerializer
from apps.core.models import Thread, Message


class ThreadSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        fields = ALL_FIELDS
        model = Thread

    def create(self, validated_data):
        existing_tread = Thread.objects.filter(participants__in=[validated_data['participants']])
        if existing_tread.exists():
            return existing_tread
        return super().create(validated_data)


class ThreadCreateSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=get_user_model().objects.all()
    )

    class Meta:
        fields = (
            'id',
            'participants',
            'created_at',
            'updated_at',
        )
        model = Thread
        read_only_fields = (
            'created_at',
            'updated_at',
        )

    def validate_participants(self, value):
        if len(value) > 2:
            raise serializers.ValidationError("A chat can have at most 2 participants.")
        elif len(value) <= 1:
            if self.context['initiator'] in value:
                raise serializers.ValidationError("A chat should have 2 participants.")
            else:
                value.append(self.context['initiator'])

        if self.context['initiator'] not in value:
            raise serializers.ValidationError("You must be a participant in the chat.")
        return value

    def create(self, validated_data):
        participants = validated_data.pop('participants', [])

        # Sort participant IDs to ensure the order does not affect the comparison
        participants_ids = sorted([user.id for user in participants])

        existing_tread = Thread.objects.filter(
            participants__id=participants_ids[0]
        ).filter(participants__id=participants_ids[1])

        if existing_tread.exists():
            return existing_tread.first()

        thread = Thread.objects.create(**validated_data)
        thread.participants.set(participants)
        return thread


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'thread',
            'text',
            'created_at',
            'sender',
            'is_read',
        )
        model = Message
        read_only_fields = (
            'created_at',
            'is_read'
        )
