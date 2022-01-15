
# https://www.hackerrank.com/challenges/circular-array-rotation

def circularArrayRotation(a, k, queries):
    result = []
    k=k%n
    for q in queries:
        result.append(a[(n-k+q)%n])
    return result

# https://www.hackerrank.com/challenges/permutation-equation

def permutationEquation(p):
    result = []
    for i in range(1,len(p)+1):
        result.append(p.index(p.index(i)+1)+1)
    return result