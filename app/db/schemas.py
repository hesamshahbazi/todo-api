from pydantic import BaseModel
from typing import Optional


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    is_done: Optional[bool] = None

class TaskCreate(BaseModel):
    title: str

class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool

    class Config:
        from_attributes = True