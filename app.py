def min_max_number(arr):
    arr.sort()
    s = sum(arr)
    min_result = s - arr[0]
    min_max_result = s - arr[len(arr) - 1]
    print(min_result, min_max_result)

love = [1,2,3,4, 5, 800]
min_max_number(love)