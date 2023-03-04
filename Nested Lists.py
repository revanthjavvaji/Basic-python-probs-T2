if __name__ == '__main__':
    # read input and create nested list of students
    n = int(input())
    students = [[input(), float(input())] for _ in range(n)]

    # find second lowest grade
    second_lowest = sorted(set([s[1] for s in students]))[1]

    # find all students with second lowest grade
    names = [s[0] for s in students if s[1] == second_lowest]

    # sort names alphabetically and print one by one
    for name in sorted(names):
        print(name)
