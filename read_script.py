import re
import argparse
import string

class Play(object):
    """ class which parses a play script and generates output formatted such that all of a character's lines appear together
    data members:
        inputFile: path of the file to be read from
        outputFile: path of the file to be written to
        characters: dict of character objects, one for each character appearing in the script file
        reserved_words: list of words which indicate that a line is not spoken dialogue
    methods:
        __init__(): initializes the object with correct file paths
            arguments: self, inputFile<string>, outputFile<string>
            returns: void
        parseFile(): primary routine which parses the inputFile and assigns lines to characters and counts the number of words spoken by each character
            arguments: self
            returns: void
        output(): writes formatted script to the object's outputFile
            arguments: self
            returns: void
    """
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.characters = dict()
        self.reserved_words = ['Exit', 'Enter', 'Aside', 'Exeunt']

    def parseFile(self):
        try:
            with open(self.inputFile, mode='r') as READ_FILE:
                fileText = READ_FILE.read()
        except OSError:
            print("Bad input file")
            exit(1)
        else:
            lines = fileText.split('\n')#divide file into lines
            current_character = None

            for line in lines:
                if len(line) != 0:
                    words = line.split(' ')
                    if len(words) == 1:
                        if words[0] not in self.characters:
                            self.characters[words[0]] = Character(words[0])
                        if current_character != None:
                            self.characters[current_character].addLine('\n')
                        current_character = words[0]#a new character is talking
                    elif current_character != None:#someone is currently talking
                        self.characters[current_character].addLine(line)
                        if not any(word in line for word in self.reserved_words):#this line is not stage direction
                            line = re.sub("([\[]).*?([\]])", '', line)#replace brackets and their contents with whitespace
                            line = re.sub("--", ' ', line)#replace -- with a space
                            line = line.translate(str.maketrans('!?,;:.', '      '))#replace punctuation marks with spaces
                            line = re.sub(' +', ' ', line)#reduce multiple spaces to one
                            line = line.strip(' ')#strip leading and trailing spaces
                            words = line.split(' ')#divide line into words
                            for word in words:
                                self.characters[current_character].addWord(word.upper())#add all words in the line to the character

    def output(self):
        with open(self.outputFile, mode='w') as WRITE_FILE:
            for character in sorted(self.characters):
                WRITE_FILE.write("{} ({}) ({}) \n".format(character, self.characters[character].getNumWords(),self.characters[character].getFreqWord()))#write character's name with word count and most frequently spoken word
                for line in self.characters[character].getLines():
                    WRITE_FILE.write("{}\n".format(line))#write all of the character's lines

class Character(object):
    """ class for characters found in the script file being parsed
        data members:
            name: name of the character as it appears in the script
            lines: a list of lines spoken by the character
            words: a dict containing the words spoken by the character and the number of times they are spoken
        methods:
            __init__(): initializes object with correct name and empty lines and words data members.
            getNumWords(): counts a character's spoken words
                arguments: self
                returns: number of words spoken by the character
            getFreqWord(): finds a character's most commonly spoken word
                arguments: self
                returns: the character's most spoken word
            addWord(): increments the words dict given a single spoken word
                arguments: self, word<string>
                returns: void
            addLine(): appends a new line to the character's list of lines
                arguments: self, line<string>
                returns: void
            getLines(): retrieves all of the character's lines
                arguments: self
                returns: list of the character's lines
    """
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.words = dict()

    def getNumWords(self):
        total = 0
        for word in self.words:#loop through all words
            total += self.words[word]#sum the mentions of all words
        return total#return sum of all mentions

    def getFreqWord(self):
        max = 0
        for word in self.words:
            if self.words[word] > max:#loop through all words to find word with most mentions
                max = self.words[word]
                result = word
        return result#return word with most mentions

    def addWord(self, word):
        if word in self.words:
            self.words[word] += 1 #increment an existing word's count
        else:
            self.words[word] = 1 #initialize new word with count of 1

    def addLine(self, line):
        self.lines.append(line)

    def getLines(self):
        return self.lines

def main():
    """ Parses command line arguments and creates a play class to parse input and generate output
        arguments: none
        returns: void
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="file path for text to be parsed")
    parser.add_argument("output", help="file path for file for output to be written to")
    args = parser.parse_args()#parse command line arguments
    inputFile = args.input
    outputFile = args.output

    PlayClass = Play(inputFile, outputFile)#create play class
    PlayClass.parseFile()
    PlayClass.output()

if __name__ == "__main__":
    main()
