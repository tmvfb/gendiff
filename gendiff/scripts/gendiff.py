#! usr/bin/env/python3
import argparse


def show_help():
    parser = argparse.\
             ArgumentParser(
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


def main():
    show_help()


if __name__ == '__main__':
    main()
