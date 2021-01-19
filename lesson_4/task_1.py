import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('time', type=float)
parser.add_argument('rate', type=float)

args = parser.parse_args(sys.argv[1:])

print(f'Итоговая зарплата = {args.time * args.rate:.2f}')
