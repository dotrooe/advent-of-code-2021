from utils.file_utils import read_num_list


def main():
    arr = read_num_list('input.txt')
    print(measure_increases(arr))


def measure_increases(arr: list):
    result = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            result += 1
    return result


if __name__ == '__main__':
    main()
