# 기본계산기
def add(a, b):
  return a+b

def subtract(a, b):
  return a-b

def multiply(a, b):
  return a+b

def divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

def power_free(a, b):
  return a ** b

def square(a):
  return a*a