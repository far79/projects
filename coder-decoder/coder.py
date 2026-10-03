msg = input("Enter your message:")
msg = str(msg)
c1 = "1"
c2 = "2"
c3 = "3"
c4 = "4"
c5 = "5"
c6 = "6"
c7 = "7"
c8 = "8"
c9 = "9"
c0 = "0"
if c1 in msg:
	msg = msg.replace("1", "!")

if c2 in msg:
	msg = msg.replace("2", "@")

if c3 in msg:
	msg = msg.replace("3", "#")

if c4 in msg:
	msg = msg.replace("4", "$")

if c5 in msg:
	msg = msg.replace("5", "%")

if c6 in msg:
	msg = msg.replace("6", "^")

if c7 in msg:
	msg = msg.replace("7", "&")

if c8 in msg:
	msg = msg.replace("8", "*")

if c9 in msg:
	msg = msg.replace("9", "(")

if c0 in msg:
	msg = msg.replace("0", ")")

print(msg)
