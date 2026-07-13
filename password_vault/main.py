vault_data={
	"google" : {"username" : "icefire", "email" : "icefire@gmail.com", "password" : "icefire1234"},
	"git" : {"username" : "fireice", "email" : "fireice@gmail.com", "password" : "fireice1234"}
}

opt_menu=int(input("which option:"))
if opt_menu==1:
	a=vault_data[input("which service(google/git):")][input("which service(username/email/password):")]
	print(a)

