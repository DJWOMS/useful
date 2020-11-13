from fastapi.testclient import TestClient

from ....main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/api/v1/board/category/")
    assert response.status_code == 200
    # assert response.json() == {
    #     "id": "foo",
    #     "title": "Foo",
    #     "description": "There goes my hero",
    # }
