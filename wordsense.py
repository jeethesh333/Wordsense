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
