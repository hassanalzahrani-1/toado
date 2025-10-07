"""SQLAlchemy ORM models."""
from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, Float

from app.db import Base


class TodoStatus(str, PyEnum):
    """Todo status enumeration."""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class TodoPriority(str, PyEnum):
    """Todo priority enumeration."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Todo(Base):
    """Todo ORM model."""
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=True)
    status = Column(Enum(TodoStatus), default=TodoStatus.PENDING, nullable=False, index=True)
    priority = Column(Enum(TodoPriority), default=TodoPriority.MEDIUM, nullable=False, index=True)
    due_date = Column(DateTime, nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Placeholder for Phase 2: user ownership
    # owner_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    # owner = relationship("User", back_populates="todos")
