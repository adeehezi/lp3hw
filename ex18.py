'''
Adee Hezi 
'''


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# okay that args is actually pointless, we can just do this
def print_two_again(arg1, arg2,):
    print(f"arg1: {arg1}, arg2: {arg2}")

 # this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
    print("I got nothin'.")


print_two("Adee", "Shaw")
print_two_again("Adee","Hezi")
print_one("First!")
print_none() 