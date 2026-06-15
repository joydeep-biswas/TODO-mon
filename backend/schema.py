from pydantic import BaseModel

class TaskCreateRequest(BaseModel):
    title: str
    description: str

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

    class Config:
        from_attributes = True

class TaskUpdateRequest(BaseModel):
    title: str
    description: str
    is_completed: bool

class TaskUpdateResponse(BaseModel):
    title: str
    description: str
    is_completed: str

class TaskStatusChangeRequest(BaseModel):
    is_completed: bool

class TaskStatusChangeResponse(BaseModel):
    title: str
    is_completed: bool

class TaskDeleteResponse(BaseModel):
    title: str