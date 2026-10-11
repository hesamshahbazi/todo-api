from pydantic import BaseModel, ConfigDict, StringConstraints
from typing import Annotated

Title = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=500)]
from typing import Optional


class TaskUpdate(BaseModel):
    title: Optional[Title] = None
    is_done: Optional[bool] = None

class TaskCreate(BaseModel):
    title: Title

class TaskOut(BaseModel):
    id: int
    title: Title
    is_done: bool

    model_config = ConfigDict(from_attributes=True)