from pole import Pole

class Game(object):

    def __init__(self):
        self.__word = ''
        self.__wrongGuesses = 0
        self.__rightGuesses = 0
        self.__characterNum = 0
        self.__lettersGuessed = []

    def main(self):
        """
        Main event loop for hangMan
        :return: None
        """

        command = 'help'
        parameter = None
        while command != 'quit':
            if command == 'help:':
                self.help('help.txt')

    def get_command(self):
        """
        Get a valid command from the user
        :return: command, parameter
        """
        commands = {'h': 'help'}

        validCommands = commands.keys()

        userInputs = '&'
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
        print(Pole.__manPrint)
        with open(filename, 'r') as file:
            help = file.read()
        print(help, end='')
        if prompt:
            input('\n' + prompt)
        hi = input("\n\npress <return> to continue")

if __name__ =='__main__':
    simulation = Game()
    simulation.main()
