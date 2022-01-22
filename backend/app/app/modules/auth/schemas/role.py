from typing import Optional
from pydantic import BaseModel


class RoleBase(BaseModel):
    name: str
    description: str


class RoleInDB(RoleBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Role(RoleInDB):
    pass
