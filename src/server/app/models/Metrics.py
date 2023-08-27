from django.db.models import AutoField, ForeignKey, TextField, DateTimeField, CASCADE
from django_paranoid.models import ParanoidModel


class Metrics(ParanoidModel):
    id = AutoField(primary_key=True)
    value = TextField()
    measure_datetime = DateTimeField()
    config = ForeignKey("MetricsConfig", on_delete=CASCADE)
