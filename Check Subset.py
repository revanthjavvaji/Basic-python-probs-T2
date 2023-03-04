# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    n = int(input())
    set_a = set(input().split())
    m = int(input())
    set_b = set(input().split())
    
    if set_a.issubset(set_b):
        print(True)
    else:
        print(False)
