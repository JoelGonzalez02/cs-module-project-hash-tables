import random
import re


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

'''
Plan:
    Split the words into single words and letters

'''
def textGenerator():
    wordSplit = ''.join([i for i in words]).replace('\n', ' ').split(' ')

    index = 1 
    chain = {}
    count = 24

    for word in wordSplit[index:]:
        key = wordSplit[index -1]
        if key in chain:
            chain[key].append(word)
        else:
            chain[key] = [word]
        index += 1

    word1 = random.choice(list(chain.keys()))
    message = word1.capitalize()

    while len(message.split(' ')) < count:
        word2 = random.choice(chain[word1])
        word1 = word2
        message += ' ' + word2
    return message





# TODO: construct 5 random sentences
# Your code here
print(f'\n Sentence 1: \n {textGenerator()}\n\n Sentence 2: \n {textGenerator()}\n\n Sentence 3: \n {textGenerator()}\n\n Sentence 4: \n {textGenerator()}\n\n Sentence 5: \n {textGenerator()}')

