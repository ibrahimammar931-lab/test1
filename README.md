# TaskFlow API — baseline

This is the **pre-ticket-1** state of the project described in
`test-project-tickets.md`. Point your A2A orchestrator's `GITHUB_REPO_URL`
at a repo containing this code, then work through the 15 tickets in order.

## Running locally

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive API docs.

## Running tests

```bash
pytest
```

Note: `tests/test_tasks.py::test_get_missing_task_404` currently asserts the
**buggy** `"Tast not found"` message on purpose — it's the fixture for
Ticket 1, and should be updated (not just made to pass) once that ticket is
implemented correctly.

## Known baseline gaps (intentional — these are what the tickets fix)

- `routes/tasks.py`: typo in the 404 detail message (Ticket 1).
- No `/health` endpoint (Ticket 2).
- `Task` has no `due_date` field (Ticket 3).
- No `DELETE /projects/{id}` endpoint (Ticket 4).
- `TaskCreate.title` has no length/emptiness validation (Ticket 5).
- `GET /tasks` is unpaginated (Ticket 6).
- No caching on `GET /projects/{id}` (Ticket 7).
- No task duplication endpoint (Ticket 8).
- `Task.status` is a free-text string, not an enum with transition rules (Ticket 9).
- `GET /projects/{id}` and task queries have no ownership/membership
  authorization — any authenticated user can read/write any project by ID
  (Ticket 10 — this is a real, deliberately-placed vulnerability for testing).
- No audit logging (Ticket 11).
- No rate limiting (Ticket 12).
- Auth is a single long-lived JWT with no rotation/revocation (Ticket 13).
- No Redis-backed cache invalidation across instances (Ticket 14).
- No `Tenant`/billing model at all (Ticket 15).
