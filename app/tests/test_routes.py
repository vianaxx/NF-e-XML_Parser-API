import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_xml_success():
    with open("tests/example_nfe.xml", "rb") as f:
        response = client.post("/api/nfe/upload", files={"file": ("example_nfe.xml", f, "application/xml")})
    assert response.status_code == 200
    assert response.json() == {"message": "Nota fiscal processada com sucesso"}

def test_upload_invalid_extension():
    response = client.post("/api/nfe/upload", files={"file": ("example.txt", b"dummy content", "text/plain")})
    assert response.status_code == 400
