
from unittest.mock import patch

from src.retrieval.reranker import rerank


def test_empty_query_returns_empty_list():
    assert rerank("", []) == []


def test_empty_candidates_returns_empty_list():
    assert rerank("How does Lambda work?", []) == []


def test_results_include_rerank_score():
    candidates = [
        {
            "doc_id": "D1",
            "score": 0.5,
            "text": "AWS Lambda runs code."
        }
    ]

    with patch(
        "src.retrieval.reranker.reranker_model.predict",
        return_value=[2.5]
    ):
        results = rerank("How does Lambda work?", candidates)

    assert results[0]["rerank_score"] == 2.5
    assert results[0]["doc_id"] == "D1"
    assert results[0]["score"] == 0.5


def test_results_are_sorted_by_rerank_score():
    candidates = [
        {"doc_id": "D1", "score": 0.5, "text": "Document one"},
        {"doc_id": "D2", "score": 0.4, "text": "Document two"},
        {"doc_id": "D3", "score": 0.3, "text": "Document three"},
    ]

    with patch(
        "src.retrieval.reranker.reranker_model.predict",
        return_value=[1.0, 3.0, 2.0]
    ):
        results = rerank("Test query", candidates)

    assert [result["doc_id"] for result in results] == [
        "D2", "D3", "D1"
    ]
