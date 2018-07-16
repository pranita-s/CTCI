
def tokenize(s):
    tokens = []
    start = 0
    for i,c in enumerate(s):
        if c in '+-/*':
            if i == 0 or i == len(s)-1:
                raise Exception('missing numbers')
            tokens.append(int(s[start:i]))
            tokens.append(c)
            start = i + 1
        elif c not in '0123456789':
            raise Exception('unknown character')
    tokens.append(int(s[start:]))
    return tokens

def compute(s):
    tokens = tokenize(s)
    result = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "*":
            result[-1] *= tokens[i + 1]
            i += 2
        elif tokens[i] == "/":
            result[-1] /= tokens[i + 1]
            i += 2
        else:
            result.append(tokens[i])
            i += 1
    res = result[0]
    for i in range(1,len(result),2):
        if result[i] == '+':
            res += result[i+1]
        elif result[i] == '-':
            res -= result[i+1]
    return res

print(compute('15-3/1'))
