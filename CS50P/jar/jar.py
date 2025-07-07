class Jar:
    def __init__(self, capacity=12):
        if  capacity < 1:
            raise ValueError("Capacity is invalid")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("There is not enough capacity")
        else:
            self._size = self._size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("There aren't enough cookies")
        else:
            self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0 or self.size > self._capacity:
            raise ValueError("Size invalid")
        self._size = size

def main():
    jar = Jar()

if __name__ == "__main__":
    main()
