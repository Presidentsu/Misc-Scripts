import re
def my_func():
    Value = 0
    my_pass = input("Gib password: ")
    if re.search('[a-z]', my_pass):
        Value = Value + 1
    if re.search('[A-Z]', my_pass):
        Value = Value + 1
    if re.search('[0-9]', my_pass):
        Value = Value + 1
    if re.search('[!@#$%^&*()~_+:?><.,;=-]', my_pass):
        Value = Value + 1
    if len(my_pass) < 6:
        print("Not good do better")
    if len(my_pass) < 9:
        print("You can still do better")
    if len(my_pass) >= 9:
        print("Ok looks promising") 
    if Value == 4:
        print("Good but not better")
    if Value < 4:
        print("Do better mf")
    return 0

my_func()