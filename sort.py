from book import Book
import time
import csv


def insertion_sort(books):
    # TO-DO: implement insertion sort
    # element at index 0 is sorted list of one book
    #if num is bigger > on the right than left, leave alone
    # loop over elements from index 1..length - 1
    for i in range(1, len(books)):
        #compare element: if num is smaller < on the left
        #compared to the right, swap smaller to the left
        #and we're not at the front
        # create temp element
        j = i
        #while looping through books/ 
        #temp j 
        while j > 0 and books[j].title < books[j-1].title:
            #swap
            temp = books[j]
            books[j] = books[j-1]
            books[j-1] = temp
            j -= 1

    return books


# Version A: Conventional, recursive Quick Sort
def quick_sort( books, low, high ):
    # TO-DO: implement Quick Sort
    #base case
        #list of 1?
        #if list is 1 -> return list
    if len(books) <= 1:
        return books
    #recursive  case
    else:
        #choose pivot(first element)
        pivot = books[0]
        #partition - smaller elements go to left larger to the right
        lhs = [b for b in books[1:] if b <= pivot]
        rhs = [b for b in books[1:] if b > pivot]
        # quick_sort(LftHndSde) + [pivot] + quick_sort[]
        return quick_sort(lhs) + [pivot] + quick_sort(rhs)
    # return books


# Version B:
# NOT done in place because for large inputs, we
# exceed Python's maximum recursion depth with 
# in-place Quick Sort
def quick_sort_B( books ):
    # STRETCH: implement Quick Sort for larger datasets

    return books


def book_sort(books):
    # STRETCH: combine Insertion & Quick Sort for
    # an improved sorting algorithm
    
    return books

# Read in book data from CSV file
# provided by https://github.com/uchidalab/book-dataset
with open('book_data.csv', encoding='utf8') as csvfile:
    my_books_long = []
    data = csv.DictReader(csvfile)
    for book in data:
        #print(book['title'], book['author'], book['genre'])
        my_books_long.append(Book(book['title'], book['author'], book['genre']))
    my_books_medium = my_books_long[0:997]
    my_books_short = my_books_long[0:10]

print("***********~Test with 10 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_short)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_A(my_books_short, 0, len(my_books_short))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n***********~Test with ~1,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_medium)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_A(my_books_medium, 0, len(my_books_medium))
# end = time.time()
# print("Quick Sort (A) took:  " + str((end - start)*1000) + " milliseconds")


print("\n**********~Test with +2,000 Books~**********")
start = time.time()
sorted_books = insertion_sort(my_books_long)
end = time.time()
print("Insertion Sort took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = quick_sort_B(my_books_long)
# end = time.time()
# print("Quick Sort (B) took:  " + str((end - start)*1000) + " milliseconds")

# start = time.time()
# sorted_books = book_sort(my_books_long)
# end = time.time()
# print("Book Sort took:       " + str((end - start)*1000) + " milliseconds\n")