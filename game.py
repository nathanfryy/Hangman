from pole import Pole
from player import Player
from words import wordList1, wordList2, wordList3
import toolbox
import random

class Game(object):

    def __init__(self):
        self.__pole = Pole()
        self.__player = Player()
        self.__word = ''
        self.__wrongGuesses = 0
        self.__rightGuesses = 0
        self.__characterNum = 0
        self.__lettersGuessed = []
        self.__hanged = False
        self.__categoryChoice = 0


    def main(self):
        """
        Main event loop for store.
        :return: None
        """
        command = 'startHelp'
        parameter = None
        while command != 'quit':
            if command == 'startHelp':
                self.help('help.txt')
                self.start_game()
            elif command == 'help':
                self.help('help.txt')
                print(self.show_pole() + '\n' + self.show_word() + '\n' + self.status())
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
        commands = {'h': 'startHelp',
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
        string = ''
        if self.__wrongGuesses == 0:
            string = self.__pole.get_manPrint()
        elif self.__wrongGuesses == 1:
            string = self.__pole.onlyHead()
        elif self.__wrongGuesses == 2:
            string = self.__pole.headBody()
        elif self.__wrongGuesses == 3:
            string = self.__pole.rightArm()
        elif self.__wrongGuesses == 4:
            string = self.__pole.leftArm()
        elif self.__wrongGuesses == 5:
            string = self.__pole.rightLeg()
        else:
            string = self.__pole.fullBody()
            self.__hanged = True
        return string

    def show_word(self):
        string = ''
        regString = ''
        currentLetter = ''
        for letter in self.__word:
            if letter in self.__lettersGuessed:
                currentLetter = f'  {letter}  '
                regString += letter
            else:
                currentLetter = '     '
            string += currentLetter
        string += '\n'
        for character in self.__word:
            string += ' ___ '
        if self.__hanged == True:
            string += f'\n\n******* You got hanged!!! *******'
        if regString == self.__word:
            print(string)
            print()
            string += f'\n\n******* You Guesses It!!! *******'
        return string

    def status(self):
        string = f'\nguessed letters: {self.__lettersGuessed} \n'
        string += f'wrong guesses: {self.__wrongGuesses} \n'
        string += f'right guesses: {self.__rightGuesses} \n'
        string += f'length of word: {self.__characterNum}\n\n'
        string += 'press: [G]uess   [?]elp  [N]ew Game'
        return string


    def start_game(self):
        self.__hanged = False
        self.__word = ''
        self.__wrongGuesses = 0
        self.__rightGuesses = 0
        self.__characterNum = 0
        self.__lettersGuessed = []
        multiplayer = toolbox.get_boolean('\nWould you like 2 players?')
        if multiplayer == False:
            self.__word = random.choice(self.get_category())
        else:
            self.__word = toolbox.get_string('\nPlayer 1 now enter the word you would like.')
            print('Player 2 will guess.')
        self.__characterNum = len(self.__word)
        print(self.show_pole() + '\n' + self.show_word() + '\nYour word is chosen' + '\n' + self.status())

    def get_category(self):
        print("\nHere are your categories of words to choose from:")
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
                while currentGuess in self.__lettersGuessed:
                    print(f'You have already guessed {currentGuess}.')
                    currentGuess = self.__player.guess()
            self.__lettersGuessed.append(currentGuess)
            rightGuess = False
            for letter in list(self.__word):
                if letter == currentGuess:
                    self.__rightGuesses += 1
                    rightGuess = True
            if rightGuess == False:
                self.__wrongGuesses += 1
            readyForPrint = True
        print(self.show_pole() + '\n' + self.show_word() + '\n' + self.status())



    def get_lettersGuesses(self):
        return self.__lettersGuessed




if __name__ =='__main__':
    simulation = Game()
    simulation.main()
