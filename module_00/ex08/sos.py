import sys

MORSE_CODE_DICT = { 65:'.- ', 66:'-... ',
                    67:'-.-. ', 68:'-.. ', 69:'. ',
                    70:'..-. ', 71:'--. ', 72:'.... ',
                    73:'.. ', 74:'.--- ', 75:'-.- ',
                    76:'.-.. ', 77:'-- ', 78:'-. ',
                    79:'--- ', 80:'.--. ', 81:'--.- ',
                    82:'.-. ', 83:'... ', 84:'- ',
                    85:'..- ', 86:'...- ', 87:'.-- ',
                    88:'-..- ', 89:'-.-- ', 90:'--.. ',
                    49:'.---- ', 50:'..--- ', 51:'...-- ',
                    52:'....- ', 53:'..... ', 54:'-.... ',
                    55:'--... ', 56:'---.. ', 57:'----. ',
                    48:'----- ', 32:'/ '}
i = 2
size  = len(sys.argv)
if size == 1:
    sys.exit('Please provide a string to translate')
str = sys.argv[1]
while i < size:
    str += " " + sys.argv[i]
    i += 1
for char in str:
    if (char.isalnum() == True):
        continue
    elif (char == ' '):
        continue
    else : 
        sys.exit('The string must be composed of alphanumeric characters and spaces only')        
str = str.upper()
str = str.translate(MORSE_CODE_DICT)
print(str)
