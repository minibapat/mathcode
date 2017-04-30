#!/usr/bin/python

def main():
  out_list = get_list()
  print out_list
  minimum1 = find_min(out_list)
  print "The minimum is " + str(minimum1)


def get_list():
  mylist = []
  while True:
    a = int(raw_input("Enter a list of numbers and I will find the minimum (-1 to quit): "))
    if (a == -1):
      break    
    mylist.append(a)
  return mylist

def find_min(out_list):
  min1 = out_list[0]
  remaining_list = out_list[1:]
  for ii in remaining_list:
    if ii<min1:
       min1 = ii
  return min1


main()
