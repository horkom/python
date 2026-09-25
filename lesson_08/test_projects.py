import pytest

from yougile_api import YougileApi


FAKE_ID = "00000000-0000-0000-0000-000000000000"


@pytest.fixture
def api():
    return YougileApi()


@pytest.fixture
def created_project(api):
    resp = api.create_project("Autotest Project")
    assert resp.status_code == 201, resp.text
    return resp.json()["id"]


# ---------- POST /projects ----------

def test_create_project_positive(api):
    title = "Positive Project"
    resp = api.create_project(title)

    assert resp.status_code == 201, resp.text
    body = resp.json()
    assert "id" in body


def test_create_project_negative_no_title(api):
    resp = api.create_project("")

    assert 400 <= resp.status_code < 500


# ---------- GET /projects/{id} ----------

def test_get_project_positive(api, created_project):
    resp = api.get_project(created_project)

    assert resp.status_code == 200
    assert resp.json()["id"] == created_project


def test_get_project_negative_not_found(api):
    resp = api.get_project(FAKE_ID)

    assert 400 <= resp.status_code < 500


# ---------- PUT /projects/{id} ----------

def test_update_project_positive(api, created_project):
    new_title = "Updated Project"
    resp = api.update_project(created_project, new_title)

    assert resp.status_code == 200, resp.text


def test_update_project_negative_not_found(api):
    resp = api.update_project(FAKE_ID, "New Title")

    assert 400 <= resp.status_code < 500
