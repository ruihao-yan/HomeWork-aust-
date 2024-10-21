import unittest

def matchBrack(ned : str):
    if ned is None:
        return True
    if len(ned) % 2  != 0:
        return False
    aux = []
    dic = {")" : "(", "}" : "{", "]" : "[", ">" : "<"}
    for i in ned:
        if i not in dic:
            aux.append(i)
        else:
            if(aux.pop() != dic[i]):
                return False
            else:
                continue
    return True
    