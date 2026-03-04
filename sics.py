#Regular falsi method for pre defined equation and values
a=1.5
b=2
x=a
y1=(x**4)-12
print("When a is in the function",y1)

x=b
y2=(x**4)-12
print("When b is the function",y2)

x1=((a*y2)-(b*y1))/(y2-y1)
print("The first approximation is",x1)

y3=(x1**4)-12
print("The value of the first approximation in the function is",y3)

#Since the value of first approx in the function is negative and greater the lower part of the given interval..
#The root lies in between the y3 and b
x2=((x1*y2)-(b*y3))/(y2-y3)
print("The second approximation is",x2)
y4=(x2**4)-12
print("The value of the second approximation in the function is",y4)

#Since the value of second approx in the function is negative and greater the lower part of the given interval..
#The root lies in between the y4 and b
x3=((x2*y2)-(b*y4))/(y2-y4)
print("The third approximation is",x3)
y5=(x3**4)-12
print("The value of the third approximation in the function is",y5)

#Since the value of second approx in the function is negative and greater the lower part of the given interval..
#The root lies in between the y5 and b

x4=((x3*y2)-(b*y5))/(y2-y5)
print("The fourth approximation is",x4)
y6=(x4**4)-12
print("The value of the fourth approximation in the function is",y6)

#Since the value of fourth approximation in function can be approximated to 0, The 4rth approximation is the root
print(f"The root is {x4:.4}")