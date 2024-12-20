import app

def test_prediction_route():
    client = app.app.test_client()
    response = client.post('/predict', json={"sample": "test"})
    assert response.status_code == 200
    assert response.get_json()["output"] == "predicted-value"
