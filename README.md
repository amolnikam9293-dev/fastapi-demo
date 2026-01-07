# FastAPI Demo Application

A modern, full-stack web application built with **FastAPI** backend and **React** frontend, demonstrating best practices for building scalable APIs with Python.

## 🎯 Project Overview

This project showcases a complete FastAPI application with:
- RESTful API endpoints with automatic OpenAPI documentation
- SQLAlchemy database models for data persistence
- Pydantic validation for request/response data
- React frontend for user interaction
- Production-ready architecture

## 📁 Project Structure

```
fastapi-demo/
├── main.py                 # FastAPI application entry point
├── models.py               # Pydantic response/request models
├── database.py             # Database configuration and session management
├── database_models.py      # SQLAlchemy ORM models
├── .github/
│   └── instructions/       # Development guidelines
├── frontend/               # React application
│   ├── public/             # Static assets
│   ├── src/                # React components
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   ├── index.css
│   │   ├── TaglineSection.js
│   │   └── TaglineSection.css
│   └── package.json
├── myvenv/                 # Python virtual environment
├── requirements.txt        # Python dependencies (recommended)
└── .gitignore             # Git ignore rules

```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js 14+ (for frontend)
- pip and npm package managers

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-demo
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic python-dotenv
   ```

4. **Run the FastAPI server**
   ```bash
   fastapi dev main.py
   ```
   The API will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm start
   ```
   The frontend will be available at `http://localhost:3000`

## 📚 API Documentation

Once the FastAPI server is running, access the interactive API documentation:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **OpenAPI Schema**: http://127.0.0.1:8000/openapi.json

## 🏗️ Architecture

### Backend Structure

#### [main.py](main.py)
The main FastAPI application file containing:
- FastAPI app initialization
- Route definitions
- CORS configuration
- Middleware setup

#### [models.py](models.py)
Pydantic data models for:
- Request validation
- Response serialization
- Type hints and documentation

#### [database_models.py](database_models.py)
SQLAlchemy ORM models defining:
- Database table schemas
- Relationships
- Column constraints

#### [database.py](database.py)
Database configuration:
- Connection string setup
- Session management
- Engine initialization

### Frontend Structure

The React frontend includes:
- **App.js**: Main application component
- **TaglineSection.js**: Reusable component for tagline display
- **index.js**: Application entry point
- **CSS files**: Styling for components

## 🔧 Technology Stack

### Backend
- **FastAPI** (0.128.0) - Modern web framework
- **Uvicorn** - ASGI server
- **SQLAlchemy** - ORM for database operations
- **Pydantic** (2.12.5) - Data validation
- **Python** (3.9+)

### Frontend
- **React** - UI library
- **Node.js** - Runtime environment
- **npm** - Package manager

### Database
- SQLAlchemy-compatible (SQLite, PostgreSQL, MySQL, etc.)

## 📝 Usage Examples

### Creating an API Endpoint

```python
from fastapi import FastAPI
from models import Item

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### Adding Database Models

```python
from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
```

## 🔐 Security Best Practices

This project follows Snyk security guidelines:

- Regular security scanning with Snyk
- Input validation using Pydantic
- SQL injection prevention with SQLAlchemy parameterized queries
- CORS configuration for cross-origin requests
- Environment variable management for sensitive data

See [.github/instructions/snyk_rules.instructions.md](.github/instructions/snyk_rules.instructions.md) for detailed security practices.

## 🧪 Testing

To run tests (when implemented):

```bash
pytest tests/
```

## 📦 Dependencies

### Python Packages
- fastapi>=0.128.0
- uvicorn[standard]>=0.12.0
- sqlalchemy>=2.0.0
- pydantic>=2.7.0
- python-dotenv>=0.19.0

### Node Packages
See [frontend/package.json](frontend/package.json) for all frontend dependencies.

## 🌍 Environment Variables

Create a `.env` file in the root directory:

```env
# Database
DATABASE_URL=sqlite:///./test.db

# API Configuration
API_TITLE=FastAPI Demo
API_VERSION=1.0.0

# CORS
ALLOWED_ORIGINS=http://localhost:3000
```

## 📖 Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [React Documentation](https://react.dev/)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 💡 Tips

- Use `fastapi dev main.py` for automatic reload during development
- Access Swagger UI at `/docs` for API testing
- Use Pydantic's validation features to ensure data integrity
- Implement proper error handling and logging
- Follow async/await patterns for better performance

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port
fastapi dev main.py --port 8001
```

### Virtual Environment Issues
```bash
# Recreate virtual environment
rm -rf myvenv
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
```

### Frontend Build Issues
```bash
# Clear npm cache
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

## 📧 Support

For issues, questions, or suggestions, please open an GitHub issue or contact the development team.

---

**Last Updated**: 2024
**Maintainer**: Amol Nikam
