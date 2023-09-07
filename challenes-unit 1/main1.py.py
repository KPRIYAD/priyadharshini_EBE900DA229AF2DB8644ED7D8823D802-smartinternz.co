def isleapyear(year):
  if(year%4==0 and year%100!=0):
    return True
  else:
    return False
year=int(input("Enter a year"))
if isleapyear(year):
  print('{} is a leapyear.'.format(year))
else:
  print('{} is not a leapyear.'.format(year))
    