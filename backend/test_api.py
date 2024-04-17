import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

@pytest.mark.parametrize("endpoint", [
    "/evaluate_clustering_kmeans/",
    "/evaluate_clustering_agglomerative/",
    "/evaluate_clustering_dbscan/"
])
def test_api_endpoints(endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200
    assert "silhouette_score" in response.json()