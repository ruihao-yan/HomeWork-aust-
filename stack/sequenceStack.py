class sequenceStack:
    # stack is LIFO 
    def __init__(self):
        self.stack = [None] * 8
        self.size = 0

    def _reSize(self):
        tmp = self.size * 2 * [None] 
        for i, v in enumerate(self.stack):
            tmp[i] = v 
    
    def __str__(self):
        ans = ""
        def aux(stack, index):
            nonlocal ans
            if(index >= self.size):
                ans += "None"
                return ans
            ans += f"{stack[index]} -> "
        return aux(self.stack, 0)
    
    # size = 0 stack[0]
    # size = 1 stack[1]
    def add(self, val):
        self.stack[self.size] = val
        self.size += 1

    def delete(self):
        tmp = self.delete(len(self.stack)) 
        self.size -= 1
        return tmp
    


    