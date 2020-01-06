## A Sorted Tale - CodeAcademy
## Import not working
#import utils
import csv

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
    bookshelf = []
    with open(filename) as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            # add your code here
            book['author_lower'] = book['author'].lower()
            book['title_lower'] = book['title'].lower()

            bookshelf.append(book)
    return bookshelf

## Import not working
#import sorts
import random

def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
        if comparison_function(arr[idx], arr[idx + 1]):
            sorted = False
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
            swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)

## Different Sorting Comparisons
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
    return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])

## Read in the small list of books for developing algorithms
bookshelf = load_books('Python_Programming/computer_science/a_sorted_tale_bubble_sort/books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf = load_books('Python_Programming/computer_science/a_sorted_tale_bubble_sort/books_large.csv')

## Print out the titles
print("##### Current Sort #####")
for book in bookshelf:
    print(book['title'])
print("##### Current Sort #####")

## Bubble Sort - By Title
sort_1 = bubble_sort(bookshelf, by_title_ascending)

## Print out the titles of sort_1
print("##### Sort 1: Bubble Sort - By Title #####")
for book in sort_1:
    print(book['title'])
print("##### Sort 1 #####")

## Bubble Sort - By Author
sort_2 = bubble_sort(bookshelf_v2, by_author_ascending)

## Print out the titles of sort_2
print("##### Sort 2: Bubble Sort - By Author #####")
for book in sort_2:
    print(book['author'])
print("##### Sort 2 #####")

## Quick Sort - By Author
quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

## Print out the titles of sort_1
print("##### Sort 3: Quick Sort - By Author #####")
for book in bookshelf_v2:
    print(book['author'])
print("##### Sort 3 #####")

## Bubble Sort - By Total Length
sort_4 = bubble_sort(long_bookshelf, by_total_length)

## Print out the titles of sort_1
print("##### Sort 4: Bubble Sort - By Total Length #####")
for book in sort_4:
    print(len(book['title']) + len(book['author']))
print("##### Sort 4 #####")

## Quick Sort - By Total Lenght
quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

## Print out the titles of sort_1
print("##### Sort 5: Quick Sort - By Total Length #####")
for book in long_bookshelf:
    print(len(book['title']) + len(book['author']))
print("##### Sort 5 #####")