def test_get_root_redirects_to_index(client):
    # Arrange
    url = "/"

    # Act
    response = client.get(url)

    # Assert: TestClient follows redirects, so final URL should be the static index
    assert response.status_code == 200
    assert str(response.url).endswith("/static/index.html")


def test_get_activities_returns_activities(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
