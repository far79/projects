# cont="yes"
# while(cont=="yes"):
# 	txt=input("enter your text:")
# 	Cap_txt=txt.upper()
# 	if (txt==Cap_txt):
# 		print("given input is already capitalized/Number/Special Character")
# 	else:
# 		print(Cap_txt)
# 	cont=input("want to continue(yes/no)")


def swap(text):
  list1 = list(text)
  list2 = []
  for i in list1:
    if i != i.upper():
      list2.append(i.upper())
    elif i != i.lower():
      list2.append(i.lower())
    else:
      list2.append(i)
  return "".join(list2)
  

print(swap("fnegFNESNG"))