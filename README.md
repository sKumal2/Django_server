# Django Server

A Django project containing the `home` and `communities` applications.

## Setup

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install Django:

   ```bash
   pip install django
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

## Run

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

## Tests

```bash
python manage.py test
```