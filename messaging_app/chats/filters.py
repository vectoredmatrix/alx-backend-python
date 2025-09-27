import django_filters
from .models import Message


class MessageFilter(django_filters.FilterSet):
    class Meta:
        model = Message
        fields = {
            "sender_id" : ["exact"],
            "sent_at":["range"]
        }
        