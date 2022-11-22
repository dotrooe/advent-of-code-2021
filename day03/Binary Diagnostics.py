from utils.file_utils import read_list


def main():
    arr = read_list('input.txt')
    print(diagnostics_part1(arr))
    print(diagnostics_part2(arr))


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


def diagnostics_part2(arr: list):
    return find_oxygen_gen_rating(arr) * find_co2_scrubber_rating(arr)


def find_oxygen_gen_rating(report: list):
    result = filter_by_most_common_bit_on(0, report)
    return int(result[0], base=2)


def find_co2_scrubber_rating(report: list):
    result = filter_by_least_common_bit_on(0, report)
    return int(result[0], base=2)


def filter_by_most_common_bit_on(pos: int, report: list):
    if len(report) == 1:
        return report
    mcb = find_most_common_bit_on(pos, report)
    result = []
    for report_line in report:
        if report_line[pos] == mcb:
            result.append(report_line)
    return filter_by_most_common_bit_on(pos + 1, result)


def filter_by_least_common_bit_on(pos: int, report: list):
    if len(report) == 1:
        return report
    mcb = find_most_common_bit_on(pos, report)
    result = []
    for report_line in report:
        if report_line[pos] != mcb:
            result.append(report_line)
    return filter_by_least_common_bit_on(pos + 1, result)


def find_most_common_bit_on(pos: int, report: list):
    zeros_count = 0
    ones_count = 0
    for report_line in report:
        if report_line[pos] == '0':
            zeros_count += 1
        else:
            ones_count += 1
    return '1' if ones_count >= zeros_count else '0'


if __name__ == '__main__':
    main()
