def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i):  # 이미 정렬된 부분은 건너뜀
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

nums = [5, 3, 1, 4, 2]
bubble_sort(nums)
print(nums)  # [1, 2, 3, 4, 5]