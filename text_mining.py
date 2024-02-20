import re
import glob
import csv
import fitz
from tqdm import tqdm

file_list = glob.glob("*.pdf")

# define search string
search_string = "Reactive|oxygen|species|ROS"
references = "References|REFERENCES"

# open the csv file for writing
with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')

    # iterate over each pdf file
    for pdf_file in tqdm(file_list):
        try:
            # open the pdf file
            pdf_doc = fitz.open(pdf_file)

            # get the number of pages
            num_pages = pdf_doc.page_count

            # extract text and search for keywords
            for page_num in range(num_pages):
                page = pdf_doc[page_num]
                text = page.get_text("text")
                
                matches = re.finditer(search_string, text)
                for match in matches:
                    start = max(match.start() - 500, 0)
                    end = min(match.end() + 500, len(text))
                    result = text[start:end].replace("\n", " ")
                    row = [pdf_file, (page_num + 1), result]
                    writer.writerow(row)
                    
                	# search for references and skip to next file if found
                    match = re.match(references, text)
                    if match:
                        continue
                
        except:
            pass

