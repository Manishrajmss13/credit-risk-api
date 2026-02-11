from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint_valid():
    payload = {
        "laufkont": 2, "laufzeit": 12, "moral": 1, "verw": 0, "hoehe": 5000,
        "sparkont": 2, "beszeit": 1, "rate": 2, "famges": 2, "buerge": 1,
        "wohnzeit": 2, "verm": 2, "alter": 30, "weitkred": 2, "wohn": 1,
        "bishkred": 2, "beruf": 3, "pers": 1, "telef": 1, "gastarb": 1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "probability" in response.json()
    assert "risk_tier" in response.json()


def test_predict_endpoint_invalid():
    payload = {
        "laufkont": 5,   # invalid: max is 4
        "laufzeit": 12, "moral": 1, "verw": 0, "hoehe": 5000,
        "sparkont": 2, "beszeit": 1, "rate": 2, "famges": 2, "buerge": 1,
        "wohnzeit": 2, "verm": 2, "alter": 30, "weitkred": 2, "wohn": 1,
        "bishkred": 2, "beruf": 3, "pers": 1, "telef": 1, "gastarb": 1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "less_than_equal"


def test_predict_endpoint_boundary():
    # Using min values
    min_payload = {
        "laufkont": 1, "laufzeit": 4, "moral": 0, "verw": 0, "hoehe": 250,
        "sparkont": 1, "beszeit": 1, "rate": 1, "famges": 1, "buerge": 1,
        "wohnzeit": 1, "verm": 1, "alter": 19, "weitkred": 1, "wohn": 1,
        "bishkred": 1, "beruf": 1, "pers": 1, "telef": 1, "gastarb": 1
    }
    response = client.post("/predict", json=min_payload)
    assert response.status_code == 200
    assert "probability" in response.json()
    assert "risk_tier" in response.json()

    # Using max values
    max_payload = {
        "laufkont": 4, "laufzeit": 72, "moral": 4, "verw": 10, "hoehe": 18424,
        "sparkont": 5, "beszeit": 5, "rate": 4, "famges": 4, "buerge": 3,
        "wohnzeit": 4, "verm": 4, "alter": 75, "weitkred": 3, "wohn": 3,
        "bishkred": 4, "beruf": 4, "pers": 2, "telef": 2, "gastarb": 2
    }
    response = client.post("/predict", json=max_payload)
    assert response.status_code == 200
    assert "probability" in response.json()
    assert "risk_tier" in response.json()


def test_predict_endpoint_missing_field():
    payload = {
        # "laufkont" missing
        "laufzeit": 12, "moral": 1, "verw": 0, "hoehe": 5000,
        "sparkont": 2, "beszeit": 1, "rate": 2, "famges": 2, "buerge": 1,
        "wohnzeit": 2, "verm": 2, "alter": 30, "weitkred": 2, "wohn": 1,
        "bishkred": 2, "beruf": 3, "pers": 1, "telef": 1, "gastarb": 1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "missing"
