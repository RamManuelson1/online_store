from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Клавиатура', 'dictionary': 'Беспроводная'},
            {'name': 'Монитор', 'dictionary': '23 дюйма'},
            {'name': 'Веб-камера', 'dictionary': '20 мегапикселей'},
        ]

        category_for_create = []
        for cat_item in category_list:
            category_for_create.append(
                Category(**cat_item)
            )

        Category.objects.bulk_create(category_for_create)