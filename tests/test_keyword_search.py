from src.retrieval.keyword_search  import (
    tokenize,
    build_index,
    search,
    documents, 
    ranking
)

def test_tokenize():
    result = tokenize("AWS Step functions.")
    assert result == ["aws", "step", "functions"]

def test_build_index():
    index = build_index(documents)

    assert index["lambda"] == {"D1", "D4"}
    
    
def test_search():
    index = build_index(documents)

    result = search("lambda timeout", index)

    assert result == {
        "D1": 2,
        "D4": 2
    }

def test_ranking():
    result = {
        "D1": 2,
        "D4": 1,
        "D2": 3
    }

    ranked = ranking(result)

    assert list(ranked.keys()) == ["D2", "D1", "D4"]

def test_search_unknown_word():
    index = build_index(documents)

    result = search("docker", index)

    assert result == {}

def test_search_empty_query():
    index = build_index(documents)

    result = search("", index)

    assert result == {}

def test_tokenize_removes_stop_words():
    assert tokenize("How can I run code?") == ["run", "code"]


def test_tokenize_preserves_meaningful_words():
    assert tokenize("run code without servers") == [
        "run", "code", "without", "servers"
    ]


def test_search_returns_empty_for_no_matching_terms():
    index = build_index(documents)
    assert search("run code without servers", index) == {}
