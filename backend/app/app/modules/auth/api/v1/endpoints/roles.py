from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.core.security import check_permissions
from app.modules.auth import models, schemas, repositories

router = APIRouter()


@router.get("/", response_model=List[schemas.Role])
def read_roles(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> List[schemas.Role]:
    """
    Retrieve roles.
    """
    check_permissions(current_user, ['role.list'])
    roles = repositories.role.get_multi(db)
    return roles
