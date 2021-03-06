from datetime import datetime, timedelta
from fastapi import HTTPException
from typing import Any, List, Union

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings
from app.modules.auth.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None, **kwargs
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject), **kwargs}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def check_permissions(user: User, permissions: List[str]):
    if user.is_superuser:
        return

    user_permissions = user.get_permissions()
    for required_permission in permissions:
        if required_permission not in user_permissions:
            raise HTTPException(
                status_code=403,
                detail="Insufficient Permissions"
            )
