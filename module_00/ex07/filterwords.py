import sys

if len(sys.argv) != 3:
    sys.exit("Error: You must provide two arguments, one string then one integer")
try :
    x = int(sys.argv[2])
except :
    sys.exit("Error: You must provide two arguments, one string then one integer")
try :
    y = int(sys.argv[1])
    sys.exit("Error: You must provide two arguments, one string then one integer")
except :
    punctuation = '!()-{\}[]\',.?/:;"'
    tab = sys.argv[1].split(" ")
    
    result = []
    for word in tab:
        i = 0
        trim = ""
        for char in word:
            if (punctuation.find(char) < 0):
                i += 1
                trim += char
        if (i >= x):
            result.append(trim)
    print(f"{result}")