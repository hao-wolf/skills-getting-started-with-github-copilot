def test_signup_and_unregister_flow(client):
    # Arrange
    activity = "Chess Club"
    email = "tester@example.com"
    signup_url = f"/activities/{activity}/signup"
    unregister_url = f"/activities/{activity}/participants"

    # Act: sign up
    resp_signup = client.post(signup_url, params={"email": email})

    # Assert: signup succeeded and message mentions the email
    assert resp_signup.status_code == 200
    assert email in resp_signup.json().get("message", "")

    # Act: unregister
    resp_unreg = client.delete(unregister_url, params={"email": email})

    # Assert: unregister succeeded and message mentions the email
    assert resp_unreg.status_code == 200
    assert email in resp_unreg.json().get("message", "")


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "No Such Activity"
    email = "x@example.com"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404


def test_unregister_nonexistent_participant_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "not-a-participant@example.com"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 404
