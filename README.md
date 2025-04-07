# Thoughtful Shipping Package

This package contains the code used for Andrew Wiser's live coding exercise for his interview with Thoughtful AI

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/AndrewW85/AHWThoughtful>
cd thoughtful
```

2. Create a virtual environment using uv (recommended):
```bash
uv venv
```

3. Install the package in development mode with all dependencies:
```bash
uv pip install --group dev
```

## Running the Code
This repository includes two options for running the code, a simple sort_demo.py script that will output lines that contain a description, expected sort class, and either True/False indicating if calling the sort() function output the expected values. The second method uses the Python unittest module to test a whether the basic sort functionality is working as expected.

### Running the Demo Script
To run the sort_demo.py script:
```bash
uv run python sort_demo.py
```

### Running Tests

To run all tests:
```bash
uv run python -m unittest discover shipping
```

To run a specific test file:
```bash
uv run python -m unittest shipping/test_package.py
```

To run tests with verbose output:
```bash
uv run python -m unittest discover shipping -v
```

## Development

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and code formatting.

### Running Ruff

To check for linting issues:
```bash
uv run ruff check .
```

To automatically fix issues:
```bash
uv run ruff check --fix .
```

To automatically fix E501 issues:
```bash
uv run ruff format
```
