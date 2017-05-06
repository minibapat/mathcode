#!/usr/bin/python

def main():
  number = 5
  finalsum = calc_sum(number)
  print "Summation is " + str(finalsum)



def calc_sum(number):
  ii = 0
  summation = 0
  while ii <= number:
    summation = summation + ii
    ii = ii + 1
  return summation

main()
