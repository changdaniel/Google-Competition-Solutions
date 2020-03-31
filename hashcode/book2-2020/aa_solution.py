from sys import stdin

num_books, num_libraries, num_days = [int(i) for i in stdin.readline().split(" ")]
book_scores = [int(i) for i in stdin.readline().split(" ")]
rest_lines = [line.split("\n")[:-1] for line in stdin.readlines()]
library_info = [tuple([int(d) for d in rest_lines[i][0].split(" ")[1:]]) for i in range(len(rest_lines)) if i % 2 == 0]
library_books = [set([int(book) for book in rest_lines[i][0].split(" ")]) for i in range(len(rest_lines)) if i % 2 == 1]
# sorted_library_books = [sorted(library_books, key=lambda book: book_scores[book]) for library_books in library_books]
sorted_library_books = [sorted(library_books, key=lambda book: book_scores[book]) for library_books in library_books]

def compute_score(library, day, books):
	sign_up_time, books_per_day = library_info[library]

	offset = 0
	score = 0
	added_books = set()
	for day in range(day + sign_up_time, num_days):
		for i in range(books_per_day):
			while offset < len(sorted_library_books[library]) and sorted_library_books[library][offset] in books:
				offset += 1

			if offset < len(sorted_library_books[library]):
				book = sorted_library_books[library][offset]
				score += book_scores[book]
				added_books.add(book)
				offset += 1
			else:
				return score, added_books

	return score, added_books

def compute_total_score():
	day = 0
	score = 0
	books = set()
	libraries = set()
	library_books = {}
	while day < num_days:
		max_library_score = 0
		max_library = -1
		max_library_added_books = set()
		for library in range(num_libraries):
			if library in libraries:
				continue
			# if len(sorted_library_books[library]) < 450:
			# 	continue
			if library_info[library][0]>480:
				continue

			library_score, library_added_books = compute_score(library, day, books)
			if library_score > max_library_score:
				max_library_score = library_score
				max_library = library
				max_library_added_books = library_added_books

		if max_library >= 0:
			day += library_info[max_library][0]
			score += max_library_score
			libraries.add(max_library)
			books.update(max_library_added_books)
			library_books[max_library] = max_library_added_books
		else:
			break
	print(score)

	out = str(len(libraries)) + '\n'
	for library in libraries:
		out += str(library) + " " + str(len(library_books[library])) + '\n'
		books = ""
		for book in library_books[library]:
			books += str(book) + " "

		out += books + '\n'

	return out

out = compute_total_score()

output = open("out.txt", "w")
output.write(out)
