from src_test.instance import client

def test_get_token():
    # The expectation is to receive token
    response = client.post('/token')
    assert response.status_code == 200
    assert 'access_token' in response.json()
    assert 'token_type' in response.json()
    assert 'expires_in' in response.json()
    assert 'scope' in response.json()
