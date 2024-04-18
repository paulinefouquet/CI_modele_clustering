import pytest
import numpy as np
from fastapi.testclient import TestClient
from api import app, fetch_or_read_data


def test_execution_test():
    assert True


def test_read_data():
    X = fetch_or_read_data()
    assert isinstance(X, np.ndarray)
    assert X.shape[0] > 0


client = TestClient(app)


@pytest.mark.parametrize(
    "endpoint",
    [
        "/evaluate_clustering_kmeans/",
        "/evaluate_clustering_agglomerative/",
        "/evaluate_clustering_dbscan/",
    ],
)
def test_api_endpoints(endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200
    assert "silhouette_score" in response.json()
