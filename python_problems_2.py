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
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    total = 0
    for i in student_marks[query_name]:
        total = total+i
    res = total/3
    formatted = "{:.2f}".format(res)
    print(formatted)
