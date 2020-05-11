import toolbox

class Player(object):

    def __init__(self):
        pass

    def guess(self):
        letter = toolbox.get_string('What is your letter guess?')
        while len(letter) != 1:
            print('Your guess has to be one character.')
            letter = toolbox.get_string('What is your letter guess?')
            while letter in ['1','2','3','4','5','6','7','8','8','9','0']:
                print('Your guess has to be a letter.')
                letter = toolbox.get_string('What is your letter guess?')
                while letter in game.get_lettersGuesses():
                    print('You have already guessed that.')
                    letter = toolbox.get_string('What is your letter guess?')
        return letter
