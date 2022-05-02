import random

def find(ordered_list, number):
  ordered_list.sort()
  for i in ordered_list:
    if i == number:
      return True
      print("True")
  return False

l = []
for i in range(0, 5):
  li = random.randint(0, 10)
  l.append(li)
print(l)

print(find(l, 7))