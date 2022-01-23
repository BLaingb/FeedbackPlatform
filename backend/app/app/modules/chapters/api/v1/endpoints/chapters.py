from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.core.security import check_permissions
from app.modules.auth import models as auth_models
from app.modules.chapters import repositories, schemas
from app.modules.auth import repositories as auth_repositories

router = APIRouter()


@router.get("/", response_model=List[schemas.ChapterListOut])
def read_chapters(
    *,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: auth_models.User = Depends(deps.get_current_active_user)
):
    check_permissions(current_user, ['chapter.list'])
    chapters = repositories.chapter.get_multi(db, skip=skip, limit=limit)
    return chapters


@router.post("/", response_model=schemas.ChapterOut)
def create_chapter(
    *,
    db: Session = Depends(deps.get_db),
    chapter_in: schemas.ChapterCreate,
    current_user: auth_models.User = Depends(deps.get_current_active_user),
):
    check_permissions(current_user, ['chapter.create'])
    chapter = repositories.chapter.get_by_name(db, name=chapter_in.name)
    if chapter:
        raise HTTPException(
            status_code=400,
            detail="A chapter with this name already exists in the system."
        )

    chapter_lead = auth_repositories.user.get(db, chapter_in.chapter_lead_id)
    if not chapter_lead:
        raise HTTPException(
            status_code=400,
            detail="The provided chapter lead id does not exist in the system."
        )
    chapter = repositories.chapter.create(db, obj_in=chapter_in)
    return chapter
