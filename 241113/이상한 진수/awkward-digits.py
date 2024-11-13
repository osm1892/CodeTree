import sys

read = sys.stdin.readline
write = sys.stdout.write


def main():
    a = list(read().strip())
    b = list(read().strip())

    for ai in range(len(a)):
        new_a = a[:]
        if new_a[ai] == "0":
            new_a[ai] = "1"
        else:
            new_a[ai] = "0"
        new_a_value = int("".join(new_a), 2)
        for bi in range(len(b)):
            new_b = b[:]
            for bv in ["0", "1", "2"]:
                if new_b[bi] == bv:
                    continue
                new_b[bi] = bv
                new_b_value = int("".join(new_b), 3)
                if new_a_value == new_b_value:
                    print(new_a_value)
                    return


main()
