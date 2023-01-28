import argparse


def add_cli():
    parser = argparse.ArgumentParser(
        description='''Compares two configuration
        files and shows a difference.'''
    )
    parser.add_argument('file1', metavar='first_file')
    parser.add_argument('file2', metavar='second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output', default='stylish',
                        choices=['stylish', 'plain', 'json'])
    args = parser.parse_args()
    return args
