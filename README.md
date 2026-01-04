# Pipeline Dev Home

Homepage microservice for the msite application.

## Features

- Homepage at /
- Health check endpoint at /health/
- Stateless service with no database requirements
- Whitenoise for static file serving

## Installation

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. Run development server:
   ```bash
   python manage.py runserver
   ```

5. Test endpoints:
   - Homepage: http://localhost:8000/
   - Health: http://localhost:8000/health/

## Production Deployment

```bash
gunicorn homepage.wsgi:application --bind 0.0.0.0:8000
```

## Environment Variables

- `SECRET_KEY`: Django secret key (default: 'dev-secret-key')
- `DEBUG`: Enable debug mode (default: 'False')
- `ALLOWED_HOSTS`: Allowed hosts (default: '*')
