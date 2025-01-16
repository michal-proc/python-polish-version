
# PolishPython

PolishPython is an innovative Python-inspired programming language that brings a localized, Polish-centric approach to coding. Designed for educational purposes and experimentation, it allows users to write scripts in Polish syntax while maintaining the structure and logic of Python. This tool not only makes programming more accessible to Polish-speaking communities but also demonstrates how languages can be adapted to different linguistic and cultural contexts. Whether you are a beginner learning to code in your native language or an advanced programmer exploring the limits of language design, PolishPython offers a unique and engaging experience.

---

## Features

- **Localized Syntax:** Write Python-like scripts using Polish keywords.
- **Compilation:** Convert PolishPython scripts into Python for execution.
- **Execution:** Optionally run the compiled scripts directly.
- **Error Handling:** Provides detailed syntax error reporting.
- **Extensibility:** Modular design for adding more translations and features.

---

## Project Structure

```
python-polish-version/
├── examples/                # Example PolishPython scripts (.ppy files)
├── grammar/                 # ANTLR grammar and lexer files
├── output/                  # Generated Python scripts from PolishPython
├── parsers/                 # Modules for parsing and validation
├── translations/            # Definitions for Polish translations (keywords, functions, etc.)
├── translators/             # Modules for translating PolishPython into Python
├── validators/              # Additional validation utilities
├── .gitignore               # Git ignore rules
├── poetry.lock              # Poetry lock file
├── pyproject.toml           # Poetry project configuration
├── README.md                # Project documentation (this file)
└── ppy.py                   # Entry point for the PolishPython CLI tool
```

---

## Requirements

- **Python 3.10+**
- **Poetry** (for dependency management)
- **ANTLR** (for generating parsers from the grammar files)

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python-polish-version
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

---

## Usage

### Command-line Arguments

Run the PolishPython CLI tool using:
```bash
python ppy.py [options]
```

| Argument        | Description                                             | Required | Default        |
|-----------------|---------------------------------------------------------|----------|----------------|
| `--file`        | Path to the input PolishPython script.                  | Yes      | N/A            |
| `--output`      | Path to save the compiled Python script.                | No       | `./output`     |
| `--run`         | Execute the compiled script after compilation.          | No       | `False`        |

### Example

1. Compile a PolishPython script:
   ```bash
   python ppy.py --file examples/example.ppy --output output/example.py
   ```

2. Compile and execute a script:
   ```bash
   python ppy.py --file examples/example.ppy --run
   ```

---

## Examples

### Input (PolishPython)

```
z typowanie sprowadź Sekwencja jako s

funkcja znajdz_maksimum(lista: s) zwraca int:
    zmienna = 0
    dla element w lista:
        jeśli element większe_niż zmienna:
            zmienna = element
    zwróć zmienna

wypisz(znajdz_maksimum([1, 2, 3]))
```

### Output (Python)

```python
from typing import Sequence as s

def znajdz_maksimum(lista: s) -> int:
    zmienna = 0
    for element in lista:
        if element > zmienna:
            zmienna = element
    return zmienna

print(znajdz_maksimum([1, 2, 3]))
```

---

## Technologies Used

- **Python:** Core language for implementation.
- **ANTLR:** Grammar-based parser generation.
- **Poetry:** Dependency and environment management.
