class Player:
    position: int
    score: int

    def __init__(self, position):
        self.score = 0
        self.position = position

    def move_to(self, new_position):
        self.position = new_position

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f'pos: {self.position}\tscore: {self.score}'


def main():
    # this is manual testing method
    player1 = Player(4)
    player2 = Player(8)
    player2.add_score(30)
    player2.add_score(21)
    print(player1)
    print(player2)


if __name__ == '__main__':
    main()
