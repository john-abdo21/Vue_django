from django.core.management.base import BaseCommand, CommandParser
from django.db import transaction
from app.database import seeders


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--name", nargs="?", default="", type=str)

    @transaction.atomic
    def handle(self, *args, **options) -> None:
        name = options["name"]
        if name != "":
            try:
                seeder = getattr(seeders, name)
                seeder.exec()
            except:
                print(f"'{name}' is unknown seeder.")
        else:
            for handler in seeders.handlers:
                handler.exec()
