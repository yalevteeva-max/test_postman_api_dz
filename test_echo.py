import pytest


def test_get_returns_args(base_url, session):
    params = {"foo1": "bar1", "foo2": "bar2"}
    response = session.get(f"{base_url}/get", params=params)
    data = response.json()
    assert data["args"] == params


def test_get_returns_headers(base_url, session):
    headers = {"my-sample-header": "Lorem ipsum dolor sit amet"}
    response = session.get(f"{base_url}/headers", headers=headers)
    data = response.json()
    assert data["headers"]["my-sample-header"] == "Lorem ipsum dolor sit amet"


def test_post_returns_json_body(base_url, session):
    payload = {"test": "value"}
    response = session.post(f"{base_url}/post", json=payload)
    data = response.json()
    assert data["json"] == payload


def test_post_returns_form_data(base_url, session):
    form_data = {"foo1": "bar1", "foo2": "bar2"}
    response = session.post(f"{base_url}/post", data=form_data)
    data = response.json()
    assert data["form"] == form_data


def test_put_returns_data(base_url, session):
    body = "This is expected to be sent back as part of response body."
    response = session.put(f"{base_url}/put", data=body)
    data = response.json()
    assert data["data"] == body


def test_patch_returns_data(base_url, session):
    body = "This is expected to be sent back as part of response body."
    response = session.patch(f"{base_url}/patch", data=body)
    data = response.json()
    assert data["data"] == body


def test_delete_returns_status_200(base_url, session):
    response = session.delete(f"{base_url}/delete")
    assert response.status_code == 200