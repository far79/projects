def add(x,y):
	return (x+y)

def sub(x,y):
	return(x-y)

def mul(x,y):
	return(x*y)

def div(x,y):
	return(x/y)

print("choose a operation to perform by number:\n","1)add\n2)sub\n3)mul\n4)div",sep="")

b="yes"

while (b=="yes"):
	a=int(input("enter operation number:"))
	if(a==1):
		res=add(float(input("enter first number:")),float(input("enter second number:")))
		print(res)
	elif(a==2):
		res=sub(float(input("enter first number:")),float(input("enter second number:")))
		print(res)
	elif(a==3):
		res=mul(float(input("enter first number:")),float(input("enter second number:")))
		print(res)
	elif(a==4):
		res=div(float(input("enter first number:")),float(input("enter second number:")))
		print(res)
	b=input("Do you want to continue calculation(yes/no)")







