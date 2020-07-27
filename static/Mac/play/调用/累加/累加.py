def sum_numbers(num):
  if num == 1:
    return 1
  temp = sum_numbers(num - 1)
  return num + temp

print(sum_numbers(3))



def sum_numbers(num):
  if num == 3:
    return 3
  temp = sum_numbers(num + 1)
  return num + temp

print(sum_numbers(1))


def my_sum(i):
  if i < 0:
    raise ValueError
  elif i <= 1:
    return i
  else:
    return i + my_sum(i - 1)

print(my_sum(10))
print(my_sum(100))