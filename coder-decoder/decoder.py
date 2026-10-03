msg = input("Enter your message:")
msg = msg

c1 = "!"
c2 = "@"
c3 = "#"
c4 = "$"
c5 = "%"
c6 = "^"
c7 = "&"
c8 = "*"
c9 = "("
c0 = ")"
if c1 in msg:
	msg = msg.replace("!", "1")

if c2 in msg:
	msg = msg.replace("@", "2")

if c3 in msg:
	msg = msg.replace("#", "3")

if c4 in msg:
	msg = msg.replace("$", "4")

if c5 in msg:
	msg = msg.replace("%", "5")

if c6 in msg:
	msg = msg.replace("^", "6")

if c7 in msg:
	msg = msg.replace("&", "7")

if c8 in msg:
	msg = msg.replace("*", "8")

if c9 in msg:
	msg = msg.replace("(", "9")

if c0 in msg:
	msg = msg.replace(")", "0")

print(msg)