from pathlib import Path
import re
from collections import Counter
import textdistance
import pandas as pd
import Levenshtein  # Import Levenshtein library for string distance calculation

# Read text file and preprocess data
file_path = Path('words.txt')
file_content = file_path.read_text()

# Extract words from text content
words = re.findall(r'\w+', file_content.lower())

# Create a set of unique words (vocabulary)
V = set(words)

# Calculate word frequency using Counter
word_freq = Counter(words)

# Calculate total sum of word frequencies
total_sum = sum(word_freq.values())

# Calculate probabilities for each word
probs = {}
for word, freq in word_freq.items():
    probs[word] = freq / total_sum

print(probs)


def my_autocorrect(input_word):
    # Calculate similarity scores using Jaccard distance
    similarity_scores = [(input_word, textdistance.jaccard(input_word, word), word) for word in word_freq.keys()]
    # Create DataFrame from similarity scores
    df = pd.DataFrame(similarity_scores, columns=['Word', 'Prob', 'Similarity'])
    return df

# Test input
test_input = 'hel'
input_word = test_input.lower()  # Convert input word to lowercase

# Check if input word is in the vocabulary
if input_word not in V:
    result = my_autocorrect(input_word)  # Call my_autocorrect function
    suggestion_words = result.sort_values(by=['Prob'], ascending=False)  # Sort suggestions by probability
    print(suggestion_words.head())  # Print top suggestions
else:
    print('Your word seems to be correct')

# Function to suggest corrections based on Levenshtein distance
def correction_suggestion(word):
    word = word.lower()
    if word in V:
        return word  # Return the word itself if it's in the vocabulary
    else:
        # Find suggestions with a Levenshtein ratio > 0.8
        suggestions = [w for w in V if Levenshtein.ratio(word, w) > 0.8]
        if suggestions:
            return suggestions[0:2]  # Return top 2 suggestions
        else:
            return None  # Return None if no suggestions are found

result = correction_suggestion('anaconda')
print(result)  # Print suggested corrections
