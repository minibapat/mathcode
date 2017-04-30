#!/usr/bin/python

def main():
  mylist = read_list()
  product = find_prod(mylist)
  print product  


def read_list():
  out_list=[]
  while True:
    a = int(raw_input("Enter number (-1 to end) : "))
    if a==-1:
      break
    out_list.append(a)
  return out_list


def find_prod(mylist):
  myprod = 1
  for ii in mylist:
    myprod = ii * myprod   
  return myprod


main()
