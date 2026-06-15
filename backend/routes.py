from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sqlalchemy import true, false

from database import SessionLocal
from model import Task
from schema import (
    TaskCreateRequest,
    TaskResponse,
    TaskDeleteResponse,
    TaskUpdateRequest,
    TaskUpdateResponse,
    TaskStatusChangeRequest,
    TaskStatusChangeResponse,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_database():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreateRequest, db: Session = Depends(get_database)):
    new_task = Task(
        title=task.title,
        description=task.description,
        is_completed=False,
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_database)):
    return db.query(Task).all()


@router.delete("/{task_id}", response_model=TaskDeleteResponse)
def delete_task(task_id: int, db: Session = Depends(get_database)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return TaskDeleteResponse(title=str(task.title))


# @router.put("/{task_id}", response_model=TaskUpdateResponse)
# def update_task(
#     task_id: int,
#     payload: TaskUpdateRequest,
#     db: Session = Depends(get_database),
# ):
#     task = db.query(Task).filter(Task.id == task_id).first()

#     if not task:
#         raise HTTPException(status_code=404, detail="Task not found")

#     task.completed = payload.is_completed
#     db.commit()
#     db.refresh(task)

#     return TaskUpdateResponse(
#         title=str(task.title),
#         description=str(task.description),
#         is_completed=str(task.is_completed),
#     )

@router.put("/{task_id}/status", response_model=TaskStatusChangeResponse)
def update_task_status(
    task_id: int,
    payload: TaskStatusChangeRequest,
    db: Session = Depends(get_database),
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.is_completed = payload.is_completed
    db.commit()
    db.refresh(task)

    return TaskStatusChangeResponse(
        title=str(task.title),
        is_completed=bool(task.is_completed),
    )