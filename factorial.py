#!/usr/bin/python

def main():
  Num_to_fact = 10
  factorialed = compute_fact(Num_to_fact)
  print "The factorial is " + str(factorialed)

def compute_fact(num):
  product = 1
  list1 = range(1, num+1)
  for ii in list1:
    product = ii * product
  return product


main()
