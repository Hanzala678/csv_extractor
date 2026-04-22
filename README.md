# CSV Processor

A Django application for processing CSV files.

## Recommended

Create a virtual environment and activate it
   '''
   python -m venv .venv
   .venv/Scripts/activate
   '''

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   python manage.py migrate
   ```

3. Start the server:
   ```
   python manage.py runserver
   ```

## Usage

- Upload CSV files via the upload page.
- View processing history.

## Troubleshooting

- Ensure Django is installed.
- Check database configuration in settings.py.