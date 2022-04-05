def test_valid_iban(client):
    response = client.post("/validate-iban", json={
        "iban": "RO13RZBR0000060007134800"
    })

    assert response.status_code == 200
    assert response.json['valid'] == "True"

def test_invalid_iban(client):
    response = client.post("/validate-iban", json={
        "iban": "SE3245"
    })
  
    assert response.status_code == 200
    assert response.json['valid'] == "False"

def test_error_without_iban(client):
    response = client.post("/validate-iban")
  
    assert response.status_code == 400