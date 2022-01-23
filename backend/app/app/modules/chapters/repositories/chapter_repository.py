from typing import Optional
from sqlalchemy.orm import Session
from app.modules.chapters.models.chapter import Chapter
from app.modules.chapters.schemas.chapter import ChapterCreate, ChapterUpdate
from app.repositories.base import BaseRepository


class ChapterRepository(BaseRepository[Chapter, ChapterCreate, ChapterUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Chapter]:
        return db.query(Chapter).filter(Chapter.name == name).first()


chapter = ChapterRepository(Chapter)
