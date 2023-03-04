# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
num_ops = int(input())

for i in range(num_ops):
    op, len_s = input().split()
    other_set = set(map(int, input().split()))
    
    if op == 'intersection_update':
        s.intersection_update(other_set)
    elif op == 'update':
        s.update(other_set)
    elif op == 'symmetric_difference_update':
        s.symmetric_difference_update(other_set)
    elif op == 'difference_update':
        s.difference_update(other_set)
        
print(sum(s))
