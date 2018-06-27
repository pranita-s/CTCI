
# TIME - O(2 ** k)

def board(k,s,l,length,res):
    if k == 0:
        res.add(length)
    else:
        board(k-1,s,l,length+s,res)
        board(k-1,s,l,length+l,res)
    return res

res = set()
print(board(5,3,4,0,res))


# TIME - O(k)

def board(k,s,l):
    lengths  =  set()
    for number_s in range(k+1):
        number_l = k - number_s
        temp = number_s  * s + number_l * l
        lengths.add(temp)

    return list(lengths)

print(board(5,3,4))
