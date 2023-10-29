## Tugas Eksperimen 1 - Desain dan Analisis Algoritma (DAA)

### Cara menjalankan program

- Untuk menjalankan algoritma baru `Bidirectional-Conditional-Insertion-Sort`

```shell
python bidirectional_conditional_insertion_sort.py
```

- Untuk menjalankan algoritma `Counting Sort`

```shell
python counting_sort.py
```

- Secara _default_, dataset yang digunakan adalah dataset dengan **ukuran besar** dan statusnya adalah _sorted_. Untuk mengubah dataset yang digunakan dapat diubah pada:

```python
arr = Generator.generate_ukuran_besar_sorted()
```

Dataset yang dipilih melalui kelas `Generator` yang terdapat di file `generator.py`, dapat dipilih kombinasi 9 method untuk _generate dataset_ yang ada.
