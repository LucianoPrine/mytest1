import math
import random

def double_print(str_input):
  print(str_input)
  print(str_input)
  
double_print("hello world")
print("My favorite number is {:.2f}.".format(math.pi))
rand_num = round(random.random()*100)
print(f"Here is a random number: {ran_num}")
