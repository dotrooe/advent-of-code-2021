from utils.file_utils import read_file


def main():
    arr = read_file('input.txt').split(',')
    num_arr = []
    for el in arr:
        el = int(el)
        num_arr.append(el)
    print(count_fish_efficient_way(num_arr))
    print(count_fish_efficient_way(num_arr, 256))


def count_fish_efficient_way(arr: list, total_days: int = 80):
    fish_school = populate_from_list(arr)
    for i in range(total_days):
        fish_school = shift_array(fish_school)
        fish_school[6] += fish_school[8]
    return sum(fish_school)


def shift_array(arr: list):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[(i + 1) % len(arr)])
    return new_arr


def populate_from_list(arr: list):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for el in arr:
        result[el] += 1
    return result


def count_fish(arr: list, total_days: int = 80):
    for day in range(total_days):
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
