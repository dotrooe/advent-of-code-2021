from utils.file_utils import read_num_list


def main():
    arr = read_num_list('input.txt')
    print(f'part I: {measure_increases(arr)}')
    print(f'part II: {measure_increases_of_triplets(arr)}')


def measure_increases(arr: list):
    result = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            result += 1
    return result


def measure_increases_of_triplets(arr: list):
    triplets = []
    for i in range(len(arr) - 2):
        suma = arr[i] + arr[i + 1] + arr[i + 2]
        triplets.append(suma)
    return measure_increases(triplets)


if __name__ == '__main__':
    main()
