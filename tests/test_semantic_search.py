
from src.retrieval.semantic_search import search_semantic


def test_empty_query_returns_empty_list():
    results = search_semantic("")

    assert results == []

def test_whitespace_query_returns_empty_list():
    results = search_semantic("   ")

    assert results == []

def test_top_k_limits_results():
    results = search_semantic(
        "How can I run code without managing servers?",
        top_k=3
    )

    assert len(results) == 3

def test_results_are_ranked_by_score():
    results = search_semantic(
        "How can I run code without managing servers?"
    )

    scores = [result["score"] for result in results]

    assert scores == sorted(scores, reverse=True)
