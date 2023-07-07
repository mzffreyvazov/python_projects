import csv
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from urllib3.exceptions import MaxRetryError
import time

input_file = 'translation_full.csv'  # Replace with the path to your input CSV file
output_file = 'output.csv'  # Replace with the desired output CSV file name

columns_to_keep = [2]  # Index of the column(s) to keep (zero-based index)

with open(input_file, 'r', newline='', encoding='utf-8') as input_csv, \
     open(output_file, 'w', newline='', encoding='utf-8') as output_csv:

    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)

    for row in reader:
        # Extract the desired column(s) and write to the output CSV file
        selected_columns = [row[i] for i in columns_to_keep]
        writer.writerow(selected_columns)

print('Columns extracted and saved to output.csv.')


input_file = 'output.csv'  # Replace with the path to your input CSV file
output_file = 'words_with_descriptions2.csv'  # Replace with the desired output CSV file name

# Read the CSV file containing the list of words
max_retries = 3

# Delay between requests (in seconds)
delay = 1

# Read the CSV file containing the list of words
with open(input_file, 'r', newline='', encoding='utf-8') as input_csv, \
        open(output_file, 'w', newline='', encoding='utf-8') as output_csv:

    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv, delimiter=';')

    # Write the header row
    writer.writerow(['Word', 'Description'])

    # Iterate over each word in the input CSV file
    for row in reader:
        word = row[0]

        retries = 0
        while retries < max_retries:
            try:
                # Construct the URL for the word in Merriam-Webster
                url = f'https://www.merriam-webster.com/dictionary/{word}'

                # Send a GET request to the URL
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract the description from the webpage
                description = ''
                entry = soup.find('span', {'class': 'dtText'})
                if entry:
                    description = entry.get_text(strip=True)

                # Write the word and its description to the output CSV file
                writer.writerow([word, description])

                print(f'Processed word: {word}')
                break

            except (RequestException, MaxRetryError) as e:
                print(f'Error occurred while processing word: {word}')
                print(f'Error: {e}')
                retries += 1
                time.sleep(delay * 2**retries)

        if retries >= max_retries:
            print(f'Failed to process word: {word}')

print('Descriptions added to the CSV file.')