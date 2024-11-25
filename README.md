# Django Notes API

A simple RESTful API built with Django and Tastypie for managing notes.

## Features

- Create, Read, Update, and Delete notes
- Each note contains a title and body
- Automatic timestamp creation
- RESTful endpoints
- JSON format support

## Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Lkanth05/RESTful-API
cd RESTful-API
```

2. Create and activate a virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/v1/`

## API Endpoints

Base URL: `http://localhost:8000/api/v1/`

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/note/` | GET | List all notes | None |
| `/note/` | POST | Create a new note | title, body |
| `/note/{id}/` | GET | Retrieve a specific note | None |
| `/note/{id}/` | PUT | Update a specific note | title, body |
| `/note/{id}/` | DELETE | Delete a specific note | None |

## API Testing with Insomnia

1. Download and install [Insomnia](https://insomnia.rest/download)

2. Create a new Collection in Insomnia

3. Example requests:

### List all notes
- Method: GET
- URL: `http://localhost:8000/api/v1/note/`

### Create a note
- Method: POST
- URL: `http://localhost:8000/api/v1/note/`
- Headers: 
  - Content-Type: application/json
- Body:
```json
{
    "title": "Sample Note",
    "body": "This is a sample note body"
}
```

### Get a specific note
- Method: GET
- URL: `http://localhost:8000/api/v1/note/1/`

### Update a note
- Method: PUT
- URL: `http://localhost:8000/api/v1/note/1/`
- Headers:
  - Content-Type: application/json
- Body:
```json
{
    "title": "Updated Title",
    "body": "Updated body content"
}
```

### Delete a note
- Method: DELETE
- URL: `http://localhost:8000/api/v1/note/1/`

## Project Structure

```
RESTAPI/
├── api/
│   ├── __init__.py
│   ├── models.py          # Contains Note model
│   ├── resources.py       # Contains API resource 
├── RESTAPI/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## Requirements.txt

```
django>=4.2.0
django-tastypie>=0.14.5
```

## Common Issues and Solutions

1. **CORS Issues**: If you're accessing the API from a different domain, ensure CORS is properly configured in settings.py:
```python
INSTALLED_APPS = [
    ...
    'api',
    ...
]



CORS_ALLOW_ALL_ORIGINS = True  # Development only!
```

2. **Database Migrations**: If you encounter database issues, try:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

