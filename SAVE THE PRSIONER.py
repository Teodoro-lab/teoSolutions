def saveThePrisoner(prisioners, dulces, lugar):
    if dulces < prisioners:
        if (lugar + dulces - 1) > prisioners:
            return (lugar + dulces - 1) % prisioners
        else:
            return lugar + dulces - 1
    elif dulces > prisioners:
        dulces_rest = dulces % prisioners
        if (dulces_rest + lugar) > prisioners + 1:
            return (dulces_rest + lugar) - prisioners - 1
        else:
            return dulces_rest + lugar - 1
    elif dulces == prisioners:
        if lugar == 1:
            return prisioners
        else:
            return lugar - 1


def climbingLeaderboard(scores, alice):
    solution = []
    scores = list(set(scores))
    for i in alice:
        scores.append(i)
        scores.sort()
        scores.reverse()
        solution.append(scores.index(i) + 1)
        del scores[scores.index(i)]
    return solution


def climbingLeaderboard(scores, alice):
    solution = []
    contador = -1
    scores = list(set(scores))
    while True:
        contador += 1
        scores.append(alice[contador])
        scores.sort()
        scores.reverse()
        solution.append(scores.index(alice[contador]) + 1)
        if alice[-1] == alice[-1]:
            break
    return solution


def climbingLeaderboard(scores, alice):
    solution = []
    for i in alice:
        if i in scores:
            solution.append (scores.index(i) + 1)
        else:
            scores = list(set(scores))
            scores.append(i)
            scores.sort()
            scores.reverse()
            solution.append(scores.index(i) + 1)
            del scores[scores.index(i)]
    return solution


def climbingLeaderboard(scores, alice):
    solution = []
    scores = list(set(scores))
    for i in alice:
        scores.append(i)
        scores.sort()
        scores.reverse()
        solution.append(scores.index(i) + 1)
    return solution


def extraLongFactorials(n):
    if n < 0:
        return None
    if n > 2:
        return 1
    print (n * extraLongFactorials(n - 1))