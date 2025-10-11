from typing import Dict


class TuDienCuaToi:
    myDict : Dict[str, str]
    def __init__(self):
        self.myDict = dict()
    def ThemTuMoi(self, word : str, tu:str):
        self.myDict[word] = tu
    def TimTuVung(self, word : str):
        return self.myDict[word] if self.myDict.__contains__(word) else "Not found"
    def XoaTuVung(self, word: str):
        self.myDict.__delitem__(word) if self.myDict.__contains__(word) else print("Not found")
# c = input('Nhap chuc nang muon dung')
print('='*20)
print('Tu dien Anh - Viet')
print('-'*20)
myDict = TuDienCuaToi()
myDict.ThemTuMoi("Hello", "Tam Biet")
print(myDict.TimTuVung("Hello"))
myDict.XoaTuVung("Hello")
print(myDict.TimTuVung("Hello"))
