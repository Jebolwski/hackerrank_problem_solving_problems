# Finding the percentage

# https://www.hackerrank.com/challenges/finding-the-percentage

# The provided code stub will read in a dictionary containing key/value pairs of name: [marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Example


# The query_name is 'beta'. beta's average score is .

# Input Format

# The first line contains the integer, the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

# Constraints

# Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()

    total = 0
    for i in student_marks[query_name]:
        total = total+i
    res = total/3
    formatted = "{:.2f}".format(res)
    print(formatted)

# Lists

# https://www.hackerrank.com/challenges/python-lists/

# Consider a list(list=[]). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of
# commands where each command will be of the  types
# listed above. Iterate through each command in order and perform the
# corresponding operation on your list.

    list = []
N = int(input())
for line in range(N):
    cmd = input().split()
    if cmd[0] == "insert":
        list.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "print":
        print(list)
    elif cmd[0] == "remove":
        list.remove(int(cmd[1]))
    elif cmd[0] == "sort":
        list.sort()
    elif cmd[0] == "pop":
        list.pop()
    elif cmd[0] == "reverse":
        list.reverse()
    elif cmd[0] == "append":
        list.append(int(cmd[1]))

#Tuples

#https://www.hackerrank.com/challenges/python-tuples/

# Task
# Given an integer,n , and n space-separated integers as input, create a tuple,t , of those n integers.
#  Then compute and print the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format

# The first line contains an integer, , denoting the number of elements in the tuple.
# The second line contains  space-separated integers describing the elements in tuple .

# Output Format

# Print the result of hash(t).

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))
