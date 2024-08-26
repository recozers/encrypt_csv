import pytest
import os
import csv
from io import StringIO
from .cli import encrypt_string, encrypt_csv

def test_encrypt_string():
    # Test basic string encryption
    assert encrypt_string('abc') == 'bcd'
    assert encrypt_string('xyz') == 'yza'
    assert encrypt_string('ABC') == 'BCD'
    assert encrypt_string('XYZ') == 'YZA'
    assert encrypt_string('Hello, World!') == 'Ifmmp, Xpsme!'

def test_encrypt_csv_in_memory():
    # Prepare in-memory CSV data
    input_csv = StringIO("Name,Number\nAlice,123\nBob,456\n")
    output_csv = StringIO()

    # Expected encrypted output
    expected_csv = "Name,Number\nBmjdf,123\nCpc,456\n"

    # Perform the encryption
    encrypt_csv(input_csv, output_csv)

    # Move to the start of the StringIO object to read its content
    output_csv.seek(0)
    
    # Normalize newlines before comparison
    actual_output = output_csv.read().replace('\r\n', '\n').replace('\r', '\n')
    expected_output = expected_csv.replace('\r\n', '\n').replace('\r', '\n')
    
    assert actual_output == expected_output