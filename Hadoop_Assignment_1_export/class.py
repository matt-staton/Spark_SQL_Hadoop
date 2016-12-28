def read_input(file):
for line in file
    yield line.split()



f1 = open('mappe.txt', 'r')
gen1 = read_input(f1)

for words in gen1:
    #print resulst returned by generator
    print(words)


def count_words(words):
    word2count = {}
    for words in words:
        try:
            word2count[word] = word2count[word] + 1
        except:
            word2count[word] = 1

    return word2count

for words in gen:
    print("--> ", count_words(words))


def read_key_value(file):
    for line in file:
        yield lin_split('\+')