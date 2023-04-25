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
    print("This is the list of the recipe in your cookbook:")
    for recipe in cookbook:
        print(f"  -{recipe}")
    print("")

    
def print_recipe():
    print("Please enter a recipe name to get its details:")
    recipe = input()
    for key in cookbook:
        if (recipe == key):
            ingredients, meal, prep_time = cookbook[recipe].values()
            print(f"Recipe for {recipe} :")
            print(f"  Ingredients list : {ingredients}")
            print(f"  To be eaten for {meal}")
            print(f"  Takes {prep_time} minutes of cooking\n")
            
            return
    print("Sorry, this recipe does not exists\n")
    
def delete_recipe():
        print("Please enter a recipe name to delete:")
        recipe = input()
        try:
            if (cookbook[recipe]):
                del cookbook[recipe]
                print("Recipe successfully deleted\n")
                return
        except:
            print("Sorry, this recipe does not exists\n")
        
    
def add_recipe():
    print("Please enter a name:")
    recipe = input()
    try :
        if (cookbook[recipe]):
            print("Sorry, this recipe allready exists\n")
    except :
        print("Please enter ingredients (one by line)")
        text = input()
        ingredients = []
        while text:
            ingredients.append(text)
            text = input()
        print("Please enter a meal type (ex: breakfast, lunch, diner, dessert...)")
        meal = input()
        print("\nPlease enter a preparation time (in minutes)")
        prep_time = input()
        cookbook.update({recipe:{'ingredients':ingredients, 'meal':meal, 'prep_time':prep_time}})
        print(f"\n{recipe} succesfuly add into the cookbook!\n")
    
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
    print("\nSorry, this option does not exist\n")
    return False
    
print('Welcome to the Python Cookbook !\n')
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


