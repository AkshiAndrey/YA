import argparse

parser = argparse.ArgumentParser(description='Calculate sum of passed parameters')
parser.add_argument('params', metavar='N', nargs='*', help='integer parameters to sum')

args = parser.parse_args()

if len(args.params) == 0:
    print('NO PARAMS')
elif len(args.params) == 1:
    print('TOO FEW PARAMS')
elif len(args.params) > 2:
    print('TOO MANY PARAMS')
elif isinstance(args.params[0], float) or isinstance(args.params[1], float):
    print(ValueError.__name__)
else:
    try:
        result = sum(map(int, args.params))
        print(result)
    except Exception as e:
        print(e.__class__.__name__)
