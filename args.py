def print_two(*args):
	arg1, arg2 = args
	print("args1: %r, arg2: %r" % (arg1,arg2))

def print_two_again(arg1,arg2):
	print("arg1: %r , arg2: %r" % (arg1,arg2))

#this just take one argument
def print_one(arg1):
	print("arg1: %r" % arg1)

#this one thke no arguments
def print_none():
	print("i got nothin.")

print_two("zed","Shaw")
print_two_again("Zed", "Shaw")
print_one("first")
print_none()
