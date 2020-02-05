Binary and Linear

Linear check if value at index = value then go. Down this until you find 

With binary search, the data must be sorted.    
     It must the dataset in half and focuses on the left 
     side repeating the process looking through the information 
     helping lessen the search time via linear search.

Focus becomes the best ways to sort data


Sorting algorithms

Algorithm
    Set of steps to solve a problem

Iterative algorithms
    Repeat one or many steps until a process is done

example…cooking cookies- repeat steps

Insertion sort

Ex. Consider first car a sorted array of length 

Shifting someone until the collection is sorted by 
verifying which item is smaller and/or larger than the 
card that is being compared.

Selection sort

Fist select the smaller ar and move it far left
Comparte everything to the right of what has yet to be 
sorted.  

Ex 4 5 8 9 0 7


Bubble sort
Compare direct neighbors 
34940
Compare every two items and switch cards until the smaller 
moves to the left


Knowing which sorts to use based off scenarios given

x = [ 1,3,4,5,8,9,7]

middle



quick sort
    recursive method
    divde-conquer algorithm
    very efficient for large datasets

Worse case O(n*2)
Average case O(n log n)
Perforamance depends mainly on pivot selection.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.

Recursive sorting

2. Runtime? Space complexity?

a = 0
    for i in range(n):
        for j in range(n, -1, -1):
            a += i + j


3. Runtime? Space completxity?
i = 0
j = 0
k = 0


for i in range(n /2, n):
    j =2
    while j <= n:
        k = k + n/2
        j *= 2

#non-recursive(iterative)
def sum(arr):
    sum = 0
    for num in arr:
        sum += nume
    return sum

pythontutor.com

#recursive(iterative)
def rec_sum(arr):
    #base case
    if len(arr) == 1:
        return arr[0]

    else:
        return arr[0] + rec_sum(arr[1:])

arr = [2, 5, 8, 4, 1, 6]

rec_sum(arr)


Anagrams

def anagram_checker(str1, str2):
    # constraints: strings only, single words, len < 50 chars
    # return: True, False
    # ex. tone, note
    # enot, enot
    
    if str1.sort() == str2.sort():
        return True
    else:
        return False

# a celebrity is a person who i) knows no one but ii) everyone knows 
# given people[], identify the celebrity (one exists)

# iterative solution- Runtime O(n),  Space complexity O(1)
def find_celebrity():
    for i in range(len(people)):
        if len(people[i].known) == 0:
            return i

#recursive solution-  Runtime O(n), Space complexity O(n)
def find_celebrity(people):
    if len(people[0].known) == 0:
        return people[0] 
    else:
        #recursive is worse due to amount of space that would be used
        return rec_find_celebrity(people[1:])   

Fibonacci
# two numbers in the sequence equal the 
#proceeding 

# Recursive solution - Runtime O(2^n)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

bigcheatsheet.com