# find the smallest the in array

def find_smalllest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newarr =  []
    for i in range(len(arr)):
        smallest = find_smalllest(arr)
        newarr.append(arr.pop(smallest))
    return newarr


my_list = [2, 1, 5, 4, 3, 7, 9]
sorted_list = selection_sort(my_list)
print(sorted_list)

#find the sum of a certain array
def sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

my_list = [2, 1, 5, 4, 3, 7, 9]

print(sum(my_list))

#recursive function for sum

def recursive_function(arr):
    if not arr:
        return 0
    for i in arr:
        return arr[0] + recursive_function(arr[1:])

my_list = [2, 1, 5, 4, 3, 7, 9]

print(recursive_function(my_list))

def fact(i):
    if i == 1:
        return 1
    else:
        return i *fact(i-1)

print(fact(4))



def count_array(arr):
    if not arr:
        return 0
    for i in arr:
        return 1 + count_array(arr[1:])
    
my_list = [2, 1, 5, 4, 3, 7, 9]
print(count_array(my_list))

def max_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], max_array(arr[1:]))
    
my_list = [2, 1, 5, 4, 3, 7, 9]
print(max_array(my_list))



def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]

        greater  = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    
my_list = [2, 1, 5, 4, 3, 7, 9]
print(quicksort(my_list))



def binary(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

