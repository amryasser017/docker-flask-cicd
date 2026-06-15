def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 999  # wrong status code on purpose