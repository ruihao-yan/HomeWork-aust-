class MinHeap:
    def __init__(self):
        self.array = [None] * 1
        self._size = 0

    def _reSize(self):
        tmp = [None] * len(self.array) * 2
        for i in range(len(self.array)):
            tmp[i] = self.array[i]
        self.array = tmp

    # [None, 1, 2, 3] index : [0, 1, 2, 3]
    # self.array[1] = 1 size = 1
    # self.array[2] = 2 size = 2
    # self.size = 3 self.array[3] = 3
    def add(self, val):
        self._size += 1
        if self._size == len(self.array):
            self._reSize()
        self.array[self._size] = val
        self._swimUp(self._size)

    def offer(self):
        tmp = self.array[1]
        if self._size == 1:
            self._size -= 1
            return tmp
        layer = self._layer(self._size) # 层数
        middle = pow(2, layer) + pow(2, layer) // 2 # 最后一层中间偏右的位置
        if self._size >= middle:
            self.array[1] = self.array[middle]
            self.array[middle] = None
            self._size -= 1
            self._swimDown(1)
            return tmp
        if self.array[self._size] == middle - 1:
            self.array[1] = self.array[middle - 1]
            self.array[middle - 1] = None
            self._size -= 1
            self._swimDown(1)
            return tmp
        else:
            # 上一层中间偏右
            start = pow(2, layer)
            middle = start - pow(2, layer - 2)
            self.array[1] = self.array[middle]
            self.array[middle] = None
            self._size -= 1
            self._swimDown(1)
            return tmp

    def _display(self) -> list[None]:
        return self.array[:self._size + 1]

    def _swimUp(self, index : int) -> None:
        if self.array[index // 2] is None:
            return
        if self.array[index // 2] <= self.array[index]:
                    return
        self.array[index // 2], self.array[index] = self.array[index], self.array[index // 2]
        self._swimUp(index // 2)

    def _layer(self, index : int) -> int:
        def aux(index, need):
            if index <= 1 or index <= need:
                return 0
            return 1 + aux(index - need, need * 2)
        return aux(index, 1)

    def _swimDown(self, index):
        if index * 2 >= len(self.array):
            return
        if type(self.array[index * 2]) == int and self.array[index * 2] <= self.array[index]:
            self.array[index], self.array[index * 2] = self.array[index * 2], self.array[index]
            self._swimDown(index * 2)
        if self.array[index * 2 + 1] is not None and self.array[index * 2 + 1] <= self.array[index]:
            self.array[index], self.array[index * 2 + 1] = self.array[index * 2 + 1], self.array[index]
            self._swimDown(index * 2 + 1)
        else:
            return













