# write an algorithm for binary-sort
# write an algorithm to find the sum of array(both normal and recursive)
#write an algorithm for selection, sort, quicksort
# count, and find the max of an array, and double each element in an arrray


# 1     
# Approach 

def binary_sort(array, item):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low  = mid + 1
    return None

my_list = [2, 3, 5, 6, 7, 8, 8, 8, 9, 1, 2, 3, 4,5, 7, 8, 8,9]
print(binary_sort(my_list, 8))

#2
# the normal function
def sum(arr):
    total = 0
    for i in arr:
        total = total + i
    return total

my_list = [2, 3, 5, 6, 7, 8, 8, 8, 9, 1, 2, 3, 4,5, 7, 8, 8,9]
print (sum(my_list))

#2 part b recursive function

def recursive_function(arr):
    # you have to create the base case
    if not arr:
        return 0
    else:
        # create the recursive function
        return arr[0] + recursive_function(arr[1:])
        
    
my_list = [2, 3, 5, 6, 7, 8, 8, 8, 9, 1, 2, 3, 4,5, 7, 8, 8,9]
print (recursive_function(my_list))

# 3 
#selection first
# you need to create a funtion to find the smallest number and highest number 
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# def find_odd_number(arr):
#     odd = arr[0]
#     odd_index = 0
#     for i in range(1, len(arr)):


def find_highest(arr):
    highest = arr[0]
    highest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            highest_index = i
    return highest_index

# you neeed to create the selection sort
def selection_sorts(arr):
    newarr = [[], []]
    while arr:
        smallest = find_smallest(arr)
        highest = find_highest(arr)
        
        if smallest < highest:
            newarr[0].append(arr.pop(smallest))
            newarr[1].append(arr.pop(highest - 1))
        else:
            newarr[1].append(arr.pop(highest))
            newarr[0].append(arr.pop(smallest -1))
    return newarr

my_list = [2, 3, 5, 6, 7, 8, 8, 8, 9, 1, 2, 3, 4,5, 7, 8, 8,9]
print (selection_sorts(my_list))

def sort_ascending_and_descending(arr):
    ascending = sorted(arr)  # Sort in ascending order
    descending = sorted(arr, reverse=True)  # Sort in descending order
    return ascending, descending

# Example usage
my_list = [2, 3, 5, 6, 7, 8, 8, 8, 9, 1, 2, 3, 4, 5, 7, 8, 8, 9]
ascending_list, descending_list = sort_ascending_and_descending(my_list)
print("Ascending order:", ascending_list)
print("Descending order:", descending_list)


def binary_sort_occurence(list, item):

    def find_first(list, item):
        low = 0
        high = len(list) - 1
        while low < high:
            mid = (low + high) // 2
            guess = list[mid]
            if guess == item:
            # check if it's the first occurence
                if mid == 0 or list[mid - 1] != item:
                    return mid
                high = mid - 1
            elif guess < item:
                low = mid + 1
            else:
                high = mid - 1
        return -1 



    def find_last(list, item):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]
            if guess == item:
                if mid == len(list) -1 or list[mid + 1]  != item:
                    return mid 
                low = mid + 1
            elif guess < item:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    

    first = find_first(list, item)
    last = find_last(list, item)
    
    return[first, last] if first != -1 else[-1, -1 ]


my_list = [1, 2, 2, 3, 3, 3, 4] 
print(binary_sort_occurence(my_list, 3))


def binary_sort_occurences(list, item):

    def find_first(list, item):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]
            if guess == item:
                if mid == 0 or list[mid -1 ] != item:
                    return mid
                high = mid - 1
            elif guess < item:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    def find_last(list, item):
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]
            if guess == item:
                if mid == len(list) -1 or list[mid + 1] != item:
                    return mid
                low = mid + 1
            elif guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    


    first = (find_first(list, item))
    last = (find_last(list, item))

    return [first, last] if first != 1 else[-1, -1]

my_list = [1, 2, 2, 3, 3, 3, 4] 
print(binary_sort_occurences(my_list, 3))

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)
my_list = [2, 3, 5, 6, 7, 8, 8, 8, 9, 1, 2, 3, 4, 5, 7, 8, 8, 9]
print(quicksort(my_list))

