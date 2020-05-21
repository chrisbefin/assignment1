import re
import argparse

class Character(object):
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.words = dict() #key: word, value: occurences

    def getNumWords(self):
        total = 0
        for word in self.words:
            total += words[word]
        return total

    def getFreqWord(self):
        max = 0
        for word in words:
            if words[word] > max:
                max = words[word]
                result = word
        return word

    def addWord(self, word):
        if word in words:
            words[word] += 1

parser = argparse.ArgumentParser()
parser.add_argument("input", help="file path for text to be parsed")
args = parser.parse_args()
filename = args.input
try:
    with open(filename, mode='r') as READ_FILE:
        fileText = READ_FILE.read()
except:
    print("Bad input file")
    exit(1)
else:
    lines = fileText.split('\n')
    reserved_words = ['Exit', 'Enter', 'Aside', 'Exeunt']
    characters = dict()#key: character name, value: list of lines spoken
    current_character = None
    word_count = dict()#key: character name, value: words spoken

#strip spaces
    for line in lines:
        if len(line) != 0:
            words = line.split(' ')
            if len(words) == 1:
                if words[0] not in characters:
                    characters[words[0]] = []
                    word_count[words[0]] = 0
                if current_character != None:
                    characters[current_character].append('\n')
                current_character = words[0]
            elif current_character != None:
                characters[current_character].append(line)
                if not any(word in line for word in reserved_words):
                    line = re.sub("([\[]).*?([\]])", '', line)
                    line = re.sub(' +', ' ', line) #strip leading spaces
                    word_count[current_character] += (len(line.split(' '))-1)

    characters[current_character].append('\n')

    file = open("output.txt", 'w')#contextual open/coding
    for character in sorted(characters):#sorted(, key= func())
        file.write("{} ({}) \n".format(character, word_count[character]))
        for line in characters[character]:
            file.write("{}\n".format(line))
    file.close()

    #print("   ", end='')
