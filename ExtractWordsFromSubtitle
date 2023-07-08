import glob
import re

# Function to extract phrases, idioms, and words from a line
def extract_words(line):
    words = re.findall(r'\b\w+\b', line)
    return words

# Directory containing the subtitle files
directory = '/tmp/srt/'

# Get a list of all subtitle files in the directory
subtitle_files = glob.glob(directory + '*.srt')

# Set to store extracted words
word_set = set()

# Iterate over each subtitle file
for file in subtitle_files:
    with open(file, 'r') as subtitle_file:
        lines = subtitle_file.readlines()

        # Iterate over each line in the subtitle file
        for line in lines:
            # Check if the line contains words
            if any(char.isalpha() for char in line):
                words = extract_words(line)
                word_set.update(words)

# Sort the words in alphabetical order
sorted_words = sorted(word_set)

# Remove punctuation from the words
cleaned_words = [re.sub(r'[^\w\s]', '', word) for word in sorted_words]

# Remove duplicate words
unique_words = list(set(cleaned_words))

# Sort the unique words again in alphabetical order
sorted_unique_words = sorted(unique_words)

# Save the words to a text file
output_file = '/tmp/output.txt'
with open(output_file, 'w') as file:
    file.write('\n'.join(sorted_unique_words))

print(f"Output saved to: {output_file}")
