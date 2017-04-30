#!/usr/bin/python
import math

def main():
  list1 = read_list()
  maxnum = find_max(list1)
  ntoadd = num_to_add(maxnum)
  curved_list = get_curved_list(list1,maxnum)
  print curved_list


def get_curved_list(list1,maxnum):
  out_list=[]
  for ii in list1:
    out_list.append(ii+maxnum)
  return out_list

def num_to_add(max):
  return 100 - max


def find_max(list1):
  max=0
  for ii in list1:
    if ii>max:
      max=ii
  return max


def read_list():
  out_list=[]
  while True:
    a = int(raw_input("Enter number (-1 to end) : "))
    if a==-1:
      break
    out_list.append(a)
  return out_list



main()
