from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

#test home api
def test_home():
    response= client.get("/")

#status code chk
    assert response.status_code ==200
#response data chk
    assert response.json() == {"message":"hellow world"}


#testing add api
def test_add():
    response= client.get("/add?a=5&b=3")
#status code chk
    assert response.status_code ==200
#response data chk
    assert response.json() == {"result":8}