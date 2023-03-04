if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Convert the map object to a list and remove duplicates using set()
    # Then, sort the list in descending order
    arr_sorted = sorted(list(set(arr)), reverse=True)

    # The second highest element is the element at index 1
    print(arr_sorted[1])
