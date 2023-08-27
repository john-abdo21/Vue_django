from django.core.management.base import BaseCommand, CommandParser
from django.db import transaction
from app.models import User, Role
from app.database import seeders


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options) -> None:
        seeders.priority.exec()
        seeders.role.exec()

        user = User(
            login_id="admin",
            first_name="管理者",
            last_name="システム",
            en_first_name="Admin",
            en_last_name="System",
            is_superuser=True,
        )

        user.set_password("dashboard2023")
        user.save()
