# Get the size of each group
k = int(input())

# Get the list of room numbers
rooms = list(map(int, input().split()))

# Initialize a dictionary to keep track of the frequency of each room number
freq = {}

# Count the frequency of each room number
for room in rooms:
    if room in freq:
        freq[room] += 1
    else:
        freq[room] = 1

# Find the Captain's room number
for room, count in freq.items():
    if count == 1:
        print(room)
        break
