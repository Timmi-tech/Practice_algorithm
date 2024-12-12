def binary_sorts(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
        return None

my_list = [2,2,3,5,6]
print(binary_sorts(my_list, 5))


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr



my_list = [2, 1, 4, 5, 3, 7]
sorted_list = selectionSort(my_list)
print(sorted_list)

def findHighest(arr):
    highest = arr[0]
    highest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            highest_index = i
    return highest_index

def selectionsort(arr):
    newarr = []
    for i in range(len(arr)):
        highest = findHighest(arr)
        newarr.append(arr.pop(highest))
    return newarr

my_list = [2, 1, 4, 5, 3, 7]
sorted_list = selectionsort(my_list)
print(sorted_list)


def countdown(i):
    if i <= 0:
        return
    print(i)
    countdown(i-1)
  

countdown(5)

def greet(name):
    print("hello how are you " + " " + name)

greet("tomiwa")

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
fact(4)

def reverse_words_preserve_spaces(s):
    # Split the string by spaces, reverse each word, and join them back with spaces
    words = s.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

#Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Example usage
input_string = "hello world this is a test"
output_string = reverse_words_preserve_spaces(input_string)
print(output_string)  # Output: "olleh dlrow siht si a tset"

# Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
# He tells them that he will only sit for the session if they show the same motif at most N times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the order?

# Task
# Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
# For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, the result would be [20,37,21].

def limit_occurrences(lst, N):
    result = []
    counts = {}
    
    for item in lst:
        # Check if the item has been added less than N times
        if counts.get(item, 0) < N:
            result.append(item)
            counts[item] = counts.get(item, 0) + 1
    
    return result

# Example usage
print(limit_occurrences([1, 2, 3, 1, 2, 1, 2, 3], 2))  # Output: [1, 2, 3, 1, 2, 3]
print(limit_occurrences([20, 37, 20, 21], 1))         # Output: [20, 37, 21]

# for finding the sum of arr
def sum(arr):
    total = 0
    for i in arr:
        total =+ i
    return total

# using recursive function

def recursive_function(arr):
    # Base case if the list is empty return 0
    if not arr:
        return 0
    
# recursive case is the first elememt in the arrry + sum of the remaining list
    return arr[0] + recursive_function(arr[1:])


