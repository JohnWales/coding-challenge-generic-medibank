import os
import re
from collections import Counter


# Retrieve all text files from the current directory 
def get_text_files(directory):
    txt_files = []
    # 3 values expected from os.walk therefore even though we do not use subdirs, it is still needed
    for root, subdirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                # Constructs full file path and adds it to the list 
                txt_files.append(os.path.join(root, file))
    return txt_files



# Read files and count word occurrences
def count_words(file_paths):
    # Initialising our counter
    counter = Counter()
    for file in file_paths:
        with open(file, 'r', encoding='utf-8') as f:
            # Using regex to find whole words and ignoring numbers etc
            # I then convert it all to lowercase for case insensitivity purposes
            words = re.findall(r'\b[a-zA-Z]+\b', f.read().lower())  
            counter.update(words)
    return counter



def sort_by_count(word_counts):
   # Converting counter dictionary into word count tuples list and reversing to ensure descending order requirement is met
    return sorted(word_counts.items(), key=get_count, reverse=True)



def get_count(item):
    # Helper function to get count from tuple (word, count). [1] is count due to indexing rules
    return item[1]



def main():
    # Scripts filepath on local machine 
    directory = os.path.dirname(os.path.abspath(__file__))  
    
    # Get list of all file paths from all subdirectories 
    files = get_text_files(directory)
    
    # Counting word occurances in files stored in a dictionary format but does not exclude occurances < 2
    word_counts = count_words(files)
    
    # Converting words to tuple format so I can output in the required way
    sorted_words = sort_by_count(word_counts)
    
    # Ensring that I meet the requiremnet of only outputting words that occur more than twice and does not output for 2 or less
    for word, count in sorted_words:
        if count > 2:
            print(f"{word} {count}")



if __name__ == "__main__":
    main()
