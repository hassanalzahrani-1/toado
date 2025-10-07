"""Pydantic schemas for request/response validation."""
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from app.models import TodoStatus, TodoPriority


class TodoBase(BaseModel):
    """Base schema for Todo with shared fields."""
    title: str = Field(..., min_length=1, max_length=200, description="Todo title")
    description: Optional[str] = Field(None, max_length=2000, description="Todo description")
    status: TodoStatus = Field(default=TodoStatus.PENDING, description="Todo status")
    priority: TodoPriority = Field(default=TodoPriority.MEDIUM, description="Todo priority")
    due_date: Optional[datetime] = Field(None, description="Due date for the todo")
    
    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, v: Optional[datetime]) -> Optional[datetime]:
        """Ensure due_date is not in the past."""
        if v is not None:
            # Make both datetimes timezone-aware for comparison
            now = datetime.now(timezone.utc)
            compare_date = v if v.tzinfo else v.replace(tzinfo=timezone.utc)
            if compare_date < now:
                raise ValueError("due_date cannot be in the past")
        return v


class TodoCreate(TodoBase):
    """Schema for creating a new todo."""
    pass


class TodoUpdate(TodoBase):
    """Schema for updating an existing todo."""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    status: Optional[TodoStatus] = None
    priority: Optional[TodoPriority] = None


class TodoOut(TodoBase):
    """Schema for todo responses."""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


# Placeholder schemas for Phase 2
class UserBase(BaseModel):
    """Base user schema (placeholder for Phase 2)."""
    email: str
    username: str


class UserCreate(UserBase):
    """User creation schema (placeholder for Phase 2)."""
    password: str


class UserOut(UserBase):
    """User response schema (placeholder for Phase 2)."""
    id: int
    is_active: bool = True
    is_admin: bool = False
    
    class Config:
        from_attributes = True


class Token(BaseModel):
    """JWT token response (placeholder for Phase 2)."""
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"
