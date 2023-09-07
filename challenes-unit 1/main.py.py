def fact_res(n):
  if n==0 or n==1:
    return 1
  else:
    return n *fact_res(n-1)
number=int(input("enter value:"))
res=fact_res(number)
print("The factorial of {} is {}.".format(number,res))