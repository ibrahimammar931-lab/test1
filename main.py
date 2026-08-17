from __future__ import annotations

from fastapi import FastAPI

from config import settings
from database import Base, engine
from models import project, task, user  # noqa: F401 — ensures models are registered on Base
from routes import auth, projects, tasks, users, health, version

app = FastAPI(title=settings.APP_NAME)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(health.router)
app.include_router(version.router)


@app.on_event("startup")
def on_startup() -> None:
    # NOTE: for local/dev convenience only. In a real deployment this
    # baseline would be replaced entirely by Alembic migrations — see
    # migrations/versions/ for where schema changes should go from here on.
    Base.metadata.create_all(bind=engine)
