import random


def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)


def create():
    special = ['?', '!', '.', '#']
    UpperLet = chr(random.randint(65, 90))
    UpperLet1 = chr(random.randint(65, 90))
    LowerLet = chr(random.randint(97, 122))
    LowerLet1 = chr(random.randint(97, 122))
    no1 = chr(random.randint(48, 57))
    no2 = chr(random.randint(48, 57))
    Special = (special[random.randint(0, 3)])
    Password = UpperLet + UpperLet1 + LowerLet + LowerLet1 + no2 + no1 + Special
    Password = shuffle(Password)
    print('Your password is: ', Password)
    UInp = input('Do you want to generate another password?')
    if UInp == 'yes':
        create()
    elif UInp == 'no':
        quit()


create()
