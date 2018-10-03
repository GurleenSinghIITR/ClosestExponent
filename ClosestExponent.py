#This function finds the exponent to the base which gives the nearest number to the given number. If there are two exponents, it gives the smaller one
import math
def closest_power(base, num):
  if base <1 or base%1!=0 or num <1 or num%1!=0:
    return -1
  ee = math.log(num,base)
  e1 = math.ceil(ee)
  e2 = math.floor(ee)
  if abs(num-base**e1)<abs(num-base**e2):
    return e1 
  else:
    return e2  

print(closest_power(2,34))
print(closest_power(2,1022))
print(closest_power(5,375))