from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score
import pandas as pd

import os
import requests

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
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Path to the CSV file in the data directory
    csv_file_path = "data/Mall_Customers.csv"

    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        # If the file doesn't exist, download it from the URL
        url = "https://gist.githubusercontent.com/pravalliyaram/5c05f43d2351249927b8a3f3cc3e5ecf/raw/8bd6144a87988213693754baaa13fb204933282d/Mall_Customers.csv"
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Write the content to the CSV file
            with open(csv_file_path, "wb") as f:
                f.write(response.content)
        else:
            raise Exception(f"Failed to download CSV file from {url}")

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
