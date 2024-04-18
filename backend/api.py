from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
import pandas as pd

from config import FRONTEND_PORT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_PORT,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def fetch_or_read_data():
    # Path to the CSV file in the data directory
    csv_file_path = "data/Mall_Customers.csv"

    # Read the CSV file directly
    df = pd.read_csv(csv_file_path)

    # Convert the 'Gender' column to 0 for Female and 1 for Male
    df["Gender"] = df["Gender"].map({"Female": 0, "Male": 1})

    # Prepare the data for clustering
    X = df.drop(columns=["CustomerID", "Gender"]).values

    return X


@app.get("/evaluate_clustering_kmeans/")
async def evaluate_clustering_kmeans():
    try:
        X = fetch_or_read_data()

        # KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans_labels = kmeans.fit_predict(X)

        # Metric
        silhouette = silhouette_score(X, kmeans_labels)

        return {
            "silhouette_score": silhouette,
        }
    except Exception as e:
        return {"error": str(e)}


@app.get("/evaluate_clustering_agglomerative/")
async def evaluate_clustering_agglomerative():
    try:
        X = fetch_or_read_data()

        # Hierarchical clustering
        agglomerative = AgglomerativeClustering(n_clusters=3)
        agglomerative_labels = agglomerative.fit_predict(X)

        # Metric
        silhouette = silhouette_score(X, agglomerative_labels)

        return {
            "silhouette_score": silhouette,
        }

    except Exception as e:
        return {"error": str(e)}


@app.get("/evaluate_clustering_dbscan/")
async def evaluate_clustering_dbscan():
    try:
        X = fetch_or_read_data()

        # DBSCAN clustering
        dbscan = DBSCAN(eps=3, min_samples=2)
        dbscan_labels = dbscan.fit_predict(X)

        # Metric
        silhouette = silhouette_score(X, dbscan_labels)

        return {
            "silhouette_score": silhouette,
        }

    except Exception as e:
        return {"error": str(e)}
