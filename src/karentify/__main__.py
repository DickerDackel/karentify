import sys
import argparse

from karentify import karentify


def main():
    cmdline = argparse.ArgumentParser(description='Unleash your inner Karen on `s`')
    cmdline.add_argument('--demand-manager', '-D', action='store_true',
                         help='Demand to speak to somebody with actual authority')
    cmdline.add_argument('message', type=str, nargs='*', help='Your important message')
    opts = cmdline.parse_args(sys.argv[1:])

    if len(opts.message) > 1:
        s = ' '.join(opts.message)
    else:
        s = input('> ')

    print(karentify(s) + '!!!')
    if opts.demand_manager:
        print(karentify('and I would like to talk to your manager') + '!!!')


if __name__ == "__main__":
    main()
