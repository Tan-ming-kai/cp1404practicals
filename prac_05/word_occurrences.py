"""
Word occurrences
Estimate: 15 mins
Actual:
"""
word_to_count = {}
user_text = input("Enter a long text here: ")
for word in user_text.split():
    word_to_count[word] = word_to_count.get(word, 0) + 1

print(word_to_count)

