import sys

size  = len(sys.argv)
if size < 2:
    sys.exit('You must provide an argument')
elif size > 2:
    sys.exit('Error: You must provide ONE argument only')
try :
    var_int = int(sys.argv[1])
    if (var_int == 0) :
        print("I'm Zero.")
    elif (var_int % 2 == 0) :
        print("I'm Even.")   
    else :
        print("I'm Odd.")
except:
    sys.exit('Error: Invalid type of argument')