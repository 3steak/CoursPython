a = 5
b = 2



try:
    result =a/b
except ZeroDivisionError:
    print("Division par zero impossible")
else:
   print(result)
finally:
  print("The 'try except' is finished")