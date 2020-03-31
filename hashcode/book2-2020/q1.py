from sys import argv, stdin
from statistics import mean
"""
num_books = number of books
num_libraries = number of libraries
num_days = number of available days

book_score List[int] = index: id of book, value: score of book
library_info List[(int, int)] = (signup_time, books_per_day)
library_books[set(int)] = [which book are in the library]
"""
num_books, num_libraries, num_days = [int(i) for i in stdin.readline().split(" ")]
book_scores = [int(i) for i in stdin.readline().split(" ")]
rest_lines = [line.split("\n")[:-1] for line in stdin.readlines()]
print(rest_lines)


# library_info = [tuple([int(d) for d in rest_lines[i][0].split(" ")]) for i in range(len(rest_lines)) if i % 2 == 0]
# library_info.pop()
# library_books = [set([int(book) for book in rest_lines[i][0].split(" ")]) for i in range(len(rest_lines)) if i % 2 == 1]


def parse(filename):
    
    data = open(filename)

    books, num_libraries, num_days = [int(i) for i in data.readline().split(" ")]
    book_scores = [int(i) for i in data.readline().split(" ")]
    rest_lines = [line.split("\n")[:-1] for line in data.readlines()]
    library_info = [tuple([int(d) for d in rest_lines[i][0].split(" ")[1:]]) for i in range(len(rest_lines)) if i % 2 == 0]
    library_books = [set([int(book) for book in rest_lines[i][0].split(" ")]) for i in range(len(rest_lines)) if i % 2 == 1]

    # print(library_books, library_info)



"""
1. Calculate average score of all librarue
2. Pick largest average score
3. Update all libraries by subtracting books in picked library and all other libraries
"""

# def all_scores(indeces, library_info, library_books):

#     maximum_score_per_day = 0
#     index = 0 
#     for i, info, books in zip(indeces, library_info, library_books):
#         signup_time, books_per_day = info

#         average_score = mean([book_scores[book] for book in books])
#         #delay in books?
#         score_per_day = (books_per_day * average_score)

#         if score_per_day > maximum_score_per_day:
#             maximum_score_per_day = score_per_day
#             index = i
    
#     return index

"""
1. sort by number of books descending
2. keep geting full out joins
3.      
"""

    

    
#index of books, index of libraries


# def library_score(info,books):
