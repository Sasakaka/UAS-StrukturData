def merge_sort_descending(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    kanan = arr[:mid]
    kiri = arr[mid:]

    left = merge_sort_descending(kiri)
    right = merge_sort_descending(kanan)

    return merge_descending(left, right)


def merge_descending(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Main program
n = int(input("Masukkan jumlah elemen: "))
arr = []

for i in range(n):
    num = int(input("Masukkan elemen ke-{}: ".format(i + 1)))
    arr.append(num)

sorted_arr = merge_sort_descending(arr)

print("Hasil pengurutan descending: ")
for num in sorted_arr:
    print(num, end=" ")
