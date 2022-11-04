from copy import deepcopy
import random as rnd

def load_dictionary():
    dictionary_data = []
    with open('dictionary.txt') as f:
        [dictionary_data.append(line.strip()) for line in f.readlines()]

    return dictionary_data

class letter:
    def __init__(self, name, points, distribution):
        self.name = name
        self.points = points
        self.distribution = distribution
    
class bag:
    def __init__(self,letters):
        self.letter_ref = letters
        self.play_letters = []

    def generate_bag(self):
        for i, value in enumerate(self.letter_ref):
            for a in range(0, (value.distribution)):
                # copy = deepcopy[value]
                self.play_letters.append(value.name)
        # self.play_letters.append('blank')
        # self.play_letters.append('blank')

    def pick_scrabble(self, player):
        len(player.rack)
        letters_returned = []
        while(len(letters_returned) < (7 - len(player.rack))):
            letters_returned.append(self.play_letters.pop())
        return letters_returned
    
    def shuffle(self):
        current_index = len(self.play_letters)
        while 0 != current_index: 
            rand_index = rnd.randint(0,(len(self.play_letters) - 1))
            current_index -= 1
            temp_value = self.play_letters[current_index]
            self.play_letters[current_index] = self.play_letters[rand_index]
            self.play_letters[rand_index] = temp_value

class player:
    def __init__(self):
        self.rack = []
        self.points = 0
        self.longest_word = ''
        self.highest_scoring_word = ''

    def find_valid_word(self, dictionary):
        valid_words = [] #store valid words
        possible_valid_words = [] #store possible words from dic
        possible_words_in_creation = [] #stores the concatenated current values
        


        # check the first letter if there are any matches return to possible valid words
        # check the following letters if there are any matches that are longer than previous return to possible valid words
        # 

    




LETTERS_ATTRIBUTES = [
    letter('E', 1, 12),
    letter('A', 1, 9),
    letter('I', 1, 9),
    letter('O', 1, 8),
    letter('N', 1, 6),
    letter('R', 1, 6),
    letter('T', 1, 6),
    letter('L', 1, 4),
    letter('S', 1, 4),
    letter('U', 1, 4),
    letter('D', 2, 4),
    letter('G', 2, 3),
    letter('B', 3, 2),
    letter('C', 3, 2),
    letter('M', 3, 2),
    letter('P', 3, 2),
    letter('F', 4, 2),
    letter('H', 4, 2),
    letter('V', 4, 2),
    letter('W', 4, 2),
    letter('Y', 4, 2),
    letter('K', 5, 1),
    letter('J', 6, 1),
    letter('X', 6, 1),
    letter('Q', 10, 1),
    letter('Z', 10, 1),
]

LETTERS_TEST = [
    letter('E', 1, 12),
    letter('A', 1, 9),
]

def main():
    game_dictionary = load_dictionary()
    game_bag = bag(LETTERS_ATTRIBUTES)
    game_bag.generate_bag()
    game_bag.shuffle()

    player1 = player()
    player1.rack = game_bag.pick_scrabble(player1)
    print('Your current rack is -------------->', player1.rack)
    player1.find_valid_word(game_dictionary)    






    # testing for amounts
    # for i in game_bag.play_letters:
    #     print(i)
    # print(game_bag.play_letters.count('E'))
    # print('----------------------------', len(game_bag.play_letters))
    # game_bag.shuffle()

    # for i in game_bag.play_letters:
    #     print(i)
    print('----------------------------', len(game_bag.play_letters))



main()