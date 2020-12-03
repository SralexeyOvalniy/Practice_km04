n = int(input())
def PascalTriangle(n):
   rows = [1]
   y = [0]
   for x in range(n):
      print(rows)
      trow=[left+right for left,right in zip(rows+y, y+rows)]
   return n>=1
PascalTriangle(n)