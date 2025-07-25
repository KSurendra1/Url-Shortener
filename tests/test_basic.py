import pytest
import sys
import os
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_shorten_valid_url(client):
    res = client.post("/api/shorten", json={"url": "https://example.com"})
    assert res.status_code == 201
    assert "short_code" in res.get_json()

def test_shorten_invalid_url(client):
    res = client.post("/api/shorten", json={"url": "bad-url"})
    assert res.status_code == 400

def test_redirect_and_stats(client):
    post = client.post("/api/shorten", json={"url": "https://example.com"})
    code = post.get_json()["short_code"]

    redirect = client.get(f"/{code}")
    assert redirect.status_code == 302

    stats = client.get(f"/api/stats/{code}").get_json()
    assert stats["url"] == "https://example.com"
    assert stats["clicks"] >= 1
    assert "created_at" in stats

def test_redirect_404(client):
    res = client.get("/fake123")
    assert res.status_code == 404

def test_stats_404(client):
    res = client.get("/api/stats/fake123")
    assert res.status_code == 404
