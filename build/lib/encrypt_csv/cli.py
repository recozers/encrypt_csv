import csv
import argparse

def encrypt_string(s):
    ''' Replaces each letter with the next letter in the alphabet (wrapping around for z)
    input: string 
    output: string'''

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
    '''Encrypts the entire CSV file into a new file
    input: CSV file
    output: CSV file (implicit nothing returned)'''

    rows = []
    # Store data in list
    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            # Encrypt each field in the row
            for field in fieldnames:
                row[field] = encrypt_string(row[field])
            rows.append(row)

    # Write to new file
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
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