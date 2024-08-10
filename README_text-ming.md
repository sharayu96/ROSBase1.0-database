# PDF text-mining

This script extracts text from PDF files, searches for specified keywords, and writes the results to a CSV file. It also skips over reference sections in the PDF files.

## Requirements
- Python 3.x
- `fitz` (PyMuPDF) Processing PDF documents
- `tqdm` Displays bars
- `re` Regular expressions for pattern matching
- `glob` Finding files in the directory
- `csv` andling comma-separated value files

## Installation
1. Install required libraries using pip:
    
    ``` pip3 install PyMuPDF tqdm glob csv fitz ```

## Usage
1. Place the PDF files you want to process in the same directory as the script.
2. Run the script by executing:
    
    ``` python3 script_name.py ```
    
3. The extracted text containing specified keywords will be saved in a CSV file named `file.csv`.

## Configuration
- `search_string`: Modify this variable to specify the keywords you want to search for in the PDF files.
- `references`: Modify this variable if you want to customize the string that indicates the start of the references section in the PDF files.

## Notes
- The script uses regular expressions for text search, it uses regex patterns in `search_string` for more complex searches.
- If a references section is encountered in a PDF file, the script skips to the next file without processing further.
