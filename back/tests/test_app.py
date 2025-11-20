from back.app import app


def test_calc_soma_route():
    client = app.test_client()

    resp = client.post("/calc", json={"a": 10, "op": "+", "b": 5})

    assert resp.status_code == 200
    data = resp.get_json()
    assert data["result"] == 15

def test_calc_sqrt_route():
    client = app.test_client()

    resp = client.post("/calc", json={"a": 9, "op": "sqrt"})

    assert resp.status_code == 200
    data = resp.get_json()
    assert data["result"] == 3


def test_calc_divisao_arredondada_route():
    client = app.test_client()

    resp = client.post("/calc", json={"a": 2, "op": "/", "b": 3})

    assert resp.status_code == 200
    data = resp.get_json()
    assert data["result"] == 0.66667
