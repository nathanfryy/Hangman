import toolbox

class Player(object):

    def __init__(self):
        pass

    def guess(self):
        letter = toolbox.get_string('What is your letter guess?')
        if len(letter) > 1:
            letter = toolbox.get_string('What is your letter guess? Has to be one character.')
        if len(letter) < 1:
            letter = toolbox.get_string('What is your letter guess? Has to be one character.')
