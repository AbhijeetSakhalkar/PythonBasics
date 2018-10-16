def solve(a):
  max = 0
  for i in range(len(a)):
    for j in range(len(a)):
      if i != j and a[i] + a[j] > max:
        max = a[i] + a[j]
  return max

print(solve([1000,1,1000]))

