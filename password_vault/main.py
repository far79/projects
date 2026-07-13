vault_data={
	"google" : {"username" : "icefire", "email" : "icefire@gmail.com", "password" : "icefire1234"},
	"git" : {"username" : "fireice", "email" : "fireice@gmail.com", "password" : "fireice1234"}
}

# opt_menu=int(input("which option:"))
# if opt_menu==1:
# 	a=vault_data[input("which service(google/git):")][input("which service(username/email/password):")]
# 	print(a)

# serv=input("which service(google/git):")

# if serv in vault_data:
# 	print("service:",serv,"exists")
# else:
# 	print("service:",serv,"doesn't exist")


print("1)to list/check service available\n2)to check password\n3)to change password\n4)exit")
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
