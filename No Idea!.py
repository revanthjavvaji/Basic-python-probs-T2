# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
a = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0
for x in a:
    if x in A:
        happiness += 1
    elif x in B:
        happiness -= 1

print(happiness)
