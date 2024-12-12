# binary sorts algorithm
# def binary_sort(list, item):
#     low = 0
#     high = len(list) - 1
#     while low <= high:
#         mid = (low + high)
#         guess = list[mid]
#     if guess == item:
#         return mid
#     if guess > item:
#         high = mid - 1
#     else:
#         low = mid + 1
#     return None 
# my_list = [1, 2, 3, 4, 5, 6]

# print (binary_sort(my_list, 5))

# Selection sorts algorithm
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

print(selectionSort([4, 8, 3, 9 , 1, 4]))


# create a function to sum up an array

def sum(arr):
    total = 0
    for i in arr:
        total += i
    return 



# recirsive function to calculate sum of an array

def recursive_funnction(arr):
    # base case it shour return 0 id the arrray is empty
    if not arr:
        return 0
    # recurive case add thr first elememt + the rest of the sumed array

    return arr[0] + recursive_funnction(arr[1:])

# recursive function to count the array
def count_array(arr):
     # base case it shour return 0 id the arrray is empty
    if not arr:
        return 0
    # recursive function
    
    return 1 + count_array(arr[1:])

def find_max(arr):
    #base case 
    if len(list) == 1:
        return arr[0]
    # recursive case
    return max(arr[0], find_max[1:])

# quick sort 
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)



def double_list(arr):
    if not arr:
        return [] # return an empty list if the array is empty
    
    doubled = [] # it should store the doubled elememts 
    for i in arr:
            doubled.append(i * 2)
    return doubled

def multiplocation_table(array):
    if not array:
        return []
    multiplied = []
    
    for i in array:
        multiplied.append(i * 2)

    return multiplied
    
my_list = [3, 2, 7]
print(multiplocation_table(my_list))
# def print_items(array):
#     for i in array:
#         print(i)

# def multiplication_table(n):
#     table = []

#     for i in range(1, n + 1):
#         row = []
#         for j in range(1, n+ 1):
#             row.append(i*j)
#         table.append(row)
#     return table

# for row in multiplication_table(5):
#     print(row)



def double(arr):
    for i in range(len(arr)):
        arr[i] *= 2
    return arr
my_list = [3, 2, 7]
print (double(my_list))


def multii(arr):
    table = [] 
    for i in arr:
        row = [i * num for num in arr ]
        table.append(row)
    return table

result = multii([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
for row in result:
    print(row)








