# Railway App

Railway App — это проект на Django, предназначенный для управления данными о грузовых поездах и их вагонах.
 С помощью этого приложения вы можете загружать данные из CSV-файлов, просматривать, добавлять и редактировать информацию о поездах и вагонах через RESTful API.

## Установка

Прежде чем начать, убедитесь, что у вас установлены следующее:

- [Python 3.7+](https://www.python.org/downloads/)
- [Django 3.2+](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)

### Шаги установки

1. **Клонируйте репозиторий**:
```bash
   git clone https://github.com/m14el/railway

2.Перейдите в директорию проекта:
   cd railway_project

3.Создайте виртуальное окружение:
   python -m venv venv

4.Активируйте виртуальное окружение:
	На Windows:
    	 .\venv\Scripts\activate
	На macOS/Linux:
    	 source venv/bin/activate
5.Установите зависимости:
   pip install -r requirements.txt

6.Настройка базы данных:
Убедитесь, что у вас установлен PostgreSQL. Настройте параметры базы данных в settings.py.

7.Примените миграции:
   python manage.py migrate

8.Запустите сервер:
   python manage.py runserver

9.Загрузите данные из CSV:
Вы можете загрузить данные о вагонах, используя команду:
   python manage.py load_wagons "C:\path\to\your\wagons_data.csv"

10.Использование API
Теперь вы можете делать запросы к вашему API:

10.1.Получить список вагонов:
  GET http://127.0.0.1:8000/api/wagons/

10.2.Получить информацию о вагоне по ID:
  GET http://127.0.0.1:8000/api/wagons/&lt;id&gt;/

10.3.Добавить новый вагон:
  POST http://127.0.0.1:8000/api/wagons/

10.4.Обновить данные о вагоне:
  PUT http://127.0.0.1:8000/api/wagons/&lt;id&gt;/

10.5.Удалить вагон:
  DELETE http://127.0.0.1:8000/api/wagons/&lt;id&gt;/
