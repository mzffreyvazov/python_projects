import csv
import asyncio
import aiohttp
from bs4 import BeautifulSoup
from aiohttp import ClientSession
from requests.exceptions import RequestException
from urllib3.exceptions import MaxRetryError

input_file = 'words.csv'  # Replace with the path to your input CSV file
output_file = 'words_with_descriptions.csv'  # Replace with the desired output CSV file name

# Maximum number of retries for failed requests
max_retries = 3

# Number of concurrent requests to be sent
concurrent_requests = 100

# Define an asynchronous function to process each word
async def process_word(session, writer, word):
    retries = 0
    while retries < max_retries:
        try:
            # Construct the URL for the word in Merriam-Webster
            url = f'https://www.merriam-webster.com/dictionary/{word}'

            async with session.get(url) as response:
                # Check if the request was successful
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')

                    # Extract the description from the webpage
                    description = ''
                    entry = soup.find('span', {'class': 'dtText'})
                    if entry:
                        description = entry.get_text(strip=True)

                    # Write the word and its description to the output CSV file
                    writer.writerow([word, description])

                    print(f'Processed word: {word}')
                    break
                else:
                    retries += 1
                    continue

        except (RequestException, MaxRetryError) as e:
            print(f'Error occurred while processing word: {word}')
            print(f'Error: {e}')
            retries += 1
            continue

        # Delay before retrying
        await asyncio.sleep(delay * 2**retries)

    if retries >= max_retries:
        print(f'Failed to process word: {word}')



async def main():
    # Read the CSV file containing the list of words
    with open(input_file, 'r', newline='', encoding='utf-8') as input_csv, \
            open(output_file, 'w', newline='', encoding='utf-8') as output_csv:

        reader = csv.reader(input_csv)
        writer = csv.writer(output_csv, delimiter=';')

        # Write the header row
        writer.writerow(['Word', 'Description'])

        # Create an asynchronous session
        async with ClientSession() as session:
            # Create a list to store the pending tasks
            tasks = []

            # Iterate over each word in the input CSV file
            for row in reader:
                word = row[0]
                task = asyncio.ensure_future(process_word(session, writer, word))
                tasks.append(task)

                # Limit the number of concurrent requests
                if len(tasks) >= concurrent_requests:
                    await asyncio.gather(*tasks)
                    tasks.clear()

            # Wait for any remaining tasks to complete
            if tasks:
                await asyncio.gather(*tasks)

    print('Descriptions added to the CSV file.')


# Run the main async function
asyncio.run(main())
