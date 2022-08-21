word_to_count = {}
text = input('Enter text: ')
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
for word in words:
    print("{}: {}".format(word, word_to_count[word]))