from utils.file_utils import read_file


def main():
    arr = read_file('input.txt').split()
    for i in range(1, len(arr)):
        if i % 2 == 0:
            continue
        else:
            arr[i] = int(arr[i])
    print(dive_part1(arr))
    print(dive_part2(arr))


def dive_part1(arr: list):
    hor_position = 0
    depth = 0
    for i in range(len(arr) - 1):
        position = arr[i]
        amount = arr[i + 1]
        if position == 'forward':
            hor_position += amount
        elif position == 'down':
            depth += amount
        elif position == 'up':
            depth -= amount
    return depth * hor_position


def dive_part2(arr: list):
    depth = 0
    hor_position = 0
    aim = 0
    for i in range(len(arr) - 1):
        position = arr[i]
        amount = arr[i + 1]
        if position == 'forward':
            hor_position += amount
            depth += aim * amount
        elif position == 'down':
            aim += amount
        elif position == 'up':
            aim -= amount
    return depth * hor_position


if __name__ == '__main__':
    main()
