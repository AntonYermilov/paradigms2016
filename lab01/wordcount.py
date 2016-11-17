"""Wordcount exercise
Google's Python class
 
The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
 
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...
 
Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.
 
2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
 
Use str.split() (no arguments) to split on all whitespace.
 
Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.
 
Optional: define a helper function to avoid code duplication inside
print_words() and print_top().
 
"""
 
import sys
 
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
 

 
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def count_words(filename):
    fin = open(filename, 'r')
    cnt = {}
    for line in fin:
        for word in line.lower().split():
            if cnt.get(word) == None:
                cnt[word] = 0
            cnt[word] += 1
    fin.close()
    return cnt

def print_words(filename):
    print("\n".join("{} {}".format(x, y) for x, y in sorted(list(count_words(filename).items()))))

def print_top(filename):
    best = sorted([(-y, x) for x, y in count_words(filename).items()])
    for i in range(min(len(best), 20)):
        print(best[i][1], -best[i][0])


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)
 
    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)
 
if __name__ == '__main__':
    main()