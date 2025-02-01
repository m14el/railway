from django.core.management.base import BaseCommand
import csv
import os
import django
from wagons_app.models import Wagon

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wagons_project.settings')
django.setup()

class Command(BaseCommand):
    help = 'Load wagon data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        file_path = options['file']
        with open(file_path, newline='', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            print(f'Заголовки: {reader.fieldnames}')
            for row in reader:
                try:
                    Wagon.objects.create(
                        train_number=row['Номер поезда'],
                        sender=row['Грузоотправитель (наим)'],
                        recipient=row['Грузополучатель (наим)'],
                        wagon_number=row['Номер вагона'],
                        waybill_number=row['Номер накладной'],
                        weight=float(row['Вес груза (кг)']),
                        cargo=row['Наименование груза'],
                    )
                except KeyError as e:
                    print(f'Ошибка: столбец {e} отсутствует в строке {row}')
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены в базу данных!'))