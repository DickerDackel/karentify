import sys
import argparse

from random import choice
from karentify import karentify


REACTIONS = ['inaudible', 'incomprehensible', 'enraged hairflip',
             'angry fingerpointing', 'attention seeking room scan']


def main(args):
    cmdline = argparse.ArgumentParser(description='Unleash your inner Karen on `s`')
    cmdline.add_argument('--dEmAnD-MaNaGeR', '-D', action='store_true', help='Demand to speak to somebody with actual authority')
    cmdline.add_argument('--AcT-ApPrOpRiAtElY', '-A', action='store_true', help='Make visually clear that this issue is serious')
    cmdline.add_argument('entitlement', type=str, nargs='*', help='Your important message')
    opts = cmdline.parse_args(args)

    def wrangle_demand(s):
        s = s.strip().rstrip('.!?,')

        if len(s):
            demand = karentify(s)
        elif opts.AcT_ApPrOpRiAtElY:
            demand = f'[{choice(REACTIONS)}]'
        else:
            demand = ''

        if s != demand:
            # Yes, I know there could be a line break mid sentence.
            # This is still the correct behaviour.
            return f'{demand}!!!'
        else:
            return s

    if len(opts.entitlement) > 0:
        print(wrangle_demand(' '.join(opts.entitlement)))
    else:
        if sys.stdin.isatty():
            print('Hello, how can I help you?')

        for s in sys.stdin:
            print(wrangle_demand(s))

    if opts.dEmAnD_MaNaGeR:
        print(wrangle_demand('and I would like to talk to your manager'))


def run():
    # if this is not split up, the cli can't be tested by injecting args
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run()
