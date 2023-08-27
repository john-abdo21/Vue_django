from django.db.models import (
    AutoField,
    ForeignKey,
    BooleanField,
    TextField,
    CASCADE,
    SET_NULL,
)
from django_paranoid.models import ParanoidModel


class Message(ParanoidModel):
    id = AutoField(primary_key=True)
    channel = ForeignKey("Channel", on_delete=CASCADE)
    user = ForeignKey("User", on_delete=CASCADE)
    body = TextField()
    thread_message = ForeignKey("Message", blank=True, null=True, on_delete=SET_NULL)
    is_thread = BooleanField(default=False)
