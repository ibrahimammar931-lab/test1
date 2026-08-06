from __future__ import annotations
from datetime import date
from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: str
    due_date: date | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    due_date: date | None = None

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: str | None
    status: str
    project_id: str
    due_date: date | None