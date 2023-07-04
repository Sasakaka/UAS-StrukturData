def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main program
n = int(input("Masukkan jumlah elemen: "))
arr = []

for i in range(n):
    num = int(input("Masukkan elemen ke-{}: ".format(i + 1)))
    arr.append(num)

target = int(input("Masukkan data yang ingin dicari: "))

arr.sort() 

result = binary_search(arr, target)

if result != -1:
    print("Data ditemukan pada indeks:", result)
else:
    print("Data tidak ditemukan dalam array.")