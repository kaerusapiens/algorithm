import hashlib
from typing import Any

class HashTable(object):
    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def hash(self,key) ->int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size #같은글자라면, 해쉬치는 같음

    def add(self, key,value) -> None:
        index = self.hash(key)

        for data in self.table[index]: #重複は上書き
            if data[0] == key:
                data[1] = value
                break
        else: # for문이 끝까지 실행되었지만 break가 호출되지 않았다면, else 블록이 실행
                self.table[index].append([key,value])

    def print(self) -> None:
         for index in range(self.size):
              print(index, end = " ")
              for data in self.table[index]:
                   print('-->', end = " ")
                   print(data, end = " ")
              print()

    def get(self,key) -> Any:
         index = self.hash(key)
         for data in self.table[index]:
              if data[0] == key:
                   return data[1]
         return None


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.add('car','Telsa')
    hash_table.add('car','Audi')
    hash_table.add('pc','MacBook')
    hash_table.add('sns','Youtube')

    hash_table.print()
    print(hash_table.get('car'))