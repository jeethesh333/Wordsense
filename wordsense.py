from pathlib import Path
import re
from collections import Counter

file_path = Path('words.txt')
file_content = file_path.read_text()

words = re.findall(r'\w+', file_content.lower())

V = set(words)

word_freq = {}
word_freq = Counter(words)

probs = {}

total_sum = sum(word_freq.values())

for word, freq in word_freq.items():
    probs[word] = freq / total_sum

print(probs)


def my_autocorrect(input_word):
    similarity_scores = [(input_word, textdistance.jaccard(input_word, word),word) for word in word_freq.keys()]
    df = pd.DataFrame(similarity_scores, columns=['Word', 'Prob', 'Similarity'])
    return df

test_input = 'hel'

input_word = test_input.lower()  # Convert input word to lowercase
 
if input_word not in V:
    result = my_autocorrect(input_word)
    suggestion_words = result.sort_values(by=['Prob'], ascending=False)
  
    print(suggestion_words.head())
else:
    print('Your word seems to be correct')

pip install levenshtein

import Levenshtein
def correction_suggestion(word):
    word = word.lower()
    if word in V:
        return word
    else:
        suggestions = [w for w in V if Levenshtein.ratio(word, w) > 0.8]
        if suggestions:
            return suggestions[0:2]
        else:
            return None

result = correction_suggestion('anaconda')
result
