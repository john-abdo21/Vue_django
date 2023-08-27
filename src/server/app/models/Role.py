from django.db.models import AutoField, IntegerField, CharField, BooleanField
from django_paranoid.models import ParanoidModel


class Role(ParanoidModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    is_admin = BooleanField(default=False)
    order = IntegerField()
