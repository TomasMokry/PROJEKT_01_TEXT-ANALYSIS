"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomáš Mokrý
email: tomas.mokry@gmail.com
discord: Tomas M#0922

"""

users = {
'bob' : '123',
'ann' : 'pass123',
'mike' : 'password123',
'liz' : 'pass123'
}
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = 50 * '-'

user_in = input('user: ')
password_in = input('password: ')
print(separator)

if user_in in users and password_in == users[user_in]:
    print(f'Welcome to the app, {user_in}')
    print('We have 3 texts to be analyzed.')
    
else:
    print(f'Unregistered user, terminating the program..')
    quit()

print(separator)

text_in = input('Enter a number btw. 1 and 3 to select: ')

print(separator)

if not text_in.isnumeric():
    print('Not number. Terminating the program..')
    quit()
elif not 1 <= int(text_in) <= 3:
    print('Selected number is not in the list. Terminating the program..')
    quit()
else:
    text_selected = TEXTS[int(text_in) - 1]

text_clean = list()
text_istitle = list()
text_isupper = list()
text_islower = list()
numbers = list()

for word in text_selected.split():
    text_clean.append(word.strip('.,:'))

words_number = len(text_clean)

for word in text_clean:
    if word.istitle():
        text_istitle.append(word)
    elif word.isupper() and word.isalpha():
        text_isupper.append(word)
    elif word.islower():
        text_islower.append(word)
    elif word.isnumeric():
        numbers.append(word)

numbers_sum = 0
for number in numbers:
    numbers_sum = numbers_sum + int(number)

print(f'''
There are {words_number} words in the selected text.
There are {len(text_istitle)} titlecase words.
There are {len(text_isupper)} uppercase words.
There are {len(text_islower)} lowercase words.
There are {len(numbers)} numeric strings.
The sum of all the numbers {numbers_sum}'''
)

print(separator)
print('LEN', ' |', 'OCCURENCES'.center(35),'| NR.')
print(separator)

colection = dict()

for word in text_clean:
    if len(word) not in colection:
        colection[len(word)] = 1
    else:
        colection[len(word)] += 1

colection_sorted = sorted(list(colection.keys()))

for index in colection_sorted:
    hvezdy = colection[index] * "*"
    print(f'{index:4} | {hvezdy:35} | {colection[index]}')