def anonymous(x):
    return x**2 + 1


def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0

    while intercept < end:
        intercept += step

        # caculate the small rectangle?
        dA = 0.1 * (anonymous(intercept-step) + anonymous(intercept))/2
        area += dA

    return area


if __name__ == '__main__':

    print(integrate(anonymous, 0 , 10))
