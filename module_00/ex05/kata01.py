# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

kata5 = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
'C++': 'Bjarne Stroustrup',
'C': 'Dennis Ritchie',
}

kata0 = {}


for language, person in kata.items() :
    print(f"{language} was created by {person}")
    
# for language, person in kata5.items() :
#     print(f"{language} was created by {person}")

# for language, person in kata0.items() :
#     print(f"{language} was created by {person}")