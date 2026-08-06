def test_get_me(client, auth_headers):
    resp = client.get("/users/me", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["email"] == "test@example.com"


def test_get_me_requires_auth(client):
    resp = client.get("/users/me")
    assert resp.status_code == 401
