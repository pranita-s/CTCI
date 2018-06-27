# TIME - O(PlogP)

def sortYears(people,b):
    arr = []
    if b:
        for p in people:
            arr.append(p.b)
    else:
        for p in people:
            if p.d:
                arr.append(p.d)
    arr.sort()
    return arr

def most_living_people(people):
    b = sortYears(people,True)
    d = sortYears(people,False)
    maxPeople = 0
    temp = 0
    maxYear = 0
    i , j = 0, 0
    while i < len(b) and j < len(d):
        if b[i] <= d[j]:
            temp += 1
            if temp > maxPeople:
                maxYear = b[i]
                maxPeople = temp
            i+=1
        else:
            temp -= 1
            j += 1

    return maxYear

# TIME - O(Range + P)

def most_living_people(people):
    if len(people) == 0:
        return None
    arr = [0] * 102
    for p in people:
        addIndex = p.b - 1900
        arr[addIndex] += 1
        if p.d:
            subtractIndex = p.d - 1900 + 1
            arr[subtractIndex] -= 1


    maxYear = 0
    maxPeople = 0
    temp = 0
    for i in range(len(arr)):
        temp += arr[i]
        if temp > maxPeople:
            maxPeople = temp
            maxYear = i

    return maxYear+1900
 
class P:
    def __init__(self,birth,death = None):
        self.b = birth
        self.d = death


people=[P(1907,1942),P(1909,1982),P(1933,1967),P(1912,1954),P(1980),P(1988)]
print(most_living_people(people))
