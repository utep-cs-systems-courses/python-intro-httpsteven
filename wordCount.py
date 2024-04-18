#!/usr/bin/env python3

import sys
import re
import os

def count_words(input_file):
    """
    Reads a text file and returns a dictionary with word counts.
    """
    word_counts = {}
    with open(input_file, 'r') as file:
        text = file.read().lower()

    # Normalize the text by replacing hyphens and apostrophes with spaces
    normalized_text = text.replace("-", " ").replace("'", " ")

    # Find words using regular expressions
    words = re.findall(r'\b\w+\b', normalized_text)

    # Count each word
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def write_output(word_counts, output_file):
    """
    Writes the word counts to the output file in sorted order.
    """
    with open(output_file, 'w') as file:
        for word, count in sorted(word_counts.items()):
            file.write(f"{word} {count}\n")

def main():
    # Check for correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: script.py <input text file> <output text file>")
        sys.exit()

    input_fname = sys.argv[1]
    output_fname = sys.argv[2]

    # Check if input file exists
    if not os.path.exists(input_fname):
        print(f"Input file {input_fname} does not exist! Exiting.")
        sys.exit()

    # Check if output file exists; create if not
    if not os.path.exists(output_fname):
        print(f"Output file {output_fname} does not exist! It will be created.")

    # Process the input file and write to the output file
    word_counts = count_words(input_fname)
    write_output(word_counts, output_fname)
    print(f"Word counts written to {output_fname}.")

if __name__ == "__main__":
    main()
