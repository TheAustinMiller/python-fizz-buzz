msg = ""
for i in range(1, 101):
  if i % 3 == 0:
    msg += "Fizz"
  if i % 5 == 0:
    msg += "Buzz"
  if msg == "":
    msg = str(i)
  print(msg)
  msg = ""
