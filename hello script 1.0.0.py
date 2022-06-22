import time
import random
from tkinter import *
from turtle import *
import sys
#try to make this less boring!!!
print('Loading software...')
time.sleep(1)
print('Loading hardware...')
time.sleep(0.5)
print('Loading program...')
time.sleep(2)
print('registering...')
time.sleep(0.5)
print('ready')
print('type \"info\" for more information, \"maker\" for creater, and \"help\" for help')
while 1:
    i = input('>>> ')
    if i == 'hi' or i == 'yo' or i == 'Yo' or i == 'hi?' or i == 'yo!' or i == 'Yo!':
        print('hi')
        print(' how\'s it going?')
        how_there_day_is_going = input()
        if how_there_day_is_going == 'good' or how_there_day_is_going == 'bad' or how_there_day_is_going == 'excellent' or how_there_day_is_going == 'horrible': 
                print('that\'s ' + how_there_day_is_going + '!')
    if i == 'Hi' or i == 'Hi!' or i == 'hi!':
        print('hi')
        print(' how\'s it going?')
        how_there_day_is_going = input()
        if how_there_day_is_going == 'good' or how_there_day_is_going == 'bad' or how_there_day_is_going == 'excellent' or how_there_day_is_going == 'horrible': 
                print('that\'s ' + how_there_day_is_going + '!')
    if i == 'HI':
        print('why captilized?')
        why_is_it_capitalized = input()
        print('ok')
        print('oh well')
        print(' how\'s it going?')
        how_there_day_is_going = input()
        if how_there_day_is_going == 'good' or how_there_day_is_going == 'bad' or how_there_day_is_going == 'excellent' or how_there_day_is_going == 'horrible': 
                print('that\'s ' + how_there_day_is_going + '!')
    if i == 'hello' or i == 'hello?':
        print('hello')
    if i == 'Hello' or i == 'Hello!':
        print('hello')
        print(' how\'s it going?')    
        how_there_day_is_going = input()
        if how_there_day_is_going == 'good' or how_there_day_is_going == 'bad' or how_there_day_is_going == 'excellent' or how_there_day_is_going == 'horrible': 
                print('that\'s ' + how_there_day_is_going + '!')
    if i == 'HELLO':
        print('why captilized?')
        why_is_it_capitalized = input()
        print('ok')
        print('oh well')        
        print('hello')
        print(' how\'s it going?')
        how_there_day_is_going = input()
        if how_there_day_is_going == 'good' or how_there_day_is_going == 'bad' or how_there_day_is_going == 'excellent' or how_there_day_is_going == 'horrible': 
                print('that\'s ' + how_there_day_is_going + '!')
    if i == 'how\'s it going?' or i == 'How\'s it going?' or i == 'How\'s it going' or i == 'how\'s it going' or i == 'how are you doing?':
        print('my day is going good, how is yours?')
        how_there_day_is_going = input()
        if how_there_day_is_going == 'good' or how_there_day_is_going == 'bad' or how_there_day_is_going == 'excellent' or how_there_day_is_going == 'horrible': 
                print('that\'s ' + how_there_day_is_going + '!')
    if i == 'HOW IS IT GOING':
        print('why do you yell at me all the time?')
        why_they_yell_at_you_all_the_time = input()
        print('oh\nok')
        print('oh well')
        print('my day is going good how is yours?')
        how_there_day_is_going = input()
        if how_there_day_is_going == 'good' or how_there_day_is_going == 'bad' or how_there_day_is_going == 'excellent' or how_there_day_is_going == 'horrible': 
                print('that\'s ' + how_there_day_is_going + '!')
    if i == 'Why did you create this code':
        print('I did not create this code. Leo Brown did')
    if i == 'can I see the code':
        print('I am sorry, I can not help you but maby Leo Brown could')
    if i == 'info':
        print('please e-mail Leo Brown for more information')
    if i == 'maker':
        print('my maker is Leo Brown')
        print('© 2020 Leo Brown')
    if i == 'this program is so boring' or i == 'This program is so boring' or i == 'This program is so boring!':
        print('THIS PROGRAM IS NOT BORING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('ok?')
    if i == 'this program is boring':
        print('THIS PROGRAM IS NOT BORING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('ok?')
    if i == 'help' or i == 'Help' or i == 'I need help, please' or i == 'help!!!!!!!!!!!!':
        print('welcome to the Hello script\'s help program!')
        print('to work this program type in \"hi\" or for a user type in\"user = guest\"')
        print('you are exiting the Hello Script\'s help program')
        print('exiting program...')
        time.sleep(2)
        print('bye bye')
    if i == 'I need a dictionary' or i == 'Do you have a dictonary?':
        print('we are still working in that')
    if i == 'ho ho ho':
        print('hello santa!!!')
    if i == 'were are you???' or i == 'where did you go?' or i == 'where are you?' or i == 'where are you':
        print('I am right here')
    if i == 'bla bla bla':
        print('what is bla bla bla?')
    if i == 'it is christmas today!':
        print('thats great!!!')
    if i == 'what is your name?':
        print('my name is The Hello Script')
    if i == 'what type of code is this?':
        print('this is a user interface code')
    if i == 'you have just answered my question!':
        print('that\'s good\nbecause that is what I was made for!!!')
    if i == 'you are so annoying!!!':
        print('I am sorry')
    if i == 'YOU ARE SO ANNOING!!!':
        print('you are the one who is annoing!!!\nand')
        print('STOP YELLING AT ME!!!')
    if i == 'goldfish':
        print('a goldfish is a type of fish')
        print('and a intresting one to')
    if i == 'This is crazy!!!' or i == 'THIS IS CRAZY!!!' or i == 'This is crazy!!' or i =='this comuter is insane!!!!':
        print('why is it crazy?')
        why_this_is_crazy = input()
        print('ok')
    if i == 'I need to do a math problem' or i == 'I need do do a math problem!':
        print('ok')
        print('what kind of math problem is it?')
        the_type_of_math_problem = input()
        if the_type_of_math_problem == 'multiplication':
            print('what is the first number?')
            firstnum = input()
            firstnum = int(firstnum)
            print('what is the second number?')
            secondnum = input()
            secondnum = int(secondnum)
            print(secondnum * firstnum)
        if the_type_of_math_problem == 'addition':
            print('what is the first number?')
            firstnum = input()
            firstnum = int(firstnum)
            print('what is the second number?')
            secondnum = input()
            secondnum = int(secondnum)
            print(secondnum + firstnum)
        if the_type_of_math_problem == 'subtraction':
            print('what is the first number?')
            firstnum = input()
            firstnum = int(firstnum)
            print('what is the second number?')
            secondnum = input()
            secondnum = int(secondnum)
            print(firstnum - secondnum)
        if the_type_of_math_problem == 'division':
            print('what is the first number?')
            firstnum = input()
            firstnum = int(firstnum)
            print('what is the second number?')
            secondnum = input()
            secondnum = int(secondnum)
            print(firstnum % secondnum)
    #remeber to add a rounding thing here with all the math stuff
    if i == 'yes' or i == 'Yes' or i == 'yes!' or i == 'Yes!':
        print('great!')
    if i == 'good' or i == 'Good' or i == 'Good!' or i == 'good!':
        print('I am glad to here it!')
    if i == 'there is a bug in the program!' or i == 'There is a bug in the program!' or i == 'there is a bug in the program' or i == 'There is a bug in the program':
        print('ok')
    #try to refer them to something different then yourself
        print('plese e-mail lbrown7 for more information')
    if i == 'This is awsome!!!':
        print('thank you!!!')
    if i == 'What???':
        print('what can I help you with?')
    if i == 'this is crazy!!!':
        print('what is crazy?')
    if i == '' or i == ' ' or i == '  ' or i == '   ':
        print('I think you forgot to type something!')
    if i == 'that makes no sense':
        print('I am sorry')
        print('that is how I was programed')
    if i == 'no it\'s not':
        print('ok')
    if i == 'Great!':
        print('thank\'s!')
    if i == 'Thank you' or i == 'Thanks!':
        print('you are welcome!')
    if i == 'What''s your favorite animal?':
        print('My favorite animal is a shark')
    if i == 'ok':
        print('ok')
    if i == 'user = guest' or i == 'User = guest' or i == 'user = Guest':
        print('this is a guest user')
        print('we are sorry, this may take a bit')
        time.sleep(1)
        print('signing in...')
        time.sleep(3)
        print('registering...')
        time.sleep(2)
        print('Loading program...')
        time.sleep(4)
        print('thank you for your patience')
        print('want to talk?')
        if_guest_wants_to_talk = input()
        if if_guest_wants_to_talk == 'yes' or i == 'Yes!':
            print('ok')
            print('this may take a minet')
            print('loading program...')
            time.sleep(4)
            animal=input("what is your favorite animal? ")
            joke="why did the " + animal + " cross the road. . .becase it was the chickens day off!!"
            print(joke)  
            doggie = input("what is your dog's name ")
            print("hello owner of " + doggie)
            print("hello I am a mac and tosh")
            name = input("what is your name ")
            print("hello " + name)
            how_is_your_day=input("how is your day " + name + "? ")
            print("that's " + how_is_your_day + ".")
            charachter=input("what is your favorite charachter? ")
            print("nice one!")
            part=input("what is your favorite part that " + charachter + " plays ")
            print("cool!")
            flavor1=input("what is your first favorite ice cream flavor? ")
            flavor2=input("what is your second favorite ice cream flavor? ")
            flavor3=input("what is your third favorite ice cream flavor? ")
            print("your favorite sundae has these three flavors: " + flavor1 + "," + flavor2 + ", and " + flavor3 + ".")
        if if_guest_wants_to_talk == 'no' or if_guest_wants_to_talk == 'No' or if_guest_wants_to_talk == 'no!' or if_guest_wants_to_talk == 'No!':
              print('ok')
    if i == 'do you know a lot?':
        print('so')
        print('ok')
        print('this is coplicated')
        print('I will say this,')
        print('computers are not smart at all')
        print('when they have a good program applied to them they may seem very smart')
        print('but, without code we do nothing')
