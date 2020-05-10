import toolbox

class Player(object):

    def __init__(self):
        pass

    def guess(self):
        letter = toolbox.get_string('What is your letter guess?')
        if len(letter) != 1:
            print('Your guess has to be one character.')
            self.guess()
        if letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9' or letter == '0':
            print('Your guess has to be a letter.')
            self.guess()
        return letter
