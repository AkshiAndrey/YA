import argparse


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("ERROR")
        exit()


def print_file_content(file_name, args):
    lines = read_file(file_name)
    for i, line in enumerate(lines):
        lines[i] = line.strip()

    if args.sort:
        lines.sort()

    if args.num:
        lines = [f"{idx} {line.strip()}" for idx, line in enumerate(lines)]

    for line in lines:
        print(line)

    if args.count:
        print(f"Количество строк в файле: {len(lines)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Программа для вывода содержимого файла с различными опциями')
    parser.add_argument('file_name', type=str, help='Имя файла для чтения')
    parser.add_argument('--sort', action='store_true', help='Сортировать строки в алфавитном порядке')
    parser.add_argument('--num', action='store_true', help='Вывести порядковый номер для каждой строки')
    parser.add_argument('--count', action='store_true', help='Вывести количество строк в конце')

    args = parser.parse_args()

    print_file_content(args.file_name, args)
