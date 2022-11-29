from utils.file_utils import read_file


def main():
    arr = read_file('input.txt').split(',')
    num_arr = []
    for el in arr:
        el = int(el)
        num_arr.append(el)
    print(num_arr)
    print(count_fish(num_arr))


def count_fish(arr: list):
    total_days = 81     # ?
    for day in range(1, total_days):
        timers = []
        new_fish = []
        for fish in arr:
            if fish == 0:
                new_fish.append(8)
                fish = 6
            else:
                fish -= 1
            timers.append(fish)
        timers.extend(new_fish)
        arr = timers
    return len(timers)


if __name__ == '__main__':
    main()
