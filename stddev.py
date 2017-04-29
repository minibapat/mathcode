#!/usr/bin/python
import math

def main():

  list1 = [37,38,38,39,39,39,39,39,40,40,40,40,41,41,41,41,42,42,42,42]
  n = len(list1)
  mysum = mylist_sum(list1)
  mean1 = calculate_mean(mysum, n)
  findsummation = calculate_summation(mean1, list1, n)
  variance1 = calc_variance(findsummation, n)
  mystandarddev = findsd(variance1)
  print "The standard deviation of list:" 
  print list1
  print " is " + str(mystandarddev)

def mylist_sum(mylist):
  mysum1 = 0
  for ii in mylist:
    mysum1 = mysum1 + ii
  return mysum1

def calculate_mean(listsum, nums):
  finalmean = listsum / (nums *1.0)
  return finalmean

def calculate_summation(mean1, list1, n):
  mysum=0
  for ii in list1:
    diff1 = ii - mean1
    finalseries = diff1*diff1
    mysum = mysum + finalseries
  return mysum

def calc_variance(findsummation, n):
  myvariance = findsummation/(n*1.0)
  return myvariance

def findsd(variance1):
  finalstanddev = math.sqrt(variance1)
  return finalstanddev


main()

