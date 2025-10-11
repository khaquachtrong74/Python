from typing import Dict
# n = int(input("Enter n:= "))
# for i in range(n):
#     print(' '*(n-i-1)+'*'*(i+1))
# for i in range(n):
#     # s = ''
#     # for j in range(n):
#     #     s += "*"
#     # print(s)
#     # print(s[:(5+i)%5])
#     print(' '*(n-i-1)+'*'*(i+1))
#     print('*'*(i+1))
#     print()
# for k in range(0, n, 2):
#     print(('*'*(k+1)).center(n))

# Bài 2
times = int(input('Enter your n integer'))
a = list()
for j in range(times):
    a.append(int(input(f'Enter your {j} number =')))
print(f'Số dương lớn nhất{max(a) if (max(a) > 0) else ' *' }')
print(f'Số dương nhỏ nhất{min(a) if (min(a) < 0) else ' *'}')
# mydic :Dict[int, int] = dict()
# for el in a:
#     mydic[el]+=1
# for key, val in mydic:
#     print(f'Key : {key} = Val : {val}')

for el in set(a):
    print(f'{el} xuat hien {a.count(el)} lan')
tmp = int(input('Nhap k lan muon xuat so phan tu'))

print([el for el in set(a) if a.count(el) == tmp])
print(sorted(a, reverse=True))
