from utils.file_utils import read_list


def main():
    arr = read_list('input.txt')
    print(diagnostics_part1(arr))


def diagnostics_part1(arr: list):
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(arr[0])):
        every_input = [input[i] for input in arr]
        if every_input.count('0') > len(arr) / 2:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    return int(gamma_rate, base=2) * int(epsilon_rate, base=2)


if __name__ == '__main__':
    main()
