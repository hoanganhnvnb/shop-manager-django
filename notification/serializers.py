from rest_framework import serializers

from .models import Notification


class NotificationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('id', 'title', 'content', 'user', 'create_at', 'is_read')

class NotificationReadSerializers(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('is_read', )
