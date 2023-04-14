import sys

cookbook = {'sandwich':{
                'ingredients':['ham', 'bread', 'cheese', 'tomatoes'], 
                'meal':'lunch', 
                'prep_time':'10'}, 
            'cake':{
                'ingredients':['flour', 'sugar', 'eggs'], 
                'meal':'dessert', 
                'prep_time':'60'},
            'salad':{
                'ingredients':['avocado', 'aragula', 'tomatoes', 'spinach'], 
                'meal':'lunch', 
                'prep_time':'15'}}

def print_all():
    for recipe, instructions in cookbook.items():
        ingredients, meal, prep_time = instructions.values()
        print(f"Recipe for {recipe}")
        print(f"  Ingredients list : {ingredients}")
        print(f"  To be eaten for {meal}")
        print(f"  Takes {prep_time} minutes of cooking\n")
    
def print_recipe():
    print("Please enter a recipe name to get its details:")
    recipe = input()
    for key in cookbook:
        if (recipe == key):
            ingredients, meal, prep_time = cookbook[recipe].values()
            print(f"Recipe for {recipe}")
            print(f"  Ingredients list : {ingredients}")
            print(f"  To be eaten for {meal}")
            print(f"Takes {prep_time} minutes of cooking\n")
            
            return
    print("Sorry, this recipe does not exists\n")
    
def delete_recipe():
        print("Please enter a recipe name to delete:")
        recipe = input()
        if (cookbook[recipe]):
            del cookbook[recipe]
            print("Recipe successfully deleted\n")
            return
        print("Sorry, this recipe does not exists\n")
        
    
def add_recipe():
    print("Please enter a name:")
    recipe = input()
    if (cookbook[recipe]):
        print("Sorry, this recipe allready exists\n")
    else:
        print("Please enter ingredients:")
        text = input()
        ingredients = []
        while text:
            ingredients.append(text)
            text = input()
        print("Please enter a meal type")
        meal = input()
        print("Please enter a preparation time")
        prep_time = input()
        cookbook.update({recipe:{'ingredients':ingredients, 'meal':meal, 'prep_time':prep_time}})
    
def is_valid_choice(input):
    valid_choices = ['1', '2', '3','4','5']
    for choice in valid_choices:
        if (input == choice):
            if choice == '1':
                add_recipe()
                return(False)
            elif choice == '2':
                delete_recipe()
                return(False)
            elif choice == '3':
                print_recipe()
                return(False)
            elif choice == '4':
                print_all()
                return(False)
            elif choice == '5':
                print("Cookbook closed. Goodbye!\n")
                return True
    print("Sorry, this option does not exists\n")
    return False
    
print('Welcome to the Python Cookbook !')
is_valid = False
options = ['Add a recipe', 'Delete a recipe', 'Print a recipe', 'Print the cookbook', 'Quit']
while is_valid != True:
    print('List of available option:')
    i = 1
    for option in options :
        print(f"   {i}: {option}")
        i += 1
    print('\nPlease select an option: ')
    choice = input()
    is_valid = is_valid_choice(choice)


