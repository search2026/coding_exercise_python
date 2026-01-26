"""Tests for the simple TF-IDF search engine."""

import pytest
from search_engine import tokenize, build_index, search


class TestTokenize:
    def test_basic(self):
        assert tokenize("Hello World") == ["hello", "world"]
    
    def test_punctuation(self):
        assert tokenize("Hello, World!") == ["hello", "world"]
    
    def test_empty(self):
        assert tokenize("") == []


class TestBuildIndex:
    def test_basic(self):
        docs = [(1, "hello world"), (2, "hello there")]
        index_data = build_index(docs)
        assert index_data['total_docs'] == 2
        assert 'hello' in index_data['index']
        assert index_data['index']['hello'][1] == 1
        assert index_data['index']['hello'][2] == 1
    
    def test_term_frequency(self):
        docs = [(1, "hello hello hello")]
        index_data = build_index(docs)
        assert index_data['index']['hello'][1] == 3
    
    def test_doc_lengths(self):
        docs = [(1, "one two three")]
        index_data = build_index(docs)
        assert index_data['doc_lengths'][1] == 3


class TestSearch:
    @pytest.fixture
    def sample_index(self):
        docs = [
            (1, "open ai builds powerful search engines"),
            (2, "ai search is transforming information retrieval"),
            (3, "open source search tools are popular"),
            (4, "retrieval augmented generation uses search")
        ]
        return build_index(docs)
    
    def test_basic_search(self, sample_index):
        results = search("search", sample_index)
        assert len(results) == 4
    
    def test_multi_term(self, sample_index):
        results = search("open ai", sample_index)
        assert len(results) > 0
        assert results[0]['score'] == 1.0  # Top result normalized to 1.0
    
    def test_empty_query(self, sample_index):
        results = search("", sample_index)
        assert results == []
    
    def test_no_match(self, sample_index):
        results = search("xyz123", sample_index)
        assert results == []
    
    def test_top_k(self, sample_index):
        results = search("search", sample_index, top_k=2)
        assert len(results) == 2
    
    def test_sorted_by_score(self, sample_index):
        results = search("open ai search", sample_index)
        scores = [r['score'] for r in results]
        assert scores == sorted(scores, reverse=True)


class TestIntegration:
    def test_example_query(self):
        docs = [
            (1, "open ai builds powerful search engines"),
            (2, "ai search is transforming information retrieval"),
            (3, "open source search tools are popular"),
            (4, "retrieval augmented generation uses search")
        ]
        index_data = build_index(docs)
        results = search("open ai search", index_data, top_k=3)
        
        assert len(results) == 3
        assert results[0]['score'] == 1.0
        assert all('id' in r and 'score' in r for r in results)
