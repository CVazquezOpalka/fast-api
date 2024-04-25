from typing import Optional
from pydantic import BaseModel, Field


class Notification(BaseModel):
    id: Optional[str] = None
    title: str
    start: str
    end: str


class CreateNotification(BaseModel):
    title: str
    title: str
    start: str
    end: str
