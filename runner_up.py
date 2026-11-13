"""Print the second-highest distinct score from standard input."""

import sys


def main():
    # The judge guarantees n valid scores and at least two distinct values.
    count, *scores = map(int, sys.stdin.read().split())
    distinct = sorted(set(scores[:count]), reverse=True)
    print(distinct[1])


if __name__ == "__main__":
    main()
