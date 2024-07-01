# import necessary libraries
from pathlib import Path
import re
from collections import Counter
import textdistance
import pandas as pd
import Levenshtein  # Import Levenshtein library for string distance calculation

# Read text file and preprocess data
# You can also have your own set of words
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
    input_word = input_word.lower()
    
    if input_word in V:
        return 'Your word seems to be correct'
    else:
        jaccard = textdistance.Jaccard(qval=2)
        result_set = []
        for word in word_freq.keys():
            similarity_score = jaccard(input_word, word)
            prob = probs[word]

            result_set.append((word, prob, similarity_score))

        
        df = pd.DataFrame(result_set, columns=['Word', 'Prob', 'Similarity'])
        # df.head()
        df = df.sort_values(by=['Similarity','Prob'], ascending=False)
        # df.head()
        return df.head()

suggestion_words = my_autocorrect('neverteless')
suggestion_words


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
