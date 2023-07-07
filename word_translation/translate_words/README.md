# Word Translation with Column Extraction and Web Scraping

This Python script extracts specific or unwanted columns from a CSV file that is exported form Google Translate and performs word translation (getting their english description) using web scraping. It allows you to specify the columns to keep in the input CSV file and fetches the English word descriptions from the Merriam-Webster website (you can use other similar websites if you want). The extracted columns and word descriptions are then saved to an output CSV file.

## Features

- Extracts specific columns from a CSV file.
- Performs word translation using web scraping.
- Utilizes the Merriam-Webster website (or a similar website if you want, but you should make the according adjustmenst)for word descriptions.
- Outputs the extracted columns and word descriptions to a CSV file.

## Requirements

- Python 3.7 or higher
- requests library (`pip install requests`)
- beautifulsoup4 library (`pip install beautifulsoup4`)

## Usage

1. Prepare your input CSV file (`translation_full.csv`) containing the data to extract columns from or translate words. Ensure that the file is in the correct format.
2. Modify the `input_file` and `output_file` variables in the script to specify the input CSV file and desired output CSV file names.
3. If needed, adjust the `columns_to_keep` variable to specify the index of the column(s) to keep in the input CSV file (zero-based index).
4. If desired, modify the URL construction and web scraping code to work with a different website.
5. Open a terminal or command prompt and navigate to the directory containing the script.
6. Run the script with the following command:

   ```bash
   python word_translation.py
   
## Note
1. Be mindful of the website's terms of service and usage policies when web scraping. Ensure that you have proper permissions to access and scrape the website's content.
2. Adjust the max_retries and delay variables in the script to control the number of retries and delay time between requests.
3. Customize the script according to your specific requirements, such as modifying column extraction or web scraping logic or the website itself.
