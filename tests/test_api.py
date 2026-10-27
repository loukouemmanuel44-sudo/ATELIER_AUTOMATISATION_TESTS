import requests

def test_post_1():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5
    )

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "title" in data
    assert "body" in data
