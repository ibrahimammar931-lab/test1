from __future__ import annotations

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.project import Project
from models.task import Task


def delete_project(db: Session, project_id: str, current_user_id: str) -> None:
    project = db.get(Project, project_id)
    if project is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    if project.owner_id != current_user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not the project owner")

    try:
        db.query(Task).filter(Task.project_id == project.id).delete()
        db.delete(project)
        db.commit()
    except Exception:
        db.rollback()
        raise
