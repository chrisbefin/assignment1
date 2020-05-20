import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()
filename = args.input
with open(filename, mode='r') as READ_FILE:
    fileText = READ_FILE.read()

lines = fileText.split('\n')
reserved_words = ['Exit', 'Enter', 'Aside', 'Exeunt']
characters = dict()
current_character = None
word_count = dict()

for line in lines:
    if len(line) != 0:#not a blank line
        words = line.split(' ')
        if len(words) == 1:
            if words[0] not in characters:#new character
                characters[words[0]] = []
                word_count[words[0]] = 0
            if current_character != None:
                characters[current_character].append('\n')#end of a character's line of dialogue
            current_character = words[0]
        elif current_character != None:#someone is speaking
            if not any(word in line for word in reserved_words):#line does not contain any reserved words
                characters[current_character].append(line)#line is added to the current character's dialogue
                line = re.sub("\[-+\]", ' ', line)
                line = re.sub(' +', ' ', line)#replace multiple spaces with single spaces
                word_count[current_character] += (len(line.split(' '))-1)

f = open("output.txt", 'w')
for key in sorted(characters):
    f.write("{} ({}) \n" .format(key, word_count[key]))
    for line in characters[key]:
        f.write("{}\n" .format(line))
f.close()
