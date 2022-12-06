class Dice:
    roll_count = 0  # or in __init__

    def __init__(self):
        self.roll_count = 0

    def roll(self):
        result = self.roll_count % 100 + 1
        self.roll_count += 1
        return result

    def roll_n_times(self, n):
        rolled_sum = 0
        for i in range(n):
            rolled_sum += self.roll()
        return rolled_sum


def main():
    # this is manual testing method
    dice = Dice()
    for _ in range(110):
        print(dice.roll())
    print(f'Rolled dice {dice.roll_count} times')


if __name__ == '__main__':
    main()
