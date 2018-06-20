# TIME AND SPACE - O(n2**n)


result = []
def Power(A):
    PowerSet([],A)
    print(result)

def PowerSet(soFar,remaining):
    if remaining == []:
        result.append(soFar)
    else:
        PowerSet(soFar+remaining[:1],remaining[1:])
        PowerSet(soFar,remaining[1:])

(Power([1,2,3]))

# COMBINATORICS

def PowerSet(arr):
	result = []
	for i in range(1<<len(arr)):
		subset = [arr[bit_position] for bit_position in range(len(arr)) if is_bit_set(i,bit_position)]
		result.append(subset)
	return result

def is_bit_set(num,bit_position):
	return num & (1<<bit_position)
	
arr = [1,2,3]
print(PowerSet(arr))


