

from pydantic import BaseModel, EmailStr


class ChapterUser(BaseModel):
    email: EmailStr
    full_name: str

    class Config:
        orm_mode = True
