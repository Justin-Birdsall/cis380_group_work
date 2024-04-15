""" 
This python file "gets the game ready to play".
In real life Rummikub can be played with 2-4 players.
We are only implementing a 4 player version of the game as it was
the easiest for us to understand from a mathematical and algorithm design perspective. In theory it shouldn't be too hard to make it 2 or 3 or 4 person
"""
import random

RED = 0
ORANGE = 1
BLUE = 2
BLACK = 3

class Joker:
    def __init__(self):
        self.joker0 = [-1][-1]
        self.joker1 = [-1][-1]
        self.joker0_on_board = False
        self.joker1_on_board = False    

class Board:
    def __init__(self, seed):
        colors = 4 #red, orange, blue, black
        numbers = 13 #1-13
        self.seed = seed
        self.pool = [[2 for i in range(numbers)] for j in range(colors)]      
        self.table_tiles = [[0 for i in range(numbers)] for j in range(colors)]
        self.table_sets = [[0 for i in range(numbers)] for j in range(colors)]
        self.table_runs = [[0 for i in range(numbers)] for j in range(colors)]

class Player:
    def __init__(self, name, num):
        self.name = name 
        self.num = num
        self.hand = [[0] * 13 for _ in range(4)]
        self.played_30 = False
        self.joker_in_hand = 0

def init_draw(players, board):
    random.seed(board.seed)
    num = board.seed % 4
    for i in range(56):
        while True:
            color = random.randint(0, 3)
            number = random.randint(0, 12)
            if board.pool[color][number] > 0:
                board.pool[color][number] -= 1
                players[num].hand[color][number] += 1
                break
        num += 1    

def check_hand_sets(self):
    # check if player has 3 or 4 of the same number (different colors)
    for i in range(13):
        count = 0
        set_buffer = []
        for j in range(4):
            if self.hand[j][i] > 0:
                count += 1
                set_buffer.append((j, i))
        if count >= 3:
            # add to potential sets
            for pair in set_buffer:
                self.potential_sets[pair[0]][pair[1]] += 1
                
def check_hand_runs(self):
    for i in range(4):
        count = 0
        runs = 0
        run_buffer = []
        for j in range(13):
            if self.hand[i][j] > 0:
                count += 1
                if count == 3:
                    runs += 1
            else:
                if count >= 3:
                    # backtrack and add to buffer
                    for k in range(count, 0, -1):
                        run_buffer.append((i, j-k))
                count = 0
        # if there are runs up to the end, add to buffer
        if count >= 3:
            for k in range(count, 0, -1):
                run_buffer.append((i, 13-k))
        if runs > 0:
            for pair in run_buffer:
                self.potential_runs[pair[0]][pair[1]] += 1
                
                
board = Board(random.randint(0,99999))
player1 = Player("player1", 0)    
player2 = Player("player2", 1)     
player3 = Player("player3", 2)    
player4 = Player("player4", 3)
players = [player1,player2,player3,player4]
init_draw(players,board)



