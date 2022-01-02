# Time Conversion

# https: // www.hackerrank.com/challenges/time-conversion

# Given a time in -hour AM/PM format, convert it to military(24-hour) time.

# Sample Input 0

# 07: 05: 45PM
# Sample Output 0

# 19: 05: 45

def timeConversion(s):
    array = []
    for i in s:
        array.append(i)
    if array[-2] == "P":
        if s[:2] == "12":
            return s[0:8]
        else:
            a = str(int(s[:2])+12)
            return a+s[2:8]

    else:
        if s[:2] == "12":
            return "00"+s[2:8]
        else:
            return s[:8]


# Mini-Max Sum

# https: // www.hackerrank.com/challenges/mini-max-sum

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is and the maximum sum is . The function prints

# 16 24


def miniMaxSum(arr):
    arr.sort()
    min = arr[0]+arr[1]+arr[2]+arr[3]
    max = arr[1]+arr[2]+arr[3]+arr[4]
    print(min, max)


# https: // www.hackerrank.com/challenges/birthday-cake-candles

    def birthdayCakeCandles(candles):
    count = 0
    for i in range(len(candles)):
        if max(candles) == candles[i]:
            count = count+1
    return count


# https: // www.hackerrank.com/challenges/grading/

    def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade >= 38:
            modul = grade % 5

            if modul >= 3:
                grade += (5-modul)
        res.append(grade)
    return res
