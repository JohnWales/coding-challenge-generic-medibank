import os
import re
from collections import Counter
#import unicodedata



# Allowing more extensions to be allowed if necessary considering that the description does not explicity state which format is used 
# file_formats = (".txt", ".csv", ".log")
file_formats = (".txt")

# Retrieve all text files from the current directory 
def get_text_files(directory):
    txt_files = []
    # 3 values expected from os.walk therefore even though I do not use subdirs, it is still needed
    for root, subdir, files in os.walk(directory):
        for file in files:
            if file.endswith(file_formats):
                # Constructing full file path and adds it to the list 
                txt_files.append(os.path.join(root, file))
    return txt_files



def count_words(file_paths):
    # Initialising the counter
    word_counter = Counter()
    for file in file_paths:
        with open(file, 'r', encoding='utf-8') as f:
            # Using regex to find whole words and ignoring numbers etc
            # I then convert it all to lowercase for case insensitivity purposes
            words = re.findall(r'\b[a-zA-Z]+\b', f.read().lower()) 
            word_counter.update(words)  

            # Below is an example of how other languages ( NON ASCII ) can be introduced into this logic but I do not think that this is needed rght now 
            """
            text = f.read()
            # Normalize text to decompose accents (e.g., é -> e) and other diacritical marks
            normalized_text = unicodedata.normalize('NFD', text)
            # Using regex to match all word characters (letters, digits, and underscores) from any alphabet
            # \w matches [a-zA-Z0-9_]
            words = re.findall(r'\b\w+\b', normalized_text.lower())  
            word_counter.update(words)  
            """

    return word_counter



def main():
     # Scripts filepath on local machine 
    directory = os.path.dirname(os.path.abspath(__file__))  

    # Get list of all file paths from all subdirectories 
    files = get_text_files(directory)

    # Counting word occurances in files stored in a dictionary format but does not exclude occurances < 2
    word_counts = count_words(files)

    # Sort by most common words which meets the requirements of descending order
    sorted_words = word_counts.most_common()  

    # Initialising a Boolean variable incase files are empty
    found_words = False
    
    # Ensring that I meet the requiremnet of only outputting words that occur more than twice and does not output for 2 or less
    for word, count in sorted_words:
        if count > 2:
            print(f"{word}\t {count}")
            found_words = True

    if not found_words:
        print("No word with an occurance greater than 2 has been found")
            


if __name__ == "__main__":
    main()
