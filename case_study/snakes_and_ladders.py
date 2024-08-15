import random


class Dice:
    num: int = None

    def __init__(self, num):
        self.num = num

    def roll_dice(self):
        return random.randint(self.num, self.num * 6)


class Player:
    id: int = None
    name: str = None

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Board:
    destination: int = 100
    num_of_snakes: int = 0
    snakes: list[int, int] = []
    num_of_ladders: int = 0
    ladders: list[int, int] = []

    def __init__(self, destination: int, num_of_snakes: int, num_of_ladders: int):
        self.destination = destination
        self.num_of_snakes = num_of_snakes
        self.num_of_ladders = num_of_ladders
        self.init_board()

    def init_board(self):
        self.add_snakes()
        self.add_ladders()

    def add_snakes(self):
        start_already_taken: set = set()
        for _ in range(self.num_of_snakes):
            start = random.randint(1, self.destination)
            while start in start_already_taken:
                start = random.randint(1, self.destination)
            end = random.randint(1, start - 1)
            self.snakes.append([start, end])
            start_already_taken.add(start)

    def add_ladders(self):
        start_already_taken: set = set()
        for _ in range(self.num_of_snakes):
            start = random.randint(1, self.destination)
            while start in start_already_taken:
                start = random.randint(1, self.destination)
            end = random.randint(start + 1, self.destination)
            self.ladders.append([start, end])
            start_already_taken.add(start)


class Game:
    board: Board = None
    players: list[Player] = []
    curr_turn: Player = None
    dice: Dice = None
    curr_position: dict[Player, int] = {}

    def __init__(self, num_of_dice: int, num_of_snakes: int, num_of_ladders: int):
        self.board = Board(num_of_snakes, num_of_ladders)
        self.dice = Dice(num_of_dice)

    def add_player(self, player: Player):
        self.players.append(player)
        self.curr_position[player] = 0

    def get_next_turn(self):
        pass

    def start_play(self):
        pass
