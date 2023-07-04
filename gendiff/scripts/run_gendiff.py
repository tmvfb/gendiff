#! usr/bin/env/python3
# NB! never name scripts the same as your package
from gendiff import add_cli, generate_diff


def main():
    args = add_cli()
    print(generate_diff(args.file1, args.file2, args.format))


if __name__ == '__main__':
    main()
