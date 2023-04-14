import sys

def text_analyser(text=""):
    "This function print the numbers of uppercase letters, lowercase letters, \
spaces and ponctuation signs in the chain provide as an argument"
    while (len(text) == 0):
        print ('What is the text to analyse?')
        text = input();  

    if type(text) != str:
        print('Error : Argument is not a string')
    punctuation = '!()-{\}[],.?/:;"'
    nb_char = 0
    lower = 0
    upper = 0
    sign = 0
    space = 0
    for character in text:
        if (character.islower()):
            lower += 1
        elif (character.isupper()):
            upper +=1
        elif (character.isspace()):
            space += 1
        elif (punctuation.find(character) >= 0):
            sign += 1
    nb_char = lower + upper + space + sign
    print("The text contains ", nb_char, 'character(s): \n- ', upper, ' upper letter(s)\n- ', lower, ' lower letter(s)\n- ', sign, ' punctuation mark(s)\n- ', space, ' space(s)\n')

if __name__ == "__main__": 
    size = len(sys.argv)
    if size > 2:
        print('Error: You must provide ONE argument')
    elif size < 2:
        text_analyser("") 
    else:
        text_analyser(sys.argv[1])