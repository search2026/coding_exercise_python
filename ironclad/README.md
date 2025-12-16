# Ironclad Technical Project – List Transformation Prototype

This project is a small Python prototype that applies a sequence of edit operations
to an input list of JSON objects and produces a transformed output.

It is designed to be:
- Simple and readable
- Easy to test with `pytest`
- Robust to different working directories (CLI / VS Code / CI)

---

## 📁 Project Structure

```
ironclad/
├── data/
│   ├── input.json              # Original input data (list of objects)
│   ├── edits.json              # Edit operations to apply
│   └── expected_output.json    # Expected output for tests
│
├── src/
│   ├── main.py                 # Program entry point
│   ├── transform.py            # Core transformation logic
│   ├── json_utils.py           # JSON load/save helpers
│   └── __init__.py
│
├── tests/
│   ├── test_transform.py       # pytest test cases
│   └── __init__.py
│
├── pyproject.toml              # pytest configuration
├── .vscode/
│   └── settings.json           # VS Code pytest + import settings
└── README.md
```

---

## ⚙️ Environment Setup

### 1. Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate  # Windows
```

### 2. Install dependencies

```bash
pip install pytest black
```

---

## ▶️ Running Tests

From the **project root** (`ironclad/`):

### Run all tests
```bash
pytest
```

### Run tests with verbose output
```bash
pytest -v
```

### Run a specific test file
```bash
pytest tests/test_transform.py
```

---

## 🎨 Code Formatting

This project uses **Black** for consistent formatting.

Format the entire project:
```bash
black ironclad/
```

Check formatting without modifying files:
```bash
black --check ironclad/
```

---

## 🚀 Running the Program

From the project root:

```bash
python src/main.py
```

The program reads:
- `data/input.json`
- `data/edits.json`

and writes:
- `data/output.json`

---

## 🧠 Notes on Design

- Edit operations are applied **sequentially**.
- The input list is **deep-copied** to avoid side effects.
- File paths are resolved using `pathlib` for robustness.
- Tests are written with `pytest` and are VS Code–friendly.

---

## 📌 Assumptions

- Input, edits, and output are JSON arrays of objects.
- Indexes in edits refer to the **current state of the list**.

---

## 📝 License

This project is intended for interview and demonstration purposes.
