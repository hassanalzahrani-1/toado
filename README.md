# Toado API

A FastAPI-based todo management backend with a playful toad theme.

## Features (Phase 1 - Groundwork)

- **Full CRUD operations** for todos
- **Input validation** with Pydantic
- **Auto-generated documentation** (Swagger UI & ReDoc)
- **Request logging middleware**
- **SQLAlchemy** data layer with SQLite
- **Modular architecture** ready for future enhancements

## Future Enhancements (Phase 2)

- User registration/login with JWT authentication
- User-specific todos
- Admin endpoints
- Rate limiting
- Email verification (mock)

## Project Structure

```
toado/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py               # Configuration settings
│   ├── db.py                   # Database setup
│   ├── models.py               # SQLAlchemy ORM models
│   ├── schemas.py              # Pydantic schemas
│   ├── middleware.py           # Custom middleware
│   ├── dependencies/           # FastAPI dependencies
│   │   ├── __init__.py
│   │   ├── db.py
│   │   ├── auth.py
│   │   └── rate_limit.py
│   ├── repositories/           # Data access layer
│   │   ├── __init__.py
│   │   └── todos.py
│   ├── routers/                # API routes
│   │   ├── __init__.py
│   │   └── todos.py
│   └── services/               # Business logic
│       ├── __init__.py
│       ├── auth.py
│       └── email.py
├── tests/
│   ├── __init__.py
│   └── test_todos.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/hassanalzahrani-1/toado.git
   cd toado
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API**
   - API: http://localhost:8000
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Development

### Running Tests
```bash
pytest
```

### Code Style
Follow PEP 8 guidelines and use type hints throughout.

## API Endpoints

### Todos
- `POST /todos` - Create a new todo
- `GET /todos` - List all todos (with optional filters)
- `GET /todos/{todo_id}` - Get a specific todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

## Postman Collection

Import the Postman collection and environment for easy API testing:

1. **Collection**: `Toado_API.postman_collection.json`
2. **Environment**: `Toado_API.postman_environment.json`

The collection includes:
- All CRUD operations
- Filter examples (status, priority, due date)
- Pagination examples
- Error case testing
- Auto-capture of `todo_id` after creation

## License

MIT
