# 🐸 Toado API

> A FastAPI-based todo management backend with a playful toad theme

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688.svg)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.23-red.svg)](https://www.sqlalchemy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Toado is a production-ready REST API for todo management, built with modern Python best practices. It features comprehensive CRUD operations, input validation, auto-generated documentation, and a modular architecture designed for scalability.

## ✨ Features

### Core Functionality
- ✅ **Full CRUD operations** for todos with filtering and pagination
- ✅ **Input validation** with Pydantic (title, description, status, priority, due dates)
- ✅ **Auto-generated documentation** (Swagger UI & ReDoc)
- ✅ **Request logging middleware** with performance timing
- ✅ **SQLAlchemy ORM** with SQLite (easily swappable to PostgreSQL)
- ✅ **Comprehensive test suite** (17 tests passing)
- ✅ **Postman collection** for API testing

### Architecture Highlights
- 🏗️ **Modular design** with clear separation of concerns
- 🔌 **Repository pattern** for data access abstraction
- 🎯 **Dependency injection** for database sessions
- 📝 **Type hints** throughout the codebase
- 🧪 **Test-driven development** ready
- 🚀 **Production-ready** with proper error handling

### Future-Ready
The codebase includes placeholders for Phase 2 enhancements:
- 🔐 JWT authentication
- 👥 User management
- 🛡️ Admin endpoints
- ⏱️ Rate limiting
- 📧 Email verification

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Testing](#-testing)
- [Development](#-development)
- [Deployment](#-deployment)
- [Roadmap](#️-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

#### Windows

```powershell
# Clone the repository
git clone https://github.com/hassanalzahrani-1/toado.git
cd toado

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1
# If you get execution policy error, use:
# Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

#### Linux/macOS

```bash
# Clone the repository
git clone https://github.com/hassanalzahrani-1/toado.git
cd toado

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```

### Access the API

Once running, access the following endpoints:

- **API Root**: http://localhost:8000
- **Interactive Docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative Docs (ReDoc)**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 📁 Project Structure

```
toado/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app entry point, middleware setup
│   ├── config.py               # Environment-based configuration
│   ├── db.py                   # Database engine and session management
│   ├── models.py               # SQLAlchemy ORM models (Todo, enums)
│   ├── schemas.py              # Pydantic models for validation
│   ├── middleware.py           # Custom middleware (logging, timing)
│   ├── dependencies/           # Reusable FastAPI dependencies
│   │   ├── __init__.py
│   │   ├── db.py              # Database session injection
│   │   ├── auth.py            # Auth dependency (Phase 2 placeholder)
│   │   └── rate_limit.py      # Rate limiter (Phase 2 placeholder)
│   ├── repositories/           # Data access layer
│   │   ├── __init__.py
│   │   └── todos.py           # Todo CRUD operations
│   ├── routers/                # API route handlers
│   │   ├── __init__.py
│   │   └── todos.py           # Todo endpoints
│   └── services/               # Business logic layer
│       ├── __init__.py
│       ├── auth.py            # JWT service (Phase 2 placeholder)
│       └── email.py           # Email service (Phase 2 placeholder)
├── tests/
│   ├── __init__.py
│   └── test_todos.py          # Comprehensive test suite
├── .gitignore
├── requirements.txt
├── Toado_API.postman_collection.json
├── Toado_API.postman_environment.json
└── README.md
```

## 📚 API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

#### Health Check

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message with API info |
| GET | `/health` | Health check status |

#### Todos

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/todos` | Create a new todo | No |
| GET | `/todos` | List all todos (with filters) | No |
| GET | `/todos/{id}` | Get a specific todo | No |
| PUT | `/todos/{id}` | Update a todo | No |
| DELETE | `/todos/{id}` | Delete a todo | No |

### Request/Response Examples

#### Create Todo

**Request:**
```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive README",
    "status": "pending",
    "priority": "high",
    "due_date": "2025-10-15T12:00:00Z"
  }'
```

**Response:**
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write comprehensive README",
  "status": "pending",
  "priority": "high",
  "due_date": "2025-10-15T12:00:00Z",
  "created_at": "2025-10-07T13:00:00Z",
  "updated_at": "2025-10-07T13:00:00Z"
}
```

#### List Todos with Filters

**Request:**
```bash
curl "http://localhost:8000/todos?status=pending&priority=high&limit=10"
```

**Query Parameters:**
- `status` - Filter by status (`pending`, `in_progress`, `completed`)
- `priority` - Filter by priority (`low`, `medium`, `high`)
- `due_before` - Filter by due date (ISO 8601 format)
- `skip` - Number of records to skip (pagination)
- `limit` - Maximum records to return (default: 100)

### Data Models

#### Todo

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | integer | Auto | Unique identifier |
| `title` | string | Yes | Todo title (1-200 chars) |
| `description` | string | No | Detailed description (max 2000 chars) |
| `status` | enum | No | Status: `pending`, `in_progress`, `completed` |
| `priority` | enum | No | Priority: `low`, `medium`, `high` |
| `due_date` | datetime | No | Due date (ISO 8601, must be future) |
| `created_at` | datetime | Auto | Creation timestamp |
| `updated_at` | datetime | Auto | Last update timestamp |

## 🧪 Testing

### Run All Tests

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_todos.py -v
```

### Test Coverage

The test suite includes:
- ✅ CRUD operations (create, read, update, delete)
- ✅ Input validation (empty titles, past due dates)
- ✅ Filtering (status, priority, due date)
- ✅ Pagination (skip, limit)
- ✅ Error handling (404 not found)
- ✅ Health check endpoints

**Current Coverage**: 17 tests, all passing ✅

## 🔧 Development

### Code Style Guidelines

- Follow **PEP 8** style guide
- Use **type hints** for all function signatures
- Write **docstrings** for all public functions and classes
- Keep functions **small and focused** (single responsibility)
- Use **meaningful variable names**
- Add **comments** for complex logic

### Adding New Features

1. **Create a new model** in `app/models.py`
2. **Define Pydantic schemas** in `app/schemas.py`
3. **Implement repository** in `app/repositories/`
4. **Create router** in `app/routers/`
5. **Write tests** in `tests/`
6. **Update documentation**

### Architecture Patterns

#### Repository Pattern
Abstracts data access logic from business logic:
```python
# app/repositories/todos.py
def create_todo(db: Session, todo_data: TodoCreate) -> Todo:
    todo = Todo(**todo_data.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
```

#### Dependency Injection
FastAPI's dependency system for clean code:
```python
# app/routers/todos.py
@router.post("/todos")
def create_todo(
    todo_data: TodoCreate,
    db: Session = Depends(get_db),  # Injected dependency
):
    return todo_repo.create_todo(db, todo_data)
```

## 🧰 Postman Collection

A comprehensive Postman collection is included for easy API testing.

### Import Instructions

1. Open Postman
2. Click **Import** button
3. Select both files:
   - `Toado_API.postman_collection.json`
   - `Toado_API.postman_environment.json`
4. Select the **Toado API - Local** environment
5. Start making requests!

### Collection Contents

- ✅ **Health endpoints** - Root and health check
- ✅ **CRUD operations** - Create, read, update, delete
- ✅ **Filtering examples** - Status, priority, due date
- ✅ **Pagination** - Skip and limit parameters
- ✅ **Error cases** - Validation errors, 404 handling
- ✅ **Auto-capture** - `todo_id` saved after creation

## 🚀 Deployment

### Environment Variables

Create a `.env` file in the project root:

```env
# Database
DATABASE_URL=sqlite:///./toado.db

# Application
APP_TITLE=Toado API
APP_VERSION=1.0.0

# JWT (Phase 2)
JWT_SECRET_KEY=your-secret-key-change-in-production
JWT_ALGORITHM=HS256
```

### Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t toado-api .
docker run -p 8000:8000 toado-api
```

### Production Considerations

- Use **PostgreSQL** instead of SQLite
- Set `echo=False` in database engine
- Configure **CORS** origins properly
- Enable **HTTPS** with SSL certificates
- Set up **logging** to files or external service
- Use **environment variables** for secrets
- Implement **rate limiting** (Phase 2)
- Add **monitoring** and **health checks**

## 🗺️ Roadmap

### Phase 1 - Groundwork ✅ (Current)
- [x] Full CRUD operations
- [x] Input validation
- [x] Auto-generated documentation
- [x] Request logging middleware
- [x] SQLAlchemy with SQLite
- [x] Comprehensive test suite
- [x] Postman collection

### Phase 2 - Enhanced Version (Planned)
- [ ] User registration and login
- [ ] JWT authentication
- [ ] User-specific todos
- [ ] Admin endpoints
- [ ] Rate limiting with Redis
- [ ] Email verification (mock)
- [ ] Password reset functionality
- [ ] Role-based access control

### Phase 3 - Full Stack (Future)
- [ ] React/Vue frontend
- [ ] Real-time updates (WebSockets)
- [ ] File attachments
- [ ] Todo sharing and collaboration
- [ ] Mobile app (React Native)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/toado.git
cd toado

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [Uvicorn](https://www.uvicorn.org/) - ASGI server

## 📞 Contact

**Hassan Alzahrani** - [@hassanalzahrani-1](https://github.com/hassanalzahrani-1)

Project Link: [https://github.com/hassanalzahrani-1/toado](https://github.com/hassanalzahrani-1/toado)

---

<div align="center">
  Made with ❤️ by a very powerful Toad 🐸
</div>
