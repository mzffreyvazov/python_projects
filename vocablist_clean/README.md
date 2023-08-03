# CSV Splitter

This is a simple Python script to clean a txt file containing english words with their azerbaijani translation and then to split
the cleaned CSV version of the file into smaller chunks for importing them into a flashcard application (Anki). 

## Usage

The script accepts a .txt file as input, cleans it and splits it into chunks of a specified size.

To run it:

```
python csv_splitter.py `vocabulary.txt
```

This will generate output files `chunk_1.csv`, `chunk_2.csv` etc in the current directory.

The chunk size can be configured by changing the `CHUNK_SIZE` constant. 

## Functions

The main logic is divided into separate functions:

- `clean_text()` - Cleans raw text into CSV format
- `write_csv()` - Writes cleaned text to a CSV file
- `chunk_csv()` - Splits CSV file into chunks
- `write_chunks()` - Writes chunks to output files

## Requirements

- Python 3
- csv
- re
- math

## Example

Input file `vocabulary.txt`:

```
Abandon v. - tərk etmək
Abandoned - tərk edilmiş
```

Generated output files:

`chunk_1.csv`:

```
English,Azerbaijani
Abandon v.,tərk etmək
Abandoned,tərk edilmiş
``` 

`chunk_2.csv`:

```
English,Azerbaijani
Ability,imkan, qabiliyyət
Able,mümkün 
```
