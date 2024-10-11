
class LinkList():
    # no sentinel
    # location start at 0 index
    class Node:
        def __init__(self, val, next):
            self.val = val
            self.next = next
    
    def __init__(self, val : str, next):
        self.sentinel = self.Node(0, self.Node(val, None))
        self._size = 1
        
    def isNone(self):
        return self._size == 0
    
    def addList(self, val : str):
        self.sentinel.next = self.Node(val, self.sentinel.next)
        self._size += 1
    
    def addListInend(self, val):
        def aux(linklist):
            if linklist.next is None:
                linklist.next = self.Node(val, None)
                return
            aux(linklist.next)
        aux(self.sentinel)
        self._size += 1

    def delList(self, location : int):
        assert(self._size > 0 and location >= 0), 'Invalid size'
        def aux(linklist, location):
            assert(linklist is not None), 'Invalid size'
            if location == 0:
                return linklist.next
            linklist.next = aux(linklist.next, location - 1)
            return linklist
        self.sentinel.next = aux(self.sentinel.next, location)
        self._size -= 1
        
    def length(self) -> int :
        def aux(linklist):
            if linklist is None:
                return 0
            return 1 + aux(linklist.next)
        return aux(self.sentinel.next)

    #search linklist and return the smallest location
    def search(self, val : str):
        def aux(linklist):
            assert(linklist is not None), 'Invalid size'
            if linklist.val == val:
                return 0
            return 1 + aux(linklist.next)
        return aux(self.sentinel.next)
    
    def __str__(self):
        ans = ""
        def aux(linklist):
            nonlocal ans
            if linklist is None:
                ans += f'{None}'
                return ans
            ans += (f"{linklist.val} -> ")
            aux(linklist.next)
        aux(self.sentinel.next)
        return ans
        




        
