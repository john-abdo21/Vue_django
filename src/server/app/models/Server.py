from django.db.models import (
    AutoField,
    CharField,
    TextField,
    DateTimeField,
    GenericIPAddressField,
)
from django_paranoid.models import ParanoidModel


class Server(ParanoidModel):
    id = AutoField(primary_key=True)
    description = TextField(blank=True, default="")
    ip_address = GenericIPAddressField()
    host_name = CharField(blank=True, default="", max_length=100)
    status = CharField(blank=True, null=True, max_length=1)
    last_status_check_datetime = DateTimeField(blank=True, null=True)
