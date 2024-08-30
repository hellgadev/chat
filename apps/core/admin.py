from django.contrib import admin
from django.contrib.auth.models import Group

from apps.core.models import Thread, Message


class MessageInline(admin.TabularInline):
    model = Message
    extra = 1
    max_num = 1
    min_num = 1

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class ThreadAdmin(admin.ModelAdmin):
    inlines = (MessageInline, )
    list_display = ('id', 'get_chat_participants', 'created_at', 'updated_at')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def get_chat_participants(self, obj):
        return ", ".join([p.username for p in obj.participants.all()])

    get_chat_participants.short_description = 'Participants'


admin.site.register(Thread, ThreadAdmin)
admin.site.unregister(Group)

