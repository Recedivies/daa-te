import datetime
from generator import Generator


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def is_equal(arr, SL, SR):
    for k in range(SL + 1, SR):
        if arr[k] != arr[SL]:
            swap(arr, k, SL)
            return False
    return True


def insert_right(arr, key, SR, right):
    j = SR
    while j <= right and key > arr[j]:
        arr[j - 1] = arr[j]
        j += 1
    arr[j - 1] = key


def insert_left(arr, key, SL, left):
    j = SL
    while j >= left and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key


def bidirectional_conditional_insertion_sort(arr):
    N = len(arr) - 1

    start_time = datetime.datetime.now()
    SL = 1
    SR = N
    while SL < SR:
        swap(arr, SR, (SR + SL) // 2)
        if arr[SL] == arr[SR]:
            if is_equal(arr, SL, SR):
                break

        if arr[SL] > arr[SR]:
            swap(arr, SL, SR)

        if SR - SL >= 100:
            i = SL + 1
            while i * i <= (SR - SL):
                if arr[SR] < arr[i]:
                    swap(arr, SR, i)
                elif arr[SL] > arr[i]:
                    swap(arr, SL, i)
                i += 1
        else:
            i = SL + 1

        LC = arr[SL]
        RC = arr[SR]
        while i < SR:
            key = arr[i]
            if key >= RC:
                arr[i] = arr[SR - 1]
                insert_right(arr, key, SR, N)
                SR -= 1
            elif key <= LC:
                arr[i] = arr[SL + 1]
                insert_left(arr, key, SL, 1)
                SL += 1
                i += 1
            else:
                i += 1

        SL += 1
        SR -= 1

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    execution_time = time_diff.total_seconds() * 1000
    print(f"Execution time: {execution_time:.1f} ms")


if __name__ == "__main__":
    arr = Generator.generate_ukuran_besar_sorted()
    bidirectional_conditional_insertion_sort(arr)
