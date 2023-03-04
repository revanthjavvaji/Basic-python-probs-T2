if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        command, *line = input().split()
        values = list(map(int, line))
        if command == "insert":
            l.insert(values[0], values[1])
        elif command == "print":
            print(l)
        elif command == "remove":
            l.remove(values[0])
        elif command == "append":
            l.append(values[0])
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop()
        elif command == "reverse":
            l.reverse()
