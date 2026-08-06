def _create_project(client, auth_headers):
    resp = client.post(
        "/projects", json={"name": "Test Project", "description": "desc"}, headers=auth_headers
    )
    return resp.json()["id"]


def test_create_and_get_task(client, auth_headers):
    project_id = _create_project(client, auth_headers)
    create_resp = client.post(
        "/tasks",
        json={"title": "Write docs", "project_id": project_id},
        headers=auth_headers,
    )
    assert create_resp.status_code == 201
    task_id = create_resp.json()["id"]

    get_resp = client.get(f"/tasks/{task_id}", headers=auth_headers)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Write docs"


def test_get_missing_task_404(client, auth_headers):
    resp = client.get("/tasks/does-not-exist", headers=auth_headers)
    assert resp.status_code == 404
    # NOTE: this currently asserts the *buggy* baseline message on purpose,
    # so Ticket 1 has a failing test to fix once the typo is corrected.
    assert resp.json()["detail"] == "Tast not found"


def test_delete_task(client, auth_headers):
    project_id = _create_project(client, auth_headers)
    create_resp = client.post(
        "/tasks", json={"title": "Temp task", "project_id": project_id}, headers=auth_headers
    )
    task_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/tasks/{task_id}", headers=auth_headers)
    assert delete_resp.status_code == 204

    get_resp = client.get(f"/tasks/{task_id}", headers=auth_headers)
    assert get_resp.status_code == 404
