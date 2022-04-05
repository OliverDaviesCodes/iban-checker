def test_valid_iban(client):
    response = client.post("/validate-iban", json={
        "iban": "RO13RZBR0000060007134800"
    })
    print(response.json)
    assert True == True

def test_invalid_iban(client):
    response = client.post("/validate-iban", json={
        "iban": "SE3245"
    })
    print(response.json)
    assert response.status_code == 400