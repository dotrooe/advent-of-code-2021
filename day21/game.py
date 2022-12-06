from dice import Dice
from player import Player


def main():
    dice = Dice()
    player1 = Player(8)
    player2 = Player(7)

    current_player = player1
    while player1.score < 1000 and player2.score < 1000:
        make_turn(current_player, dice)
        current_player = switch_player(current_player, player1, player2)
    print('### RESULTS: ###')
    if player1.score > player2.score:
        print(player2.score * dice.roll_count)
    else:
        print(player1.score * dice.roll_count)
    print(f'Player 1 score: {player1.score}')
    print(f'Player 2 score: {player2.score}')
    print(f'dice rolls: {dice.roll_count}')


def switch_player(current_player, player1, player2):
    return player1 if current_player == player2 else player2


def make_turn(current_player, dice):
    rolled = dice.roll_n_times(3)
    new_position = calculate_new_position(current_player, rolled)
    current_player.move_to(new_position)
    current_player.add_score(new_position)


def calculate_new_position(player, rolled):
    new_position = player.position + rolled
    new_position %= 10
    if new_position == 0:
        new_position = 10
    return new_position


if __name__ == '__main__':
    main()
