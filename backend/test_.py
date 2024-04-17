import pandas as pd
from fastapi.testclient import TestClient
from api import app, read_data


def test_execution_test():
    assert 1 == 1


def test_read_data():
    csv_file_path = "data/Mall_Customers.csv"
    # Read the CSV file directly
    df = pd.read_csv(csv_file_path)

    # Convert the 'Gender' column to 0 for Female and 1 for Male
    df["Gender"] = df["Gender"].map({"Female": 0, "Male": 1})

    # Prepare the data for clustering
    X = df.drop(columns=["CustomerID", "Gender"]).values
    assert X.shape[0] > 0
    assert X.shape[1] > 0


# client = TestClient(app)

# @pytest.mark.parametrize("endpoint", [
#     "/evaluate_clustering_kmeans/",
#     "/evaluate_clustering_agglomerative/",
#     "/evaluate_clustering_dbscan/"
# ])
# def test_api_endpoints(endpoint):
#     response = client.get(endpoint)
#     assert response.status_code == 200
#     assert "silhouette_score" in response.json()
