import pytest
from fastapi.testclient import TestClient
from api import app, read_data

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


def test_read_data():
    result = read_data()
    assert result.shape[0] > 0
    assert result.shape[1] > 0