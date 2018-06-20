# TIME - O(2 ** n)


def hanoi_recursive(num):

    def helper(num,from_peg,to_peg,use_peg):
        if num <=0:
            return
        helper(num-1,from_peg,use_peg,to_peg)
        pegs[to_peg].append(pegs[from_peg].pop())
        print(from_peg,to_peg)
        helper(num-1,use_peg,to_peg,from_peg)

    pegs = [list(reversed(range(1,num+1)))] + [[] for _ in range(1,num)]
    helper(num,0,1,2)

print(hanoi_recursive(4))


def hanoi_iterative(num):

    def legal_move(i,j):
        if not pegs[i]:
            pegs[i].append(pegs[j].pop())
            from_peg, to_peg = j, i
        elif not pegs[j]:
            pegs[j].append(pegs[i].pop())
            from_peg, to_peg = i, j
        else:
            if pegs[i][-1] > pegs[j][-1]:
                pegs[i].append(pegs[j].pop())
                from_peg, to_peg = j, i
            else:
                pegs[j].append(pegs[i].pop())
                from_peg, to_peg = i, j
        print(from_peg,to_peg)


    pegs = [list(reversed(range(1, num + 1)))] + [[] for _ in range(1, num)]
    total_moves = (2 ** num)-1
    from_peg, to_peg, use_peg = 0,1,2
    for i in range(1,total_moves+1):
        if i % 3 == 1:
            legal_move(from_peg, to_peg)
        elif i % 3 == 2:
            legal_move(from_peg, use_peg)
        elif i % 3 == 0:
            legal_move(to_peg, use_peg)


print(hanoi_iterative(4))
