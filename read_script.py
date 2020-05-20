import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()
filename = args.input
try:
    with open(filename, mode='r') as READ_FILE:
        fileText = READ_FILE.read()
except:
    print("Bad input file")
else:
    lines = fileText.split('\n')
    reserved_words = ['Exit', 'Enter', 'Aside', 'Exeunt']
    characters = dict()#key: character name, value: array of lines spoken
    current_character = None
    word_count = dict()#key: character name, value:words spoken

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
                    line = re.sub(' +', ' ', line)
                    word_count[current_character] += (len(line.split(' '))-1)

    characters[current_character].append('\n')

    f = open("output.txt", 'w')
    for character in sorted(characters):
        f.write("{} ({}) \n" .format(character, word_count[character]))
        for line in characters[character]:
            f.write("{}\n" .format(line))
    f.close()
