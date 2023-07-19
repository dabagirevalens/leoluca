def non_recursive(n):
  if n < 2:
    raise ValueError('Invalid input')
  cur = 0
  for i in range(2, n + 1):
    cur += 1 / (i * (i - 1))
  return cur


n = 5
print(non_recursive(n))

# space complexity: O(1) bcz we only need to store the current value
# time complexity: O(n) // n is the input number since we need to loop through the input number