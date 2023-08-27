from django.db.models import OneToOneField, CASCADE
from django_paranoid.models import ParanoidModel


class DivisionTree(ParanoidModel):
    parent = OneToOneField(
        "Division",
        related_name="DivisionTree.parent+",
        on_delete=CASCADE,
    )
    child = OneToOneField(
        "Division",
        related_name="DivisionTree.child+",
        on_delete=CASCADE,
    )
