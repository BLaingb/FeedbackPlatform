from typing import List, Optional
from pydantic import BaseModel

from app.modules.chapters.schemas.dependencies import ChapterUser


class ChapterBase(BaseModel):
    name: Optional[str] = None


class ChapterCreate(ChapterBase):
    name: str
    chapter_lead_id: int


class ChapterUpdate(ChapterBase):
    chapter_lead_id: Optional[int] = None


class ChapterInDBBase(ChapterBase):
    id: Optional[int] = None
    chapter_lead_id: Optional[int] = None

    class Config:
        orm_mode = True


class ChapterListOut(ChapterInDBBase):
    chapter_lead: Optional[ChapterUser] = None


class ChapterOut(ChapterListOut):
    members: Optional[List[ChapterUser]] = None
