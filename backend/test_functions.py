import numpy as np
from api import read_data, evaluate_clustering_kmeans, evaluate_clustering_agglomerative, evaluate_clustering_dbscan

def test_read_data():
    result = read_data()
    assert isinstance(result, np.ndarray)
    assert result.shape[0] > 0
    assert result.shape[1] > 0

    # Tests the evaluate_clustering_kmeans function to ensure it returns the expected output for a given input.
def test_evaluate_clustering_kmeans():
   
    # Call the function
    result = evaluate_clustering_kmeans()
    
    # Check the output
    assert isinstance(result, np.ndarray)
    assert result.shape[1] == 1

def test_evaluate_clustering_agglomerative():   
    # Call the function
    result = evaluate_clustering_agglomerative()
    
    # Check the output
    assert isinstance(result, np.ndarray)
    assert result.shape[1] == 1

def test_evaluate_clustering_dbscan():   
    # Call the function
    result = evaluate_clustering_dbscan()
    
    # Check the output
    assert isinstance(result, np.ndarray)
    assert result.shape[1] == 1