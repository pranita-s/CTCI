# TIME - O(C(n))
# nth Catalan number = (2n)!/((n+1)!n!)


def stringToBool(s):
    if s == '1':return True
    else: return False

def countEval(s,result,memo):

    if len(s) == 0 :
        return 0
    if len(s) == 1:
        return int(stringToBool(s) == result)
    if str(result)+s in memo:
        return memo[str(result)+s]

    ways = 0
    for i in range(1,len(s),2):
        operation = s[i]
        left = s[:i]
        right = s[i+1:]

        leftTrue = countEval(left,True,memo)
        leftFalse = countEval(left,False,memo)
        rightTrue = countEval(right,True,memo)
        rightFalse = countEval(right,False,memo)
        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

        totalTrue = 0

        if operation == '^':
            totalTrue = leftFalse * rightTrue + leftTrue * rightFalse
        elif operation == '&':
            totalTrue = leftTrue * rightTrue
        elif operation == '|':
            totalTrue = leftFalse * rightTrue + leftTrue * rightFalse + leftTrue * rightTrue

        if result == True:
            subways = totalTrue
        else:
            subways = total - totalTrue

        ways += subways

    memo[str(result)+s] = ways
    return ways

memo = {}
print(countEval('1^0|0|1',False,memo))
