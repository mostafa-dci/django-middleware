def makeDivision(a, z):
    # check if b NOT 0
    middleware(z)
    return a/z


def middleware(x):
    if x == 0:
        print("Not Possible")
        exit()
    else:
        pass

d = makeDivision(8, 0)
print(d)