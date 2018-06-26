
def countZeroes(n):
    i = 5
    count =0
    while n/i:
        count += n//i
        i*=5
    return count

print(countZeroes(100))
