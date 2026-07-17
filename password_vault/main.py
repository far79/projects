vault_data={
	"google" : {"username" : "icefire", "email" : "icefire@gmail.com", "password" : "icefire1234"},
	"git" : {"username" : "fireice", "email" : "fireice@gmail.com", "password" : "fireice1234"}
}


print("1)to list/check service available\n2)to check password\n3)to change password\n4)to generate a random password\n5)to exit")
opt_menu=int(input("choose option number:"))

if opt_menu==1:
	print("1)list all service\n2)check service")
	opt_ser=int(input("choose option number:"))
	if opt_ser==1:
		print(list(vault_data.keys()))
	if opt_ser==2:
		serv=input("Enter Service name:")
		if serv in vault_data:
			print("service:",serv,"exists")
		else:
			print("service:",serv,"doesn't exist")

if opt_menu==2:
	a=vault_data[input("which service(google/git):")][input("which credential(username/email/password):")]
	print(a)

if opt_menu==3:
	serv=input("type selected service\n1)google\n2)git")
	cred=input("type selected credential\n1)username\n2)email\n3)password")
	new_cred=input("type new credential")
	vault_data[serv][cred]=new_cred
	print(vault_data)

if opt_menu==4:
	import string
	import random
	character = string.ascii_letters + string.digits + string.punctuation
	password=""
	for i in range(12):
		password+=random.choice(character)
	print(password)


if opt_menu==5:
	print("Exiting")