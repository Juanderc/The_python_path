import argparse


def Greetings(args):
    print("{0} {1}".format(args.greeting, args.name.capitalize()))


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


greeting = subparsers.add_parser("say_hi")
greeting.add_argument("name")
greeting.add_argument("--greeting", default="HELLO")
greeting.add_argument("--version", action="version", version="1.0.0")
# greeting.add_argument('--caps', action='store_true')
greeting.set_defaults(func=Greetings)


if __name__ == "__main__":
    args = parser.parse_args()
    args.func(args)
