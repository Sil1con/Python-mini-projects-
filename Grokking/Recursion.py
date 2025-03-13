arr_num = [2, 3, 7, 8, 10]

max_num = 0


def sum_arr(arr, total):
    if len(arr) != 0:
        global max_num

        if arr[0] > max_num:
            max_num = arr[0]

        total += arr[0]
        arr.pop(0)
        sum_arr(arr, total)
    else:
        print("The base case: the array is empty")
        print(f"Total: {total}")
        print(f"The biggest number: {max_num}")
        return 0


#Task 4.8
def multiply_arr(arr):
    for multiplier in arr:
        arr2 = []
        for num in arr:
            num *= multiplier
            arr2.append(num)
        print(arr2)


multiply_arr(arr_num)
