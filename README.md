# Encrypt CSV

`encrypt_csv` is a Python tool for encrypting the contents of a CSV file by shifting each letter in the text fields to the next letter in the alphabet (e.g., 'A' becomes 'B', 'z' becomes 'a'). The tool is designed as a command line utility.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Interface](#command-line-interface)
- [Testing](#testing)

## Installation

### Prerequisites
- Python 3.6 or higher

### Install via pip
You can install the package locally by navigating to the project directory and running:

```bash
pip install .
```

## Usage

### Command-Line Interface
Once installed, you can use the `encrypt-csv` command to encrypt a CSV file.

```bash
encrypt-csv input.csv output.csv
```

- `input.csv`: The path to the input CSV file.
- `output.csv`: The path to save the encrypted CSV file.

## Testing

To run tests, you can use `pytest`. Ensure that `pytest` is installed:

```bash
pip install pytest
```

Run the tests with:

```bash
pytest -v
```

This will execute all the tests in the `test_encrypt_csv.py` file, ensuring that the code behaves as expected.
