"""Encrypt or decrypt from stdin/stdout
Usage:
    cape [command] [file]

Encrypt stdin and save to 'encrypted.dat'
    cape encrypt > encrypted.dat

Encrypt 'sensitive.txt' and save to 'encrypted.dat'
    cape encrypt sensitive.txt > encrypted.dat

Decrypt 'encrypted.dat' and print to stdout
    cape decrypt < encrypted.dat

Hash 'file' and save to 'file.hash'
    cape hash file > file.hash

The password and salt will be taken from stdin.
"""
import os
import sys

from cape import Cape


PY3K = sys.version_info >= (3, 0)

if PY3K:
    source = sys.stdin.buffer
else:
    # Python 2 on Windows opens sys.stdin in text mode, and
    # binary data that read from it becomes corrupted on \r\n
    if sys.platform == "win32":
        # set sys.stdin to binary mode
        import msvcrt
        msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)
    source = sys.stdin


def stringify(bytes):
    for c in bytes:
        if c < ord(' ') or c > ord('~'):
            return repr(bytes)
    return ''.join(map(lambda c: chr(c), bytes))


def run():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('command', nargs='?', help='which command to run: hash, encrypt or decrypt')
    parser.add_argument('file', default='', nargs='?', help='optional: a file to encrypt, decrypt, or hash')
    args = parser.parse_args()
    print(repr(args))

    if args.command == 'hash':
        print(args.command)
    elif args.command == 'encrypt':
        print(args.command)
    elif args.command == 'decrypt':
        print(args.command)
    elif not args.command:
        parser.print_help()
    else:
        sys.stderr.write("Unknown command {}\n".format(repr(args.command)))


if __name__ == '__main__':
    run()
