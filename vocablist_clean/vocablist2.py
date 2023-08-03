import sys
import csv
import re
import math

def clean_text(text):
    """Clean text and convert to CSV format"""

    # Cleaning logic...
    text = re.sub(r'\d+\.', '', text)
    
    # Replace dashes with commas
    text = text.replace('-', ',')    
    # Split text into lines
    lines = text.split('\n')
    
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line:
            if '-' in line:
                en, az = line.split('-')
                en = en.strip()
                az = az.strip()
            else:
                en = line
                az = ""
                
            cleaned_line = f'{en},{az}'
            cleaned_lines.append(cleaned_line)

    # Join lines    
    cleaned_text = '\n'.join(cleaned_lines)
    return cleaned_text


def write_csv(cleaned_text):
    """Write cleaned text to CSV file"""

    with open("cleaned_file.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)  
        writer.writerow(['English', 'Azerbaijani'])     
        for line in cleaned_text.split('\n'):
            en, az = line.split(',', maxsplit=1)
            writer.writerow([en, az])


def chunk_csv(csv_file, chunk_size):
    """Split CSV into chunks"""

    chunks = []

    with open(csv_file) as f:
        reader = csv.reader(f)
        data = list(reader)

    num_chunks = math.ceil(len(data) / chunk_size)

    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size
        chunk = data[start_idx:end_idx]
        chunks.append(chunk)

    
    return chunks


def write_chunks(chunks):
    """Write chunks to files"""

    for i, chunk in enumerate(chunks):
       with open(f'chunk_{i+1}.csv', 'w') as f:
           writer = csv.writer(f)
           writer.writerows(chunk)
           
           
def main():
    input_file = sys.argv[1]

    with open(input_file,  encoding='utf-8') as f:
        text = f.read()

    cleaned_text = clean_text(text)
    write_csv(cleaned_text)

    chunks = chunk_csv('cleaned_file.csv', 20) 
    write_chunks(chunks)


if __name__ == '__main__':
    main()