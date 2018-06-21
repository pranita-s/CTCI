
# TIME - O(n * Cat(n)) (Cat(n) -- nth Catalan number)
# Cat(n) = choose(2n, n) / (n + 1), O(n * Cat(n)) = O(choose(2n, n)) = O(4^n / sqrt(n))


def parens(num):
  result = []
  generateParens(result,'',num,num)
  return result

def generateParens(result,current,left,right):
  if left == 0 and right == 0:
    result.append(current)
  if left > 0 :
    generateParens(result,current+'(',left-1,right)
  if left < right:
    generateParens(result,current+')',left,right-1)


print(parens(3))
