def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Почему quicksort:
# - Quicksort имеет среднюю временную сложность O(n log n), что делает его одним из самых быстрых алгоритмов сортировки для общего использования.
# - Он хорошо работает с большими и случайными массивами, часто опережая другие алгоритмы сортировки в реальных сценариях.
# - В худшем случае (отсортированный массив) временная сложность составляет O(n^2), однако выбор случайного опорного элемента может уменьшить вероятность худшего случая.
# - Реализация проста и понятна, а также легко оптимизируется для конкретных сценариев использования.
