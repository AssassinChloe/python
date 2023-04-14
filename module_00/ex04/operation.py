import sys

if len(sys.argv) > 3:
    sys.exit("You must provide two int as arguments")
  
try :
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print("Sum: ".ljust(12), x+y)
    print("Difference: ".ljust(12), x-y)
    print("Product: ".ljust(12), x*y)
    if (y == 0) :
        print("Quotient: ".ljust(12), "ERROR (division by 0)")
        print("Remainder: ".ljust(12), "ERROR (modulo by 0)")
    else:
        print("Quotient: ".ljust(12), x/y)
        print("Remainder: ".ljust(12), x%y)
except:
    sys.exit("You must provide two int as arguments")