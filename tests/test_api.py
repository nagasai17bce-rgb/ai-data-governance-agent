from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_sensitive_field_requires_approval():
    data=client.post("/v1/run",json={"value":"name,email,order_id"}).json()
    assert data["approval_required"] is True
    assert data["findings"][0]["field"]=="email"
