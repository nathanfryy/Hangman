from pole import Pole
from player import Player
from words import wordList1, wordList2, wordList3
import random
import toolbox

class Game(object):

    def __init__(self):
        self.__pole = Pole()
        self.__player = Player()
        self.__word = ''
        self.__wrongGuesses = 0
        self.__rightGuesses = 0
        self.__characterNum = 0
        self.__lettersGuessed = []
        self.__categoryChoice = 0

    def main(self):
        """
        Main event loop for store.
        :return: None
        """
        command = 'help'
        parameter = None
        while command != 'quit':
            if command == 'help':
                self.help('help.txt')
                self.start_game()
            elif command == 'newGame':
                self.start_game()
            elif command == 'guess':
                self.take_guess()


            command, parameter = self.get_command()
        print('goodbye')

    def get_command(self):
        """
        Get a valid command from the user.
        :return: command, parameter
        """
        commands = {'h': 'help',
                    '?': 'help',
                    'q': 'quit',
                    'n': 'newGame',
                    'g': 'guess'}

        validCommands = commands.keys()

        userInput = '&'
        parameter = None
        while userInput[0].lower() not in validCommands:
            userInput = input()
            if userInput == '':
                userInput = 'n'
                parameter = 1
        command = commands[userInput[0].lower()]
        if len(userInput) > 1:
            parameter = userInput[1:].strip()
        return command, parameter



    def help(self, filename, prompt = None):
        """
        Displays instructions.
        :param filename: The string of helping instructions.
        :param prompt:
        :return: None
        """
        with open(filename, 'r') as file:
            help = file.read()
        print(help, end='')
        if prompt:
            input('\n' + prompt)
        hi = input("\n\npress <return> to continue")

    def show_pole(self):
        string = self.__pole.get_manPrint()
        return string

    def show_word(self):
        string = ''
        counter = 0
        for letter in list(self.__word):
            for guess in self.__lettersGuessed:
                if letter == guess:
                    string += letter
                else:
                    string += '  '
        if string == self.__word:
            print(string)
            print()
            string = 'Game over'
        return string

    def start_game(self):
        self.__word = ''
        self.__wrongGuesses = 0
        self.__rightGuesses = 0
        self.__characterNum = 0
        self.__lettersGuessed = []
        self.__word = random.choice(self.get_category())
        self.__characterNum = len(self.__word)
        print(self.__word)
        print(self.show_pole() + '\n' + self.show_word())
        print('Your word is chosen')

    def get_category(self):
        print("Here are your categories of words to choose from:")
        print("1. Animals     2. Foods     3. Sports")
        self.__categoryChoice = toolbox.get_integer_between(1, 3, 'Which category do you want to use? ')
        if self.__categoryChoice == 1:
            self.__categoryChoice = wordList1
        elif self.__categoryChoice == 2:
            self.__categoryChoice = wordList2
        else:
            self.__categoryChoice = wordList3
        return self.__categoryChoice

    def take_guess(self):
        currentGuess = self.__player.guess()
        readyForPrint = False
        while readyForPrint == False:
            for letter in self.__lettersGuessed:
                if currentGuess == letter:
                    self.take_guess()
            self.__lettersGuessed.append(currentGuess)
            rightGuess = False
            for letter in list(self.__word):
                if letter == currentGuess:
                    self.__rightGuesses += 1
                    rightGuess = True
            if rightGuess == False:
                self.__wrongGuesses += 1
            readyForPrint = True
        print(self.__rightGuesses)
        print(self.__wrongGuesses)
        print(self.show_pole() + '\n' + self.show_word())




if __name__ =='__main__':
    simulation = Game()
    simulation.main()
