class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.end = 0
        self.count = 0

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, item):
        if self.is_full():
            raise BufferError("Buffer is full")
        self.buffer[self.end] = item
        self.end = (self.end + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise BufferError("Buffer is empty")
        item = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        return item

class CircularBufferWithOverwrite:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.start = 0
        self.end = 0

    def is_full(self):
        return self.start == (self.end + 1) % self.size

    def is_empty(self):
        return self.start == self.end

    def enqueue(self, item):
        self.buffer[self.end] = item
        self.end = (self.end + 1) % self.size
        if self.end == self.start:
            self.start = (self.start + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            raise BufferError("Buffer is empty")
        item = self.buffer[self.start]
        self.buffer[self.start] = None
        self.start = (self.start + 1) % self.size
        return item

# Плюсы и минусы:
# CircularBuffer:
# Плюсы:
# - Простая реализация с ясной семантикой (не перезаписывает данные).
# - Легко понять и использовать.
# Минусы:
# - Неэффективно использует пространство, если буфер часто полон.

# CircularBufferWithOverwrite:
# Плюсы:
# - Эффективное использование пространства, так как данные перезаписываются при заполнении буфера.
# Минусы:
# - Могут быть потеряны данные, если буфер переполнен и новые данные записываются поверх старых.
# - Может быть сложнее понять и использовать правильно.
