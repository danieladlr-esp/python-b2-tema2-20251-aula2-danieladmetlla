import pytest
from ej2d7 import prepare_data_for_clustering, perform_kmeans_clustering, visualize_clusters


@pytest.fixture
def german_credit_data_path():
    return './data/german_credit_data.csv'


def test_prepare_data_for_clustering(german_credit_data_path):
    data_scaled = prepare_data_for_clustering(german_credit_data_path)
    assert data_scaled.mean(axis=0).all() == pytest.approx(0, abs=1e-6), "The data should be centered around 0"
    assert data_scaled.std(axis=0).all() == pytest.approx(1, abs=1e-6), "The data should have a standard deviation of 1"


def test_perform_kmeans_clustering(german_credit_data_path):
    data_scaled = prepare_data_for_clustering(german_credit_data_path)
    n_clusters = 5
    labels = perform_kmeans_clustering(data_scaled, n_clusters)
    assert len(labels) > 0, "The labels should not be empty"
    assert len(set(labels)) == n_clusters, "The number of unique labels should match the number of clusters"


def test_visualize_clusters(german_credit_data_path):
    data_scaled = prepare_data_for_clustering(german_credit_data_path)
    n_clusters = 5
    labels = perform_kmeans_clustering(data_scaled, n_clusters)
    data_reduced, fig, ax = visualize_clusters(data_scaled, labels)
    assert data_reduced.shape[1] == 2, "The data should be reduced to 2 dimensions"
