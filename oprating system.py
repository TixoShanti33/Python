#!/usr/bin/python

log = 0
print('Hello please enter the username you would like to use below')
username = input()
print('Ok Hi ' + username)
print('Ok now please enter your passcode below')
password = input()
print('Ok now you are all setup')
print('please enter password to login')
enterpasscode = ('')
while enterpasscode != password:
    print('\/\/\/')
    enterpasscode = input()
    if enterpasscode != password:
        print('Wrong password')

enterpasscode = ('')
log = 1
print("You are logged in")
while True:
    userinput = input()

    if userinput == './change.password./' and log == 1:
        print('please enter current password')
        while enterpasscode != password:
            print('\/\/\/')
            enterpasscode = input()
            if enterpasscode != password:
                print('Wrong password')

        enterpasscode = ("")
        print('please enter new password')
        print('\/\/\/')
        enterpasscode = input()
        password = enterpasscode
        enterpasscode = ("")
        print('your passcode has been changed Successfully!')

    if userinput == "smile" and log == 1:
        print("(:")   

    if userinput == "+" and log == 1:
        number1 = input()
        number2 = input()
        anwser = int(number1) + int(number2)
        print(anwser)

    if userinput == "-" and log == 1:
        number1 = input()
        number2 = input()
        anwser = int(number1) - int(number2)
        print(anwser)

    if userinput == "./log.out./" and log == 1:
        log = 0
        print("logged out")

    if userinput == "./log.in./" and log == 0:
        print("Please enter password for " + username)
        while enterpasscode != password:
            print('\/\/\/')
            enterpasscode = input()
            if enterpasscode != password:
                print('Wrong password')
        enterpasscode = ""
        log = 1
        print("Logged in Successfully!")
    
    
    if userinput == "*" and log == 1:
        number1 = input()
        number2 = input()
        anwser = int(number1) * int(number2)
        print(anwser)

    if userinput == "sq" and log == 1:
        number1 = input()
        anwser = int(number1) * int(number1)
        print(anwser)

    if userinput == "do" and log == 1:
        number1 = input()
        anwser = int(number1) + int(number1)
        print(anwser)

    if userinput == "BIG" and log == 1:
        print("___       _____       ______   ")
        print("|  \        |        /         ")
        print("|  |        |        |         ")
        print("|__/        |        |   ___   ")
        print("|  \        |        \      \  ")
        print("|   |       |         \     |  ")
        print("|___/     __|__        \____/  ")

    if userinput == "/" and log == 1:
        number1 = input()
        number2 = input()
        anwser = int(number1) / int(number2)
        print(anwser)

    if userinput == "sudo ./change.name.system.user./" and log == 1:
        print("Please enter password to change name")
        while enterpasscode != password:
            print('\/\/\/')
            enterpasscode = input()
            if enterpasscode != password:
                print('Wrong password')
        enterpasscode = ""
        print("Please enter new username")
        print("\/\/\/")
        username = input()
        print("Hello "+username)
        print("You have been logged out and your username is changed")
        log = 0

    if userinput == "whatismyname" and log == 1:
        print(username)
