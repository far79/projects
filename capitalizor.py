cont="yes"
while(cont=="yes"):
	txt=input("enter your text:")
	Cap_txt=txt.upper()
	if (txt==Cap_txt):
		print("given input is already capitalized/Number/Special Character")
	else:
		print(Cap_txt)
	cont=input("want to continue(yes/no)")