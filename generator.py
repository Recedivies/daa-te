import random

K = 100_000


class Generator:
    @classmethod
    def generate_ukuran_kecil_sorted(cls):
        arr = cls._ukuran_kecil()
        arr.sort()
        return arr

    @classmethod
    def generate_ukuran_kecil_random(cls):
        arr = cls._ukuran_kecil()
        return arr

    @classmethod
    def generate_ukuran_kecil_reversed(cls):
        arr = cls._ukuran_kecil()
        arr.sort(reverse=True)
        return arr

    @classmethod
    def generate_ukuran_sedang_sorted(cls):
        arr = cls._ukuran_sedang()
        arr.sort()
        return arr

    @classmethod
    def generate_ukuran_sedang_random(cls):
        arr = cls._ukuran_sedang()
        return arr

    @classmethod
    def generate_ukuran_sedang_reversed(cls):
        arr = cls._ukuran_sedang()
        arr.sort(reverse=True)
        return arr

    @classmethod
    def generate_ukuran_besar_sorted(cls):
        arr = cls._ukuran_besar()
        arr.sort()
        return arr

    @classmethod
    def generate_ukuran_besar_random(cls):
        arr = cls._ukuran_besar()
        return arr

    @classmethod
    def generate_ukuran_besar_reversed(cls):
        arr = cls._ukuran_besar()
        arr.sort(reverse=True)
        return arr

    @classmethod
    def _random_int(cls, lower, upper):
        return random.randint(lower, upper)

    @classmethod
    def _generate_dataset(cls, N):
        arr = [0] * (N + 1)
        for i in range(1, N + 1):
            arr[i] = cls._random_int(1, K)
        return arr

    @classmethod
    def _ukuran_kecil(cls):
        N = 500
        arr = cls._generate_dataset(N)
        return arr

    @classmethod
    def _ukuran_sedang(cls):
        N = 5_000
        arr = cls._generate_dataset(N)
        return arr

    @classmethod
    def _ukuran_besar(cls):
        N = 50_000
        arr = cls._generate_dataset(N)
        return arr
