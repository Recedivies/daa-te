import datetime
from generator import Generator

K = 100_000


def counting_sort(arr):
    start_time = datetime.datetime.now()
    counter = [0] * (K + 1)
    N = len(arr)

    for i in range(N):
        counter[arr[i]] += 1

    sorted_arr = [0] * N
    k = 0
    for i in range(1, K + 1):
        for j in range(counter[i]):
            sorted_arr[k] = i
            k += 1

    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    execution_time = time_diff.total_seconds() * 1000
    print(f"Execution time: {execution_time:.1f} ms")


if __name__ == "__main__":
    arr = Generator.generate_ukuran_besar_sorted()
    counting_sort(arr)
