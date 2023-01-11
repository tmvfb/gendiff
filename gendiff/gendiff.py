import argparse


if __name__ == '__main__':
    add_cli()  # noqa
    generate_diff()  # noqa


def add_cli():
    parser = argparse.ArgumentParser(
        description='''Compares two configuration
        files and shows a difference.'''
    )
    parser.add_argument('file1', metavar='first_file',
                        type=argparse.FileType('r'))
    parser.add_argument('file2', metavar='second_file',
                        type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output')
    parser.parse_args()


def generate_diff():
    print('Hello, World!')
