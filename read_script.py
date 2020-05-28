#!usr/bin/env python

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
            returns: None
        parseFile(): primary routine which parses the inputFile and assigns lines to characters and counts the number of words spoken by each character
            arguments: self
            returns: None
        output(): writes formatted script to the object's outputFile
            arguments: self
            returns: None
        print(): prints formatted output to the terminal
            arguments: self
            returns: None
        characterSummary():prints summary to terminal for each character
            arguments: self
            returns: None
    """
    def __init__(self, inputFile, outputFile):
        """
        __init__(): initializes the object with correct file paths, the reserved_words list can be added to as needed to identify all stage direction lines appearing in the script
            arguments: self, inputFile<string>, outputFile<string>
            returns: None
        """
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.characters = dict() # key:character name, value: character object
        self.reserved_words = ['Exit', 'Enter', 'Aside', 'Exeunt']

    def parseFile(self):
        """
        parseFile(): primary routine which parses the inputFile line by line. It creates character objects for each character as they appear in the script and then assigns those character objects lines and updates their word count dict. It identifies stage direction lines using this class' list of reserved words and does not count those toward word count.
        <raises an OSError if input file cannot be opened>
            arguments: self
            returns: None
        """
        try:
            with open(self.inputFile, mode='r') as READ_FILE:
                fileText = READ_FILE.read()
        except OSError:
            raise OSError("bad input file")
        else:
            lines = fileText.split('\n') # divide file into lines
            current_character = None

            for line in lines:
                if len(line) != 0:
                    words = line.split(' ')
                    if len(words) == 1: # a one word line
                        if words[0] not in self.characters: # character speaking for the first time
                            self.characters[words[0]] = Character(words[0]) # create object for new character
                        if current_character != None:
                            self.characters[current_character].addLine('\n')
                        current_character = words[0] # update who is talking
                    elif current_character != None: # someone is currently talking
                        self.characters[current_character].addLine(line)
                        if not any(word in line for word in self.reserved_words): # this line is not stage direction
                            line = re.sub("([\[]).*?([\]])", '', line) # replace brackets and their contents with whitespace
                            line = re.sub("--", ' ', line) # replace -- with a space
                            line = line.translate(str.maketrans('!?,;:.', '      ')) # replace punctuation marks with spaces
                            line = re.sub(' +', ' ', line) # reduce multiple spaces to one
                            line = line.strip(' ') # strip leading and trailing spaces
                            words = line.split(' ') # divide line into words
                            for word in words:
                                self.characters[current_character].addWord(word.upper()) # add all words in the line to the character
            self.characters[current_character].addLine('\n') # edge case resolution

    def output(self):
        """
        output(): writes formatted script to the object's outputFile- lines grouped by character and characters organized alphabetically. Word count and most spoken word printed next to each character name. Stage directions are outputted as if they were lines spoken by whoever was talking at the time they were given, however stage directions do not count towards word count.
            arguments: self
            returns: None
        """
        with open(self.outputFile, mode='w') as WRITE_FILE:
            for character in sorted(self.characters):
                WRITE_FILE.write("{} ({}) ({}) \n".format(character, self.characters[character].getNumWords(),self.characters[character].getFreqWord())) # write character's name with word count and most frequently spoken word
                for line in self.characters[character].getLines():
                    WRITE_FILE.write("{}\n".format(line)) # write all of the character's lines

    def print(self):
        """
        print(): prints same formatted output to the terminal as is going into the outputFile
            arguments: self
            returns: None
        """
        for character in sorted(self.characters):
            print("{} ({}) ({}) \n".format(character, self.characters[character].getNumWords(),self.characters[character].getFreqWord())) # write character's name with word count and most frequently spoken word
            for line in self.characters[character].getLines():
                print("{}\n".format(line)) # write all of the character's lines

    def characterSummary(self):
        """
        characterSummary(): prints summary to terminal for each character- name, words spoken and most spoken word
            arguments: self
            returns: None
        """
        for character in sorted(self.characters):
            print("name: {}".format(character))
            print("words spoken: {}".format(self.characters[character].getNumWords()))
            print("most spoken word: {}".format(self.characters[character].getFreqWord()))
            print()

class Character(object):
    """ class for characters found in the script file being parsed
        data members:
            name: name of the character as it appears in the script
            lines: a list of lines spoken by the character and stage directions appearing while this character is speaking
            words: a dict containing the words spoken by the character and the number of times they are spoken
        methods:
            __init__(): initializes object with correct name and empty lines and words data members.
                arguments: self, name<string>
                returns: None
            getNumWords(): counts a character's spoken words
                arguments: self
                returns: number of words spoken by the character
            getFreqWord(): finds a character's most commonly spoken word
                arguments: self
                returns: the character's most spoken word
            addWord(): increments the words dict given a single spoken word
                arguments: self, word<string>
                returns: None
            addLine(): appends a new line to the character's list of lines
                arguments: self, line<string>
                returns: None
            getLines(): retrieves all of the character's lines
                arguments: self
                returns: list of the character's lines
    """
    def __init__(self, name):
        """
        __init__(): initializes object with correct name and empty lines and words data members.
            arguments: self, name<string>
            returns: None
        """
        self.name = name
        self.lines = []
        self.words = dict()

    def getNumWords(self):
        """
        getNumWords(): counts a character's spoken words
            arguments: self
            returns: number of words spoken by the character
        """
        total = 0
        for word in self.words: # loop through all words
            total += self.words[word] # sum the mentions of all words
        return total #  return sum of all mentions

    def getFreqWord(self):
        """
        getFreqWord(): finds a character's most commonly spoken word
            arguments: self
            returns: the character's most spoken word
        """
        max = 0
        for word in self.words:
            if self.words[word] > max: # loop through all words to find word with most mentions
                max = self.words[word]
                result = word
        return result # return word with most mentions

    def addWord(self, word):
        """
        addWord(): increments the words dict given a single spoken word
            arguments: self, word<string>
            returns: None
        """
        if word in self.words:
            self.words[word] += 1 # increment an existing word's count
        else:
            self.words[word] = 1 # initialize new word with count of 1

    def addLine(self, line):
        """
        addLine(): appends a new line to the character's list of lines
            arguments: self, line<string>
            returns: None
        """
        self.lines.append(line)

    def getLines(self):
        """
        getLines(): retrieves all of the character's lines
            arguments: self
            returns: list of the character's lines
        """
        return self.lines

def main():
    """ Parses command line arguments and creates a play class to parse input and generate output
        arguments: none
        returns: None
        <Will return 1 if input file cannot be opened>
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="file path for text to be parsed")
    parser.add_argument("output", help="file path for file for output to be written to")
    args = parser.parse_args() # parse command line arguments
    inputFile = args.input
    outputFile = args.output

    PlayClass = Play(inputFile, outputFile) # create play class
    try:
        PlayClass.parseFile() # parse script
    except OSError:
        print("OSError raised. Execution halted")
        exit(1)
    PlayClass.output() # write output to file
    PlayClass.characterSummary() # print summary to terminal

if __name__ == "__main__":
    main()
