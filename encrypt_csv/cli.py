import csv
import argparse

def encrypt_string(s):
    ''' Replaces each letter with the next letter in the alphabet (wrapping around for z)
    input: string (or will return without editing)
    output: string'''

    if type(s) is not str:
        return s

    encrypted = ''
    for char in s:
        if char.isalpha():
            if char.lower() == 'z':
                new_char = 'a'
            else:
                new_char = chr(ord(char) + 1)
            if char.isupper():
                encrypted += new_char.upper()
            else:
                encrypted += new_char.lower()
        else:
            encrypted += char
    return encrypted

def encrypt_csv(input_file, output_file):
    '''Encrypts the entire CSV file into a new file.
    input: file path or file-like object for input
    output: file path or file-like object for output'''

    rows = []

    # If input_file is a string (file path), open it; otherwise, use it as-is
    if isinstance(input_file, str):
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                for field in fieldnames:
                    row[field] = encrypt_string(row[field])
                rows.append(row)
    else:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        for row in reader:
            for field in fieldnames:
                row[field] = encrypt_string(row[field])
            rows.append(row)

    # If output_file is a string (file path), open it; otherwise, use it as-is
    if isinstance(output_file, str):
        with open(output_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
    else:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f'Encrypted data saved to {output_file}')

def main():
    parser = argparse.ArgumentParser(description='Encrypt the entire CSV file by shifting letters in all columns.')
    parser.add_argument('input_file', help='The input CSV file')
    parser.add_argument('output_file', help='The output CSV file')
        
    args = parser.parse_args()
        
    encrypt_csv(args.input_file, args.output_file)

if __name__ == '__main__':
    main()