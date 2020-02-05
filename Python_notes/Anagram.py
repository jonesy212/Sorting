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

# iterative solution
def find_celebrity():
    for i in range(len(people)):
        if len(people[i].known) == 0:
            return i
    
    people.sort() (based on known[])

#recursive
def find_celebrity(people):
    if len(people[0].known) == 0:
        return people[0] 

    else:
        #recursive is worse due to space
        return rec_find_celebrity(people[1:])   

# two numbers in the sequence equal the 
#proceeding 
def fib(n):
    if n == 0 or 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

bigcheatsheet.com