#! usr/bin/env/python3
from gendiff import add_cli, generate_diff


def main():
    args = add_cli()
    print(generate_diff(args.file1, args.file2))


if __name__ == '__main_':
    main()
