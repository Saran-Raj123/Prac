string = input("Text: ")
count = dict()

words = string.split()

for word in words:
    frequency = count.get(word, 0)
    count[word] = frequency + 1

words = list(count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, count[word]))