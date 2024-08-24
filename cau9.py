import math
a= float(input("a: "))
b= float(input("b: "))
A=math.sqrt(a)
B=math.sqrt(b)
C=math.sqrt(a*b)
ket_qua= ((A-B)/(A**(1/2)-B**(1/2)))-((A+C**(1/2))/((A**(1/2)+B**(1/2))))
print("ket qua: ", ket_qua)

