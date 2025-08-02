#Greet my users😎
a = "Hello There😎😎. I'm a simple calc... "
b = "Welcome aboard"

#the calculator
x=float(input("Enter first value: "))
operator=str(input("input your operator"))
y=float(input("Enter last Value: "))

# check the operator chosen

if operator == '+':
    result=x+y

elif operator == '-':
    result=x-y

elif operator == '*':
    result=x*y

elif operator == '/':
    result=x/y

else: 
    print("input a valid operator i.e +,-,*,/")

    



