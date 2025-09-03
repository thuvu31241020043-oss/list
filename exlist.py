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
# 2. Write a Python program to multiply all the items in a list.
   print(f"Prodcution of item:{product}")

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
# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
def ex_05():
    str=['abc','fg','tobit','vlmtv']
    count=0
    for st in str:
        if len(st)<2:
            continue
        if st[0]==st[-1]:
            count+=1
    print(f"Number of item with the first and last characters are the same:{count}")

if __name__ == '__main__':
    print_list()
    ex_01_02()
    ex_03()
    ex_04()
    ex_05()

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
result = sort_by_last_element(sample_list)
print("Sorted list:", result)


# 7. Write a Python program to remove duplicates from a list.
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("List sau khi xóa trùng lặp:", unique_list)
# 8. Write a Python program to check if a list is empty or not.
def check_empty(my_list):
    if not my_list:
        print("The list is empty")
    else:
        print("The list is not empty")
list1 = []
list2 = [1, 2, 3]
check_empty(list1)
check_empty(list2)
# 9. Write a Python program to clone or copy a list.
my_list = [1, 2, 3, 4, 5]
copied_list = my_list.copy()
print(f"Original List:{my_list}")
print(f"Copy list:{copied_list}")
# 10. Write a Python program to find the list of words that are longer than n from a given list of words.
def long_words(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result
word_list = ["apple", "banana", "pear", "kiwi", "strawberry"]
print("Words longer than 4:", long_words(word_list, 4))
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
print(have_common_member([1, 2, 3], [4, 5, 6]))
print(have_common_member([1, 2, 3], [3, 5, 6]))
# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(5)
color.pop(4)
color.pop(0)
print(color)

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
array_3d = []
for i in range(3):
    block = []
    for j in range(4):
        row = []
        for k in range(6):
            row.append('*')
        block.append(row)
    array_3d.append(block)
print(array_3d)
# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
numbers=[1,2,3,4,5,6,7,8,9]
result = []
for n in numbers:
    if n % 2 != 0:
        result.append(n)
print(result)
# 15. Write a Python program to shuffle and print a specified list.
def shuffle_list(my_list):
    random.shuffle(my_list)
    return my_list
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(f"Original list:{colors}")
print(f"Shuffled list:{shuffle_list(colors)}")
# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).
def square_list():
    squares = [i**2 for i in range(1, 31)]
    return squares[:5] + squares[-5:]
print(square_list())
# 17. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def all_primes(numbers):
    for num in numbers:
        if not is_prime(num):
            return False
    return True
print(all_primes([0, 3, 4, 7, 9]))
print(all_primes([3, 5, 7, 13]))
print(all_primes([1, 5, 3]))
# 18. Write a Python program to generate all permutations of a list in Python.
import itertools
def all_permutations(lst):
    return list(itertools.permutations(lst))
print(all_permutations([1, 2, 3]))
# 19. Write a Python program to calculate the difference between the two lists.
def list_difference(list1, list2):
    return list(set(list1) - set(list2))
print(list_difference([1, 2, 3, 4], [2, 4]))
# 20. Write a Python program to access the index of a list.
def print_with_index(lst):
    for index, value in enumerate(lst):
        print(f"Index: {index}, Value: {value}")
print_with_index(['Red', 'Green', 'Blue'])
# 21. Write a Python program to convert a list of characters into a string.
def chars_to_string(char_list):
    return ''.join(char_list)
print(chars_to_string(['P', 'y', 't', 'h', 'o', 'n']))
# 22. Write a Python program to find the index of an item in a specified list.
def find_index(lst, item):
    return lst.index(item)
colors = ['red', 'green', 'blue']
print(find_index(colors, 'green'))
# 23. Write a Python program to flatten a shallow list.
def flatten_list(lst):
    return [item for sublist in lst for item in sublist]
print(flatten_list([[1, 2], [3, 4], [5, 6]]))
# 24. Write a Python program to append a list to the second list.
def append_list(list1, list2):
    list1.extend(list2)
    return list1
print(append_list([1, 2, 3], [4, 5, 6]))
# 25. Write a Python program to select an item randomly from a list.
def random_choice(lst):
    return random.choice(lst)
print(random_choice([10, 20, 30, 40, 50]))
# 26. Write a Python program to check whether two lists are circularly identical.
def circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False
    return ''.join(map(str, list2)) in ''.join(map(str, list1 * 2))
print(circularly_identical([1, 2, 3, 4], [3, 4, 1, 2]))  # True
print(circularly_identical([1, 2, 3], [2, 3, 4]))
# 27. Write a Python program to find the second smallest number in a list.
def second_smallest(numbers):
    unique_nums = sorted(set(numbers))
    return unique_nums[1]
print(second_smallest([1, 2, 3, 4, 5]))
# 28. Write a Python program to find the second largest number in a list.
def second_largest(numbers):
    unique_nums = sorted(set(numbers))
    return unique_nums[-2]
print(second_largest([1, 2, 3, 4, 5]))
# 29. Write a Python program to get unique values from a list.
def unique_values(lst):
    return list(set(lst))
print(unique_values([1, 2, 2, 3, 4, 4, 5]))
# 30. Write a Python program to get the frequency of elements in a list
from collections import Counter
def frequency(lst):
    return dict(Counter(lst))
print(frequency(['apple', 'banana', 'apple', 'orange', 'banana', 'apple']))
# 31. Write a Python program to count the number of elements in a list within a specified range.
def count_in_range(lst, low, high):
    count = 0
    for num in lst:
        if low <= num <= high:
            count += 1
    return count
numbers = [10, 20, 30, 40, 50, 60, 70]
print(count_in_range(numbers, 25, 55))
# 32. Write a Python program to check whether a list contains a sublist.
def is_sublist(main_list, sub_list):
    n, m = len(main_list), len(sub_list)
    for i in range(n - m + 1):
        if main_list[i:i+m] == sub_list:
            return True
    return False
print(is_sublist([1, 2, 3, 4, 5], [2, 3]))
print(is_sublist([1, 2, 3, 4, 5], [3, 5]))
# 33. Write a Python program to generate all sublists of a list.
def all_sublists(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            sublists.append(lst[i:j])
    return sublists
print(all_sublists([1, 2, 3]))
# 34. Write a Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0], primes[1] = False, False
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return [i for i, prime in enumerate(primes) if prime]
print(sieve_of_eratosthenes(30))
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.
# 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
def concatenate_list(lst, n):
    result = []
    for i in range(1, n+1):
        for item in lst:
            result.append(f"{item}{i}")
    return result
print(concatenate_list(['p', 'q'], 5))
# 36. Write a Python program to get a variable with an identification number or string.
x = 100
y = "Python"
print("ID of x:", id(x))
print("ID of y:", id(y))
# 37. Write a Python program to find common items in two lists.
def common_items(list1, list2):
    return list(set(list1) & set(list2))
print(common_items([1, 2, 3, 4], [3, 4, 5, 6]))
# 38. Write a Python program to change the position of every n-th value to the (n+1)th in a list.
def swap_adjacent(lst):
    result = lst[:]
    for i in range(0, len(lst)-1, 2):
        result[i], result[i+1] = result[i+1], result[i]
    return result
print(swap_adjacent([0,1,2,3,4,5]))
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
def list_to_integer(lst):
    return int("".join(map(str, lst)))
print(list_to_integer([11, 33, 50]))
# 40. Write a Python program to split a list based on the first character of a word.
from collections import defaultdict
def split_by_first_char(words):
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(groups)
words = ["apple", "banana", "apricot", "cherry", "blueberry", "avocado"]
print(split_by_first_char(words))
# 41. Write a Python program to create multiple lists.
list1, list2, list3 = ([] for i in range(3))
print(list1, list2, list3)
# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']
missing = set(list1) - set(list2)
additional = set(list2) - set(list1)
print("Missing values in second list:", ", ".join(missing))
print("Additional values in second list:", ", ".join(additional))
# 43. Write a Python program to split a list into different variables.
colors = ["Red", "Green", "Blue"]
c1, c2, c3 = colors
print(c1)
print(c2)
print(c3)
# 44. Write a Python program to generate groups of five consecutive numbers in a list.
nums = [i for i in range(1, 21)]  # 1 → 20
result = [nums[i:i+5] for i in range(0, len(nums), 5)]
print(result)
# 45. Write a Python program to convert a pair of values into a sorted unique array.
pair = [(1, 2), (3, 4), (1, 2), (2, 3)]
result = sorted(set(sum(pair, ())))
print(result)
# 46. Write a Python program to select the odd items from a list.
lst = [10, 11, 12, 13, 14, 15]
odds = [x for x in lst if x % 2 != 0]
print(odds)
# 47. Write a Python program to insert an element before each element of a list.
lst = [1, 2, 3]
new_lst = []
for item in lst:
    new_lst.append("X")
    new_lst.append(item)
print(new_lst)
# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
nested = [[1, 2], [3, 4], [5, 6]]
for l in nested:
    print(l)
# 49. Write a Python program to convert a list to a list of dictionaries.
lst = ["a", "b", "c", "d"]
dicts = [{i: i} for i in lst]
print(dicts)
# 50. Write a Python program to sort a list of nested dictionaries.
my_list = [
    {"name": "John", "age": 25},
    {"name": "Emma", "age": 30},
    {"name": "Mike", "age": 20},
    {"name": "Sophia", "age": 28}
]
sorted_list = sorted(my_list, key=lambda x: x["age"])
print("Sorted by age:")
for item in sorted_list:
    print(item)
sorted_list_by_name = sorted(my_list, key=lambda x: x["name"])
print("\nSorted by name:")
for item in sorted_list_by_name:
    print(item)