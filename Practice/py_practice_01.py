"""
Author: Kha
Date: 10-06-2025
Day 1
"""
import random
from collections import defaultdict
from typing import DefaultDict
def cacul(x):
    # 2x^4 + 3x^3 + 4x^2 + 5x + 7
    return ((((2*x +3)*x + 4)*x+5)*x +7)
def manhatan(x : tuple, y : tuple):
    return sum(abs(a - b) for a, b in zip(x,y))
def find_pair(s : str):
    text = s.split()
    pair = []
    for i in range(len(text) -1):
        if (text[i],text[i+1]) not in pair:
            pair.append((text[i], text[i+1]))
    return pair
def sparse_vector(vector1, vector2):
    return sum([v1*v2 for v1, v2 in zip(vector1, vector2)])
def dot_product(v1 : defaultdict, v2 : defaultdict):
    return sum(v1[i]*v2[i] for i in v1 if i in v2)

if __name__ == '__main__':
#    text = input('Give me text: ')
    text = "Toi Di Hoc"
    # min_char = "" if len(text.split()) == 0 else sorted(text.split())[0]
    # print(min_char)
    print(sorted(text.lower().split(" "))[0])
    print(cacul(6))
    """
        INPUT: con cho va con meo
    """
    print(manhatan((1,2),(3,4)))
    text = "con cho va con meo"

    print(find_pair(text))
    input = text.split()
    for i in range(20):
        text = ''
        tmp_set = {0, 1, 2, 3, 4}
        while True:
            if len(tmp_set) == 0: break
            rndInt = random.randint(0,4)
            if rndInt in tmp_set:
                tmp_set.discard(rndInt)
                text += input[rndInt] + " "
        print(f"{i}: {text}\n")
    # Dot product
    v1 = defaultdict(int)
    v2 = defaultdict(int)
    data = {'a':1,'b':3,'c':4}
    data2 =  {'b':5,'d':1}
    v1.update(data)
    v2.update(data2)
    print(dot_product(v1,v2))
