def test_register_and_login(client):
    register_resp = client.post(
        "/auth/register",
        json={"email": "alice@example.com", "password": "hunter2", "full_name": "Alice"},
    )
    assert register_resp.status_code == 201

    login_resp = client.post(
        "/auth/login", json={"email": "alice@example.com", "password": "hunter2"}
    )
    assert login_resp.status_code == 200
    assert "access_token" in login_resp.json()


def test_login_wrong_password(client):
    client.post(
        "/auth/register",
        json={"email": "bob@example.com", "password": "correct-pw", "full_name": "Bob"},
    )
    resp = client.post("/auth/login", json={"email": "bob@example.com", "password": "wrong-pw"})
    assert resp.status_code == 401
