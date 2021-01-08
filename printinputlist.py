def myfunc():
  numbers = list()

  while True:
    a = input("a: ")
    b = input("b: ")

    numbers.append(a + b)

    if input("repeat? y/n:") != "y":
      break

  print(numbers)
  print(numbers[1])
  print(numbers[0])
 
  for i in range(len(numbers)):
      print(numbers[i])


myfunc()