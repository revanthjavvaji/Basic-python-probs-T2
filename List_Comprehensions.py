if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # generate all possible coordinates of the 3D grid
    coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in           range (z+1)]

    # filter out the coordinates whose sum is equal to n
    result = [c for c in coordinates if sum(c) != n]

    # print the result
    print(result)
