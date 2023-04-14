from datetime import datetime

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

try:
    print(datetime(*kata).strftime("%m/%d/%Y %H:%M"))
except:
    print("Some of your value are invalid")