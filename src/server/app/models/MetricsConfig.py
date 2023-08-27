from django.db.models import AutoField, CharField
from django_paranoid.models import ParanoidModel


class MetricsConfig(ParanoidModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    unit = CharField(max_length=20, blank=True, null=True)
