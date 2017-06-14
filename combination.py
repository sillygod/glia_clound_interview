class memoize:

    def __init__(self, f):
        self.f = f
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.f(*args)

        return self.cache[args]


@memoize
def combination(n, r):
    # base case
    if n == r:
        return 1
    elif r == 1:
        return n
    else:
        return combination(n-1, r) + combination(n-1, r-1)

# ok.... will maximum recursion exceeded, go to use iter!!


def combination_iter(n, r):

    mTable = [[0 for _ in range(r)] for _ in range(n)]


    for x in range(n):
        for y in range(r):
            if y == 0:
                mTable[x][y] = x + 1
            elif y == x:
                mTable[x][y] = 1
            else:
                if x > y:
                    mTable[x][y] = mTable[x-1][y] + mTable[x-1][y-1]

    return mTable[-1][-1]


if __name__ == '__main__':

    print(combination_iter(5, 2))
    print(combination_iter(5, 1))
    print(combination_iter(990, 33))
