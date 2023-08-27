from django.db.models import AutoField, IntegerField, CharField
from django_paranoid.models import ParanoidModel


class Priority(ParanoidModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20)
    order = IntegerField()
