from app.models import Priority


def exec():
    Priority.objects.all().delete()

    default_priorities = [
        Priority(name="高", order=1),
        Priority(name="通常", order=2),
        Priority(name="低", order=3),
    ]

    Priority.objects.bulk_create(default_priorities)
