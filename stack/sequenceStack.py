class sequenceStack:
    # stack is LIFO 
    def __init__(self):
        self.stack = [None] * 8
        self.size = 0
        self.dur = 8

    def _reSize(self):
        tmp = self.size * 2 * [None] 
        for i, v in enumerate(self.stack):
            tmp[i] = v
        self.dur *= 2
        self.stack = tmp
    
    def __str__(self):
        ans = ""
        def aux(stack, index):
            nonlocal ans
            if(index < 0):
                ans = ans[:-4]
                return
            ans += f"{stack[index]} -> "
            aux(stack, index - 1)
        aux(self.stack, self.size - 1)
        return ans
    
    # size = 0 stack[0]
    # size = 1 stack[1]
    def add(self, val):
        if self.size >= self.dur:
            self._reSize()
        self.stack[self.size] = val
        self.size += 1

    def delete(self):
        assert(self.size > 0), "The stack is None"
        tmp = self.stack[self.size - 1]
        self.size -= 1
        return tmp
    


    