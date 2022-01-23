

from pydantic import BaseModel, EmailStr


class ChapterUser(BaseModel):
    email: EmailStr
    full_name: str

    class Config:
        orm_mode = True


class AuthChapter(BaseModel):
    name: str
    chapter_lead: ChapterUser

    class Config:
        orm_mode = True
