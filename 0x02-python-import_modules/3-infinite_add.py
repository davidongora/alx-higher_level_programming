#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    total = 0
    total += sum(int(sys.argv[i]) for i in range(1, len(sys.argv)))
    print("{}".format(total))
