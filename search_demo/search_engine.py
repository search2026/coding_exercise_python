"""
Simple TF-IDF Search Engine

A minimal implementation of a search engine using TF-IDF scoring.
"""

import math
import re
from collections import defaultdict
from typing import Dict, List, DefaultDict, Tuple


class Index:
    """Data model for the inverted index."""
    index: Dict[str, Dict[int, int]]
    doc_lengths: Dict[int, int]
    total_docs: int

    def __init__(self, index: Dict[str, Dict[int, int]], doc_lengths: Dict[int, int], total_docs: int):
        self.index = index
        self.doc_lengths = doc_lengths
        self.total_docs = total_docs


class SearchResult:
    """Data model for search results."""
    doc_id: int
    score: float

    def __init__(self, doc_id: int, score: float):
        self.doc_id = doc_id
        self.score = score


def tokenize(text: str) -> List[str]:
    """Convert text to lowercase tokens, removing punctuation."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()


def build_index(documents: List[Tuple[int, str]]) -> Index:
    """
    Build an inverted index from documents.

    Returns Index object.
    """
    index: DefaultDict[str, DefaultDict[int, int]] = defaultdict(lambda: defaultdict(int))
    doc_lengths: Dict[int, int] = {}

    for doc_id, text in documents:
        tokens = tokenize(text)
        doc_lengths[doc_id] = len(tokens)
        for token in tokens:
            index[token][doc_id] += 1

    return Index(
        index=dict(index),
        doc_lengths=doc_lengths,
        total_docs=len(documents)
    )


def calculate_tfidf(term_freq: int, doc_length: int, doc_freq: int, total_docs: int) -> float:
    """Calculate TF-IDF score for a term in a document."""
    if doc_length == 0 or doc_freq == 0:
        return 0.0
    tf = term_freq / doc_length
    idf = math.log((total_docs + 1) / (doc_freq + 1)) + 1
    return tf * idf


def search(query: str, index_data: Index, top_k: int = 10) -> List[SearchResult]:
    """
    Search for documents matching the query.

    Returns list of SearchResult objects, sorted by score descending.
    """
    query_terms: List[str] = tokenize(query)
    if not query_terms:
        return []

    index = index_data.index
    doc_lengths = index_data.doc_lengths
    total_docs = index_data.total_docs

    # Find candidate documents (docs containing at least one query term)
    scores: DefaultDict[int, float] = defaultdict(float)

    for term in query_terms:
        if term not in index:
            continue
        doc_freq = len(index[term])
        for doc_id, term_freq in index[term].items():
            tfidf = calculate_tfidf(term_freq, doc_lengths[doc_id], doc_freq, total_docs)
            scores[doc_id] += tfidf

    if not scores:
        return []

    # Sort by score descending and normalize
    sorted_results: List[Tuple[int, float]] = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    max_score: float = sorted_results[0][1] if sorted_results else 1.0

    return [SearchResult(doc_id=doc_id, score=round(score / max_score, 2)) for doc_id, score in sorted_results]


def main() -> None:
    """Demo the search engine with sample documents."""
    documents: List[Tuple[int, str]] = [
        (1, "open ai builds powerful search engines"),
        (2, "ai search is transforming information retrieval"),
        (3, "open source search tools are popular"),
        (4, "retrieval augmented generation uses search")
    ]

    print("=" * 50)
    print("TF-IDF Search Engine Demo")
    print("=" * 50)

    print("\nDocuments:")
    for doc_id, text in documents:
        print(f"  {doc_id}: {text}")

    # Build index
    index_data: Index = build_index(documents)

    # Test queries
    queries: List[str] = ["open ai search", "search", "retrieval"]

    for query in queries:
        print(f"\nQuery: '{query}'")
        results: List[SearchResult] = search(query, index_data, top_k=5)
        for r in results:
            print(f"  Doc {r.doc_id}: {r.score}")


if __name__ == "__main__":
    main()
