# Simple TF-IDF Search Engine

A minimal search engine using TF-IDF scoring.

## Files

- `search_engine.py` - Main implementation
- `test_search_engine.py` - Tests
- `requirements.txt` - Dependencies

## Usage

```python
from search_engine import build_index, search

docs = [
    (1, "open ai builds powerful search engines"),
    (2, "ai search is transforming information retrieval"),
]

index = build_index(docs)
results = search("ai search", index, top_k=5)
print(results)  # [{'id': 1, 'score': 1.0}, {'id': 2, 'score': 0.85}]
```

## Run Demo

```bash
python search_engine.py
```

## Run Tests

```bash
pytest test_search_engine.py -v
```
