# https: // www.hackerrank.com/challenges/between-two-sets

def getTotalX(a, b):
    multa = []
    multb = []
    final = []
    totallen = len(a+b)
    for i in range(1, 101):
        for aa in a:
            if i % aa == 0:
                multa.append(i)
        for bb in b:
            if bb % i == 0:
                multb.append(i)
        potential = multa+multb

    for number in potential:
        if potential.count(number) == totallen:
            final.append(number)
    return len(set(final))
