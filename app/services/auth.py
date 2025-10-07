"""Authentication service (placeholder for Phase 2)."""
from datetime import datetime, timedelta
from typing import Optional


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token (placeholder for Phase 2).
    
    Phase 2 will implement actual JWT encoding using python-jose.
    """
    raise NotImplementedError("JWT authentication will be implemented in Phase 2")


def verify_token(token: str) -> dict:
    """
    Verify and decode a JWT token (placeholder for Phase 2).
    
    Phase 2 will implement actual JWT verification using python-jose.
    """
    raise NotImplementedError("JWT authentication will be implemented in Phase 2")


def hash_password(password: str) -> str:
    """
    Hash a password (placeholder for Phase 2).
    
    Phase 2 will implement password hashing using passlib.
    """
    raise NotImplementedError("Password hashing will be implemented in Phase 2")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash (placeholder for Phase 2).
    
    Phase 2 will implement password verification using passlib.
    """
    raise NotImplementedError("Password verification will be implemented in Phase 2")
