
A = list(map(int, input().split()))

n = len(A)

for j in range(1, n):
  key = A[j]
  i = j - 1

  while (i >= 0) and (A[i] > key):
    A[i + 1] = A[i]
    i -= 1

  A[i + 1] = key

print(A)
   