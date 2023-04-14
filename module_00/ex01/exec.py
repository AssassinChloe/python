import sys

i = 2
size  = len(sys.argv)
if size == 1:
    sys.exit('')
str = sys.argv[1]
while i < size:
    str += " " + sys.argv[i]
    i += 1
str = str[::-1]
print(str.swapcase())
