 # định nghĩa 1 list ở mức global
import random
from typing import Any

lst=[]
for i in range(20):
    lst.append(random.randint(1,100))

def print_list():
    print(lst)

 # 1. Write a Python program to sum all the items in a list.
def ex_01_02():
   sum = 0
   product = 1
   for item in lst:
     sum += item
     product  *= item
   print(f"Sum of items:{sum}")
   print(f"Prodcution of item:{product}")
# 2. Write a Python program to multiply all the items in a list.


# 3. Write a Python program to get the largest number from a list.
def ex_03():
    largest =0
    for item in lst:
        if item > largest:
           largest = item
    print(f"The largest number:{largest}")
# 4. Write a Python program to get the smallest number from a list.
def ex_04():
    smallest =lst[0]
    for item in lst:
        if item < smallest:
            smallest = item
    print(f"The smallest number:{smallest}")




if __name__ == '__main__':
    print_list()
    ex_01_02()
    ex_03()


# 5. Write a Python program to count the number of strings from a given list of
# strings. The string length is 2 or more and the first and last characters are the
# same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2