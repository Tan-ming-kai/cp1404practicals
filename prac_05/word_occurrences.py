"""
Word occurrences
Estimate: 15 mins
Actual: 20 mins
"""
from operator import *
word_to_count = {}
user_text = input("Enter a long text here: ")
for word in user_text.split():
    word_to_count[word] = word_to_count.get(word, 0) + 1

longest_word = max(len(word) for word in list(word_to_count))
for word,count in sorted(word_to_count.items()):
    print(f"{word:{longest_word+1}}: {count}")

