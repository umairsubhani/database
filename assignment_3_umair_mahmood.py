"""
Assignment 3.
"""
from datetime import datetime
from datetime import date
from datetime import timedelta


def main():
    """
    Enter your code below.
    """
    print('Please enter the information below:') #main message display
    while True:
        first_name= input('---->' 'Enter your First Name: ') #First Name
        if not first_name:
            print('Please enter first name') #if empty print this
            continue
        break
    while True:
        last_name= input('---->' 'Enter your Last Name: ') #Last Name
        if not last_name:
            print('Please enter last name') #if empty print this
            continue
        break
    try:
        gender1='male'
        gender2='female'
        gender3='non-binary'
        sex= input('---->' 'Sex (M for male, F for female and N for non-binary): ').upper()
        if sex not in ('M', 'F', 'N'):
            print('Not an appropriate choice, please enter M for male, F for female and N for non-binary ')
            exit()
        age= int(input('---->' 'Enter your age: '))
    except ValueError:
        print('Please enter number') #input numbers only
        exit()
    try:
        d0= date.fromisoformat(input('---->' 'Enter your date of birth as YYYY-mm-dd: '))
        d1 = date.today() - d0
        agedob = d1.days/365
    except ValueError:
        print('Please enter date in YYYY-mm-dd format')
        exit()
    city= input('---->' 'Enter place/city of birth: ')
    try:
        sin= int(input('---->' 'Enter SIN # (no letters or dashes): '))
    except ValueError:
        print('Please enter numbers only without - ') #incase of number or dashes
        exit()
    if sex =='M':
        print(f'{first_name.capitalize()} {last_name.capitalize()} is a {agedob:.0f} years old {gender1}. He was born in {city.capitalize()} and his SIN # is {sin}')
    elif sex =='F':
        print(f'{first_name.capitalize()} {last_name.capitalize()} is a {agedob:.0f} years old {gender2}. She was born in {city.capitalize()} and her SIN # is {sin}')
    else:
        print(f'{first_name.capitalize()} {last_name.capitalize()} is a {agedob:.0f} years old {gender3}. They were born in {city.capitalize()} and their SIN # is {sin}')








# Do not edit below
if __name__ == '__main__':
    main()
